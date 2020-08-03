from ..category import Category
import json

forensics_tools = list({})

with open('src/toolsList.json', 'r') as json_list:
    toolsList = json.load(json_list)

for tool in toolsList:
    if 'forensics' in tool.get('categories'):
       forensics_tools.append(tool)

forensics = Category(forensics_tools)