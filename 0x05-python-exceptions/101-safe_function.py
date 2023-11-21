#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        import sys
        print("Exception: {}".format(str(e)), file=sys.stderr)
        return None
