#!/usr/bin/env python
import sys
import time
import re

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
        s = self.read_statement(permit_eof=False)
        if s != "ISO-10303-21":
            raise SyntaxError("Unknown format '{fmt}'".format(fmt=s))

        # read everything until "DATA"
        in_header = False
        self.header = STEPHeader()
        while True:
            s = self.read_statement(permit_eof=False)
            if s == "DATA":
                break

            if s == "HEADER":
                in_header = True
            elif s == "ENDSEC":
                in_header = False
            elif in_header:
                # parse the statement and use it as header definition
                e = parse_entity(s)
                self.header.add(e)

        last_printout_time = time.time()
        # read all entities from the input
        while True:
            s = self.read_statement()
            if s == None:
                break
            # print "Statement: {s}".format(s=s)

            if s == "ENDSEC":
                break

            # split to 'Index=Entity'
            equal_pos = s.find("=")
            if s[0] != "#" or equal_pos == -1:
                raise SyntaxError("Invalid entity definition '{val}'".format(val=s))

            index = int(s[1:equal_pos])

            expression = s[equal_pos + 1:].strip()

            if self.__expression_is_complex_entity_instance(expression=expression):
                self.__process_complex_entity(
                    expression=expression,
                    index=index)

            else:
                self.__process_simple_entity(
                    expression=expression,
                    index=index)

            now = time.time()
            if (last_printout_time + 1) <= now:
                last_printout_time = now
                sys.stderr.write("  index={i}\n".format(i=index))

            # print "  type={t}".format(t=entity.rtype)
            # print "  args={a}".format(a=entity.args)

        self.fd.close()

    # vim: set sw=4 ts=4 et:

    def __process_complex_entity(
            self,
            expression: str,
            index: int):
        simple_entity_instances = \
            self.__get_all_simple_entity_instances_in_compex_entity_instance(
                expression=expression)

        for simple_entity_instance in simple_entity_instances:
            entity = parse_entity(simple_entity_instance)

            entity.code_block = expression

            if index > 0:
                self.entities[index] = entity

    def __process_simple_entity(
            self,
            expression: str,
            index: int):
        entity = \
            parse_entity(
                expression)

        entity.code_block = \
            expression

        if index > 0:
            self.entities[index] = entity

    def __expression_is_complex_entity_instance(
            self,
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

    def __get_all_simple_entity_instances_in_compex_entity_instance(
            self,
            expression: str) \
            -> list:
        complex_entity_instane_pattern = re.compile(pattern='[^()]+\([^\()]*\)')

        simple_entity_instances = \
            complex_entity_instane_pattern.findall(
                string=expression)

        return \
            simple_entity_instances
