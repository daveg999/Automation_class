import pprint
import yaml
import json

# import/read yaml file

with open("class1_list.yml") as f:
  ex7_output = yaml.load(f)

# import/read json file

with open("class1_list.json") as f:
  ex7_output.append(json.load(f))

# pretty print combined output

pprint.pprint(ex7_output)

