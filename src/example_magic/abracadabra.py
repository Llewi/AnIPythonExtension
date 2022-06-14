from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic, display, HTML)

@magics_class
class Abracadabra(Magics):

    @line_magic
    def abra(self, line):
        return line

    @cell_magic
    def cadabra(self, line, cell):
        return line, cell

    def vanilla_method():
        return "literally no flavour"

    @line_magic
    def it_is_html(self, line):
        return display(HTML('<h1>Hello, world!</h1>'))
