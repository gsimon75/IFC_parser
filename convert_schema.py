#!/usr/bin/env python
import sys
import argparse 
from Ifc import SchemaParser
from jinja2 import Environment, FileSystemLoader, Template, contextfilter
from jinja2.runtime import Context
from jinja2 import Undefined

# parse the commandline arguments
ap = argparse.ArgumentParser(                                                                                                                                       
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,                                                                                                       
        description = "Convert an Express schema to a python module containing parser classes",                                     
        )
ap.add_argument("-s", "--schema", required=True, help = "the input schema file")                                                                          
ap.add_argument("-m", "--module", required=True, help = "the output python module file")                                                                             
args = vars(ap.parse_args())                                                                                                                                        

# initialise the jinja2 engine
env = Environment(
    loader = FileSystemLoader('./templates'),
    trim_blocks=True,
    lstrip_blocks=True
    )

# a handy jinja extension
@contextfilter
def filter_apply(ctx, args, macro, *param):
    return map(lambda x: ctx.call(macro, x, *param), args)
env.filters['apply'] = filter_apply

# read the templates
entity_template = env.get_template("entity_parser.template.py")
typedef_template = env.get_template("type_parser.template.py")

# initialise the schema parser and read the input
parser = SchemaParser()
schema = parser.read_schema_file(args["schema"])

# dump everything
#for classname, definitions in schema.classes.iteritems():
#    print("-- {cn} definitions:".format(cn=classname))
#    for defname, definition in definitions.iteritems():
#        print("  {d}".format(d=definition))
#sys.exit(0)
# dump only one class
#schema.classes["ENTITY"]["IfcRelContainedInSpatialStructure"].dump_python_class(sys.stdin)
#sys.exit(0)

primitive_types = ["BOOLEAN", "REAL", "BINARY", "INTEGER", "NUMBER", "STRING", "LOGICAL"]
# create the output file and write the necessary import statements
fd = open(args["module"], "w")
fd.write("from ClassRegistry import ifc_class, ifc_abstract_class\n")
fd.write("from IfcBase import IfcEntity, {pr}\n".format(pr=", ".join(primitive_types)))
fd.write("from Misc import parse_uuid\n")
# I know it's a hack, but I need `str()` to handle non-ascii characters
# *I know* that utf8 output will be fine, so dear python please let me use it...
# No, I definitely WON'T explicitely write `x.encode(...)` everywhere
fd.write("import sys\n")
fd.write("reload(sys)\n")
fd.write("sys.setdefaultencoding('UTF8')\n")
fd.write("\n")

# Python requires the base class declared before the derived classes, so we'll proceed step
# by step, always dump those entities whose prerequisites are already dumped.
remaining = filter(lambda t: t.ttype == "SCALAR", schema.classes["TYPE"].values())
already_dumped = set(primitive_types)
while remaining:
    for typedef in list(remaining):
        if typedef.basetype in already_dumped:
            typedef_template.stream(typedef.__dict__).dump(fd)
            remaining.remove(typedef)
            already_dumped.add(typedef.defname)

# Python requires the base class declared before the derived classes, so we'll proceed step
# by step, always dump those entities whose prerequisites are already dumped.
remaining = schema.classes["ENTITY"].values()
already_dumped = set()
while remaining:
    for entity in list(remaining):
        if not entity.subtype_of or entity.subtype_of in already_dumped:
            entity_template.stream(entity.__dict__).dump(fd)
            remaining.remove(entity)
            already_dumped.add(entity.defname)

# write a vim modeline and close the output
fd.write("# vim: set sw=4 ts=4 et:\n")
fd.close()

# vim: set sw=4 ts=4 et:
