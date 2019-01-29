from cudatext import *
import sys
import os

sys.path.append(os.path.dirname(__file__))
import slimit
import format_proc

format_proc.MSG = '[JS Minifier] '
format_proc.INI = ''

def do_format(text):
    return slimit.minify(text, mangle=True, mangle_toplevel=True)

class Command:
    def run(self):
        format_proc.run(do_format)

    def save_to_min_js(self):
        format_proc.min_js(do_format)