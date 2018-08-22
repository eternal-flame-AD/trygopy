""""""
import collections
import os
import sys
import cffi as _cffi_backend

_PY3 = sys.version_info[0] == 3

ffi = _cffi_backend.FFI()
ffi.cdef("""
typedef signed char GoInt8;
typedef unsigned char GoUint8;
typedef short GoInt16;
typedef unsigned short GoUint16;
typedef int GoInt32;
typedef unsigned int GoUint32;
typedef long long GoInt64;
typedef size_t GoUintptr;
typedef unsigned long long GoUint64;
typedef GoInt64 GoInt;
typedef GoUint64 GoUint;
typedef float GoFloat32;
typedef double GoFloat64;
typedef struct { const char *p; GoInt n; } GoString;
typedef void *GoMap;
typedef void *GoChan;
typedef struct { void *t; void *v; } GoInterface;
typedef struct { void *data; GoInt len; GoInt cap; } GoSlice;
typedef struct { GoFloat32 real; GoFloat32 imag; } GoComplex64;
typedef struct { GoFloat64 real; GoFloat64 imag; } GoComplex128;

extern GoComplex64 _cgopy_GoComplex64(GoFloat32 p0, GoFloat32 p1);
extern GoComplex128 _cgopy_GoComplex128(GoFloat64 p0, GoFloat64 p1);
extern GoString _cgopy_GoString(char* p0);
extern char* _cgopy_CString(GoString p0);
extern void _cgopy_FreeCString(char* p0);
extern GoUint8 _cgopy_ErrorIsNil(GoInterface p0);
extern char* _cgopy_ErrorString(GoInterface p0);
extern void cgopy_incref(void* p0);
extern void cgopy_decref(void* p0);

extern void cgo_pkg_trygopy_init();

extern GoString cgo_func_trygopy_Echo(GoString p0);
extern GoInt cgo_func_trygopy_HeavyCalc(GoInt p0);
""")

# python <--> cffi helper.
class _cffi_helper(object):

    here = os.path.dirname(os.path.abspath(__file__))
    lib = ffi.dlopen(os.path.join(here, "_trygopy.so"))

    @staticmethod
    def cffi_cgopy_cnv_py2c_bool(o):
        return ffi.cast('_Bool', o)

    @staticmethod
    def cffi_cgopy_cnv_py2c_complex64(o):
        real = o.real
        imag = o.imag
        complex64 = _cffi_helper.lib._cgopy_GoComplex64(real, imag)
        return complex64

    @staticmethod
    def cffi_cgopy_cnv_py2c_complex128(o):
        real = o.real
        imag = o.imag
        complex128 = _cffi_helper.lib._cgopy_GoComplex128(real, imag)
        return complex128

    @staticmethod
    def cffi_cgopy_cnv_py2c_string(o):
        if _PY3:
            o = o.encode('ascii')
        s = ffi.new("char[]", o)
        return _cffi_helper.lib._cgopy_GoString(s)

    @staticmethod
    def cffi_cgopy_cnv_py2c_int(o):
        return ffi.cast('int', o)

    @staticmethod
    def cffi_cgopy_cnv_py2c_float32(o):
        return ffi.cast('float', o)

    @staticmethod
    def cffi_cgopy_cnv_py2c_float64(o):
        return ffi.cast('double', o)

    @staticmethod
    def cffi_cgopy_cnv_py2c_uint(o):
        return ffi.cast('uint', o)

    @staticmethod
    def cffi_cgopy_cnv_c2py_bool(c):
        return bool(c)

    @staticmethod
    def cffi_cgopy_cnv_c2py_complex64(c):
         return complex(c.real, c.imag)

    @staticmethod
    def cffi_cgopy_cnv_c2py_complex128(c):
         return complex(c.real, c.imag)

    @staticmethod
    def cffi_cgopy_cnv_c2py_string(c):
        s = _cffi_helper.lib._cgopy_CString(c)
        pystr = ffi.string(s)
        _cffi_helper.lib._cgopy_FreeCString(s)
        if _PY3:
            pystr = pystr.decode('utf8')
        return pystr

    @staticmethod
    def cffi_cgopy_cnv_c2py_errstring(c):
        s = _cffi_helper.lib._cgopy_ErrorString(c)
        pystr = ffi.string(s)
        _cffi_helper.lib._cgopy_FreeCString(s)
        if _PY3:
            pystr = pystr.decode('utf8')
        return pystr

    @staticmethod
    def cffi_cgopy_cnv_c2py_int(c):
        return int(c)

    @staticmethod
    def cffi_cgopy_cnv_c2py_float32(c):
        return float(c)

    @staticmethod
    def cffi_cgopy_cnv_c2py_float64(c):
        return float(c)

    @staticmethod
    def cffi_cgopy_cnv_c2py_uint(c):
        return int(c)

# make sure Cgo is loaded and initialized
_cffi_helper.lib.cgo_pkg_trygopy_init()

# pythonization of: trygopy.Echo 
def Echo(s):
    """Echo(str s) str"""
    c_s = _cffi_helper.cffi_cgopy_cnv_py2c_string(s)
    cret = _cffi_helper.lib.cgo_func_trygopy_Echo(c_s)
    ret = _cffi_helper.cffi_cgopy_cnv_c2py_string(cret)
    return ret


# pythonization of: trygopy.HeavyCalc 
def HeavyCalc(k):
    """HeavyCalc(int k) int"""
    cret = _cffi_helper.lib.cgo_func_trygopy_HeavyCalc(k)
    return cret

