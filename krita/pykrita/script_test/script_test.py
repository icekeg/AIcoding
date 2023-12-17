from krita import *

def scripter_trigger():
    Krita.instance().action("python_scripter").trigger()