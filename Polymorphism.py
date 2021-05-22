# Duck Typing

class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")

class My_editor:

        def execute(self):
            print("Spell Check")
            print("Convention Check")
            print("Compiling")
            print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = My_editor()  # the type of ide is Myeditor
lap1 = Laptop()  # creating the obj of laptop
lap1.code(ide)
