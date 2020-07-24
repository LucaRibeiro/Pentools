from ..category import Category
import json

def essentials():
    essentialsTools = list({})

    with open('src/toolsList.json', 'r') as json_list:
        toolsList = json.load(json_list)

    for tool in toolsList:
        if tool.get('essential-tool'):
        essentialsTools.append(tool)

    essentialsTools = Category(essentialsTools)
    essentialsTools.installWithoutUI()