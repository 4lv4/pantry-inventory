#Here the Json file will be created and updated this is not where the classes are created they are created and updated from the Json file
import json
inventory = r'data\inventory.json'
with open(inventory, 'w', encoding = 'utf-8') as inv:
    json.dump(inv, 'new_dict')
with open(inventory, 'r', encoding = 'utf-8') as inv:
    print(json.load(inv))