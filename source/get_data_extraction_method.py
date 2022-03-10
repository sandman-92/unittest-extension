import sys

def get_data_extraction_method(sys_filepath = None,
                               name=None,
                               globals=None,
                               locals=None,
                               fromlist=(),
                               level=0):
    """
    This function appends a sys filepath and returns the imported method.
    assumes the function returned is <module>_extract
    :param sys_filepath:
    :return:
    """
    sys.path.append(sys_filepath)

    return __import__(name=name, globals=globals, locals=locals, fromlist=fromlist,level=level)
