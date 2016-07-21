""" Class Widget: traverse dependency tree (recursion) """

class Widget(object):

    def __init__(self,name):
        self.name = name
        self.dependencies = []

    def add_dependency(self,*widgets):
        for widget in widgets: self.dependencies.append(widget)

    def build_internal(self,name_list):
        if self.name in name_list: return []
        for dependency in self.dependencies:
            dependency_name_list = dependency.build_internal(name_list)
            for name in dependency_name_list:
                if name not in name_list: name_list.append(name)
        name_list.append(self.name)
        return name_list

    def build(self):
        name_list = self.build_internal([])
        print name_list[0:-1]


#### MAIN ####

luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)