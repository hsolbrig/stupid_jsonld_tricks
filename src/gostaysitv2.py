import os
from json import load, dumps
from pyld import jsonld

from src import input_dir, output_dir

with open(os.path.join(input_dir, 'prefixes.json')) as docf:
    doc = load(docf)
with open(os.path.join(input_dir, 'prefixes.context.jsonld')) as ctxtf:
    ctxt = load(ctxtf)

compacted = jsonld.compact(doc, ctxt)
with open (os.path.join(output_dir, 'prefixes.compacted.jsonld'), 'w') as f3:
    f3.write(dumps(compacted, indent=2))
