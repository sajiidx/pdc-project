# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sobel
else:
    import _sobel

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _sobel.delete_SwigPyIterator

    def value(self):
        return _sobel.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _sobel.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _sobel.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _sobel.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _sobel.SwigPyIterator_equal(self, x)

    def copy(self):
        return _sobel.SwigPyIterator_copy(self)

    def next(self):
        return _sobel.SwigPyIterator_next(self)

    def __next__(self):
        return _sobel.SwigPyIterator___next__(self)

    def previous(self):
        return _sobel.SwigPyIterator_previous(self)

    def advance(self, n):
        return _sobel.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _sobel.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _sobel.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _sobel.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _sobel.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _sobel.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _sobel.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _sobel:
_sobel.SwigPyIterator_swigregister(SwigPyIterator)

class VecDouble(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _sobel.VecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _sobel.VecDouble___nonzero__(self)

    def __bool__(self):
        return _sobel.VecDouble___bool__(self)

    def __len__(self):
        return _sobel.VecDouble___len__(self)

    def __getslice__(self, i, j):
        return _sobel.VecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _sobel.VecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _sobel.VecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _sobel.VecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _sobel.VecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _sobel.VecDouble___setitem__(self, *args)

    def pop(self):
        return _sobel.VecDouble_pop(self)

    def append(self, x):
        return _sobel.VecDouble_append(self, x)

    def empty(self):
        return _sobel.VecDouble_empty(self)

    def size(self):
        return _sobel.VecDouble_size(self)

    def swap(self, v):
        return _sobel.VecDouble_swap(self, v)

    def begin(self):
        return _sobel.VecDouble_begin(self)

    def end(self):
        return _sobel.VecDouble_end(self)

    def rbegin(self):
        return _sobel.VecDouble_rbegin(self)

    def rend(self):
        return _sobel.VecDouble_rend(self)

    def clear(self):
        return _sobel.VecDouble_clear(self)

    def get_allocator(self):
        return _sobel.VecDouble_get_allocator(self)

    def pop_back(self):
        return _sobel.VecDouble_pop_back(self)

    def erase(self, *args):
        return _sobel.VecDouble_erase(self, *args)

    def __init__(self, *args):
        _sobel.VecDouble_swiginit(self, _sobel.new_VecDouble(*args))

    def push_back(self, x):
        return _sobel.VecDouble_push_back(self, x)

    def front(self):
        return _sobel.VecDouble_front(self)

    def back(self):
        return _sobel.VecDouble_back(self)

    def assign(self, n, x):
        return _sobel.VecDouble_assign(self, n, x)

    def resize(self, *args):
        return _sobel.VecDouble_resize(self, *args)

    def insert(self, *args):
        return _sobel.VecDouble_insert(self, *args)

    def reserve(self, n):
        return _sobel.VecDouble_reserve(self, n)

    def capacity(self):
        return _sobel.VecDouble_capacity(self)
    __swig_destroy__ = _sobel.delete_VecDouble

# Register VecDouble in _sobel:
_sobel.VecDouble_swigregister(VecDouble)

class VecVecDouble(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _sobel.VecVecDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _sobel.VecVecDouble___nonzero__(self)

    def __bool__(self):
        return _sobel.VecVecDouble___bool__(self)

    def __len__(self):
        return _sobel.VecVecDouble___len__(self)

    def __getslice__(self, i, j):
        return _sobel.VecVecDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _sobel.VecVecDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _sobel.VecVecDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _sobel.VecVecDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _sobel.VecVecDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _sobel.VecVecDouble___setitem__(self, *args)

    def pop(self):
        return _sobel.VecVecDouble_pop(self)

    def append(self, x):
        return _sobel.VecVecDouble_append(self, x)

    def empty(self):
        return _sobel.VecVecDouble_empty(self)

    def size(self):
        return _sobel.VecVecDouble_size(self)

    def swap(self, v):
        return _sobel.VecVecDouble_swap(self, v)

    def begin(self):
        return _sobel.VecVecDouble_begin(self)

    def end(self):
        return _sobel.VecVecDouble_end(self)

    def rbegin(self):
        return _sobel.VecVecDouble_rbegin(self)

    def rend(self):
        return _sobel.VecVecDouble_rend(self)

    def clear(self):
        return _sobel.VecVecDouble_clear(self)

    def get_allocator(self):
        return _sobel.VecVecDouble_get_allocator(self)

    def pop_back(self):
        return _sobel.VecVecDouble_pop_back(self)

    def erase(self, *args):
        return _sobel.VecVecDouble_erase(self, *args)

    def __init__(self, *args):
        _sobel.VecVecDouble_swiginit(self, _sobel.new_VecVecDouble(*args))

    def push_back(self, x):
        return _sobel.VecVecDouble_push_back(self, x)

    def front(self):
        return _sobel.VecVecDouble_front(self)

    def back(self):
        return _sobel.VecVecDouble_back(self)

    def assign(self, n, x):
        return _sobel.VecVecDouble_assign(self, n, x)

    def resize(self, *args):
        return _sobel.VecVecDouble_resize(self, *args)

    def insert(self, *args):
        return _sobel.VecVecDouble_insert(self, *args)

    def reserve(self, n):
        return _sobel.VecVecDouble_reserve(self, n)

    def capacity(self):
        return _sobel.VecVecDouble_capacity(self)
    __swig_destroy__ = _sobel.delete_VecVecDouble

# Register VecVecDouble in _sobel:
_sobel.VecVecDouble_swigregister(VecVecDouble)


def SobelOperator(img):
    return _sobel.SobelOperator(img)


