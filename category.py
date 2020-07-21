import os

class Category:

    def __init__(self, tools):
        self.tools = tools

    def getToolList(self):
        return self.tools

    def getTool(self, toolName):
        for tool in self.tools: 
            if tool.get('name') == toolName:
                return tool.get
    def install(self):
        for tool in self.tools: 
            print("Instalando {}".format(tool.get('name')))
            codigo = tool.parse(' ')
            print(codigo)    