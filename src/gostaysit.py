import os

from rdflib import Graph

from src import input_dir, output_dir

g = Graph()
g.parse(os.path.join(input_dir, 'prefixes.json'), format='json-ld', context= os.path.join(input_dir, 'prefixes.context.jsonld'))
g.serialize(os.path.join(output_dir, 'prefixes.ttl'), format='turtle')