"""
Strange behavior in simple inheritance
"""


class Library:
    # only Interface instances can call this method since there's no
    # interface_method() method in Library class, but there's in Interface class
    def call_interface_method(self):
        self.interface_method()


class Interface(Library):
    def interface_method(self):
        print("Method being called from interface.")


i1 = Interface()
i1.call_interface_method()
