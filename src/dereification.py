import os
from rdflib import Graph
from src import input_dir, output_dir

# Step one -- convert the tags to indices
g = Graph()
g.parse(os.path.join(input_dir, 'dereification.json'), format="json-ld",
       context=os.path.join(input_dir, 'dereification_p1.context.jsonld'))
output = g.serialize(format='json-ld', auto_compact=True).decode()

# Bug in json-ld processor -- "@index" gets combined with the default namespace...
output = output.replace('http://example.org/@index', '@index')
p1_json = os.path.join(output_dir, 'dereification_p1x.jsonld')
with open(p1_json, 'w') as f:
       f.write(output)

# Step two -- convert the indices to predicates
g = Graph()
g.parse(p1_json, format="json-ld", context=os.path.join(input_dir, 'dereification_p2.context.jsonld'))
output2 = g.serialize(format='json-ld').decode()
output2 = output2.replace('http://example.org/@index', '@index')

g = Graph()
g.parse(data=output2, format='json-ld')
g.serialize(os.path.join(output_dir, 'dereification.ttl'), format='ttl')
