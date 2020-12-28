import math
import re
import sys
import time

from Ifc.IfcBase import STEPHeader
from Ifc.Misc import StatementFileReader, parse_entity


class Database(StatementFileReader):
    """
    Read a textfile and parse it into a list of entities
    """

    def __init__(self):
        """
        Initialise the parser
        """
        StatementFileReader.__init__(self, comment_open="/*", comment_close="*/")
        self.header = None
        self.entities = {}

    def read_data_file(self, filename):
        """
        Open a file and read its header, right up until the "DATA" statement.
        """
        self.fd = open(filename, "r")
        self.reset_state()

        # read format statement
        statement = self.read_statement(permit_eof=False)
        if statement != "ISO-10303-21":
            raise SyntaxError("Unknown format '{fmt}'".format(fmt=statement))

        # read everything until "DATA"
        in_header = False
        self.header = STEPHeader()
        while True:
            statement = self.read_statement(permit_eof=False)
            if statement == "DATA":
                break

            if statement == "HEADER":
                in_header = True
            elif statement == "ENDSEC":
                in_header = False
            elif in_header:
                # parse the statement and use it as header definition
                e = parse_entity(statement)
                self.header.add(e)

        last_printout_time = time.time()
        # read all entities from the input
        while True:
            statement = self.read_statement()
            if statement is None:
                break
            # print "Statement: {statement}".format(statement=statement)

            if statement == "ENDSEC":
                break

            # split to 'Index=Entity'
            equal_pos = statement.find("=")
            if statement[0] != "#" or equal_pos == -1:
                raise SyntaxError("Invalid entity definition '{val}'".format(val=statement))

            index = int(statement[1:equal_pos])

            expression = statement[equal_pos + 1:].strip()

            if self.__expression_is_complex_entity_instance(expression=expression):
                self.__process_complex_entity(
                    statement=statement,
                    expression=expression,
                    complex_entity_index=index)

            else:
                self.__process_simple_entity(
                    statement=statement,
                    expression=expression,
                    simple_entity_index=index)

            now = time.time()
            if (last_printout_time + 1) <= now:
                last_printout_time = now
                sys.stderr.write("  index={i}\n".format(i=index))

            # print "  type={t}".format(t=entity.rtype)
            # print "  args={a}".format(a=entity.args)

        self.fd.close()

    def __process_complex_entity(
            self,
            statement: str,
            expression: str,
            complex_entity_index: int):
        simple_entity_instances = \
            self.__get_all_simple_entity_instances_in_compex_entity_instance(
                expression=expression)

        simple_entity_index_step = \
            self.__find_index_step_for_simple_entities(
                complex_entity_count=len(simple_entity_instances))

        simple_entity_count = 0

        for simple_entity_instance in simple_entity_instances:
            simple_entity_count += 1

            entity = parse_entity(simple_entity_instance)

            entity.code_block = \
                statement

            simple_entity_index = \
                complex_entity_index + simple_entity_count * simple_entity_index_step

            if complex_entity_index > 0:
                self.entities[simple_entity_index] = entity

    def __process_simple_entity(
            self,
            statement: str,
            expression: str,
            simple_entity_index: int):
        entity = \
            parse_entity(
                expression)

        entity.code_block = \
            statement

        if simple_entity_index > 0:
            self.entities[simple_entity_index] = entity

    @staticmethod
    def __expression_is_complex_entity_instance(
            expression: str) \
            -> bool:
        if expression[0] == '(' and expression[-1] == ')' and len(expression) > 2:
            if expression[1] == '*':
                return False
            else:
                return True
        else:
            return \
                False

    @staticmethod
    def __get_all_simple_entity_instances_in_compex_entity_instance(
            expression: str) \
            -> list:
        complex_entity_instane_pattern = re.compile(pattern='[^()]+\([^\()]*\)')

        simple_entity_instances = \
            complex_entity_instane_pattern.findall(
                string=expression)

        return \
            simple_entity_instances

    @staticmethod
    def __find_index_step_for_simple_entities(
            complex_entity_count: int) \
            -> float:
        simple_entity_index_depth = \
            math.ceil(math.log10(complex_entity_count))

        simple_entity_index_step = \
            1.0 / math.pow(10, simple_entity_index_depth)

        return \
            simple_entity_index_step
