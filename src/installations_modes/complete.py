from ..category import Category
import json

def complete():
    with open('src/toolsList.json', 'r') as json_list:
        toolsList = json.load(json_list)

    tools = Category(toolsList)
    tools.installWithoutUI()