import os

class Category():
    tools = []

    def __init__(self, tools):
        Category.tools = tools

    def getToolList(self):
        return self.tools

    def getTool(self, toolName):
        for tool in self.tools:
            if tool.get('name') == toolName:
                return tool

    def installTool(self, tool):
        print("\033[1;32mInstalando {}\033[0;0m".format(tool.get('package')))
        codigo = tool.get('installation')
        os.system(codigo)

    def installWithoutUI(self):
        for tool in self.tools:
            if not(tool.get('requiresUI')):
                self.installTool(tool)

    def installAll(self):
        for tool in self.tools:
            self.installTool(tool)

    def installEssentialsWithoutUI(self):
        for tool in self.tools:
            if not(tool.get('RequiresUI')) and tool.get('essential-tool'):
                self.installTool(tool)

    def installEssentials(self):
        for tool in self.tools:
            if tool.get('essential-tool'):
                self.installTool(tool)