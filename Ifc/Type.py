# START EDIT - AMi 20201210 - added to store code block
import os
# END EDIT

from nf_express_source.ifc_parser.Ifc.ClassRegistry import ifc_definition


@ifc_definition
class Type:
    """
    A TYPE definition in an Express schema
    NOTE: Parsed only as deep as necessary
    """

    def __init__(self, classname, defname, defspec, parser):
        self.classname = classname
        self.defname = defname

        # START EDIT - AMi 20201210 - added to store code block
        self.code_block = \
            self.classname + ' ' + self.defname + ';'

        if defspec:
            self.code_block += \
                os.linesep + defspec
        # END EDIT

        if defspec == None and parser == None:
            return
        if not defspec.startswith("="):
            raise SyntaxError("Specification of Type {dn} should start with '='".format(dn=defname))
        defspec = defspec[1:].lstrip()

        # don't care about string length
        if defspec.startswith("STRING("):
            defspec = "STRING"

        if defspec.startswith("ARRAY ") or defspec.startswith("LIST ") or defspec.startswith("SET "):
            self.ttype = "LIST"
            # nothing to do, iterative types are implicitely parsed as list
            pass
        elif defspec.startswith("ENUMERATION OF ("):
            self.ttype = "ENUM"
            # nothing to do, enums are only declared and their values used, but the typename doesn't appear in expressions
            pass
        elif defspec.startswith("SELECT ("):
            self.ttype = "UNION"
            # doesn't occur either, refs are parsed implicitely
            pass
        else:
            self.ttype = "SCALAR"
            self.basetype = defspec
            pass

        if parser is None:
            return

        # process constraints, FIXME: now just skip them
        while True:
            # START EDIT - AMi 20201210 - changed first line to keep whitespaces for code_block text
            s = parser.read_statement(permit_eof=False, zap_whitespaces=False)

            self.code_block += \
                os.linesep + s + ';'

            s = \
                s.strip()
            # END EDIT
            if s == "END_TYPE":
                break

    def __str__(self):
        return "Type({dn}) {ds}".format(dn=self.defname, ds=self.defspec)

# vim: set sw=4 ts=4 et:
