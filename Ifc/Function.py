# START EDIT - AMi 20201210 - added to store code block
import os
# END EDIT

from Ifc.ClassRegistry import ifc_definition


@ifc_definition
class Function:
    """
    A FUNCTION definition in an Express schema
    NOTE: Parsed only as deep as necessary
    """

    def __init__(self, classname, defname, defspec, parser):
        self.classname = classname
        self.defname = defname
        self.defspec = defspec

        # START EDIT - AMi 20201210 - added to store code block
        self.code_block = \
            self.classname + ' ' + self.defname + ';'

        if defspec:
            self.code_block += \
                os.linesep + defspec
        # END EDIT

        # process body, FIXME: now just skip it
        while True:
            # START EDIT - AMi 20201210 - changed first line to keep whitespaces for code_block text
            s = parser.read_statement(permit_eof=False, zap_whitespaces=False)

            self.code_block += \
                os.linesep + s + ';'

            s = \
                s.strip()
            # END EDIT
            if s == "END_FUNCTION":
                break

    def __str__(self):
        return "Function({dn}) {ds}".format(dn=self.defname, ds=self.defspec)

# vim: set sw=4 ts=4 et:
