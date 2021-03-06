'''
Pure Python wrapper to the Yajl C library

.. data:: __version__

    Version of yajl-py

.. data:: yajl_version

    Version of the yajl library that was loaded
'''

from yajl_common import *
from yajl_parse import *
from yajl_gen import *

__version__ = '2.0.5' 
yajl_version = get_yajl_version()

def check_yajl_version():
    '''
    :rtype: bool

    Returns True, if the version of yajl is identical to the version of yajl-py
    otherwise displays a RuntimeWarning and returns False.
    '''
    if __version__ != yajl_version:
        import warnings
        warnings.warn(
            'Using Yajl-Py v%s with Yajl v%s. '
            'It is advised to use the same Yajl-Py and Yajl versions' %(
                __version__, yajl_version),
            RuntimeWarning, stacklevel=3)
        return False
    return True

check_yajl_version()
