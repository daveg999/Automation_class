import yaml
import json

yaml_list = range(5)
yaml_list.append('string1')
yaml_list.append('string2')
yaml_list.append({})
yaml_list[-1]
{}
yaml_list[-1]['critter1'] = 'hedgehog'
yaml_list[-1]['critter2'] = 'bunny'
yaml_list[-1]['dungeon_levels'] = range(5)
yaml_list.append('list_end')

with open("class1_list.yml", "w") as f:
  f.write(yaml.dump(yaml_list, default_flow_style=False))
  
with open("class1_list.json", "w") as f:
  json.dump(yaml_list, f)

