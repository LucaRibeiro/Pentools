#!/usr/bin/python3
from ..category import Category
import json

web_tools = list({})

with open('src/toolsList.json', 'r') as json_list:
    toolsList = json.load(json_list)

for tool in toolsList:
    if 'web' in tool.get('categories'):
       web_tools.append(tool)

web_application_analisys = Category(web_tools)