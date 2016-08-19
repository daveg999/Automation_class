from ciscoconfparse import CiscoConfParse

# load exercise config file into variable

input_file = CiscoConfParse("cisco_ipsec.txt")

# find crypto map entries

crypto = input_file.find_objects(r"^crypto map CRYPTO")

# print out crypto map entries and their children

for c in crypto:
  print c.text
  for child in c.all_children:
    print child.text


