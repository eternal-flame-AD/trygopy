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

// C definitions for Go type trygopy.trygopy_GoMessage.
// C definitions for Go type trygopy.0x552445933.
typedef void* cgo_type_0x552445933;
extern void* cgo_func_0x552445933_new();
extern void cgo_func_0x552445933_ass_item(void* p0, GoInt p1, GoString p2);
extern void cgo_func_0x552445933_append(void* p0, GoString p1);
extern GoString cgo_func_0x552445933_item(void* p0, GoString p1);
extern GoString cgo_func_0x552445933_str(cgo_type_0x552445933 p0);

// C definitions for Go type trygopy.trygopy_GoMessage.
// A type definition of the trygopy.cgo_type_trygopy_GoMessage for wrapping.
typedef void* cgo_type_trygopy_GoMessage;
extern void* cgo_func_trygopy_GoMessage_new();
extern cgo_type_trygopy_GoMessage cgo_func_trygopy_EchoGoMessage(cgo_type_trygopy_GoMessage p0);
extern GoInt cgo_func_trygopy_GoMessage_getter_1(void* p0);
extern void cgo_func_trygopy_GoMessage_setter_1(void* p0, GoInt p1);
extern GoString cgo_func_trygopy_GoMessage_getter_2(void* p0);
extern void cgo_func_trygopy_GoMessage_setter_2(void* p0, GoString p1);
extern GoFloat64 cgo_func_trygopy_GoMessage_getter_3(void* p0);
extern void cgo_func_trygopy_GoMessage_setter_3(void* p0, GoFloat64 p1);
extern GoString cgo_func_trygopy_GoMessage_str(void* p0);
extern GoString cgo_func_trygopy_GoPyStringSliceHelper(cgo_type_0x552445933 p0, GoInt p1);
extern GoInt cgo_func_trygopy_HeavyCalc(GoInt p0);
extern cgo_type_0x552445933 cgo_func_trygopy_BatchEcho(cgo_type_0x552445933 p0);
extern GoString cgo_func_trygopy_Echo(GoString p0);
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

    # converters for trygopy_GoMessage - GoMessage
    @staticmethod
    def cffi_cgopy_cnv_py2c_trygopy_GoMessage(o):
        if type(o) is GoMessage:
            return o.cgopy
    
    @staticmethod
    def cffi_cgopy_cnv_c2py_trygopy_GoMessage(c):
        o = GoMessage()
        o.cgopy = c
        return o
    
    # converters for 0x552445933 - []string
    @staticmethod
    def cffi_cgopy_cnv_py2c_0x552445933(o):
        if type(o) is cgo_type_0x552445933:
            return o.cgopy
        if not isinstance(o, collections.Iterable):
            raise TypeError('[]string.__init__ takes a sequence as argument')
        c = _cffi_helper.lib.cgo_func_0x552445933_new()
        for elt in o:
            pyitem = _cffi_helper.cffi_cgopy_cnv_py2c_string(elt)
            _cffi_helper.lib.cgo_func_0x552445933_append(c, pyitem)
        return c
    
    @staticmethod
    def cffi_cgopy_cnv_c2py_0x552445933(c):
        o = cgo_type_0x552445933()
        o.cgopy = c
        return o
    
    # converters for trygopy_GoMessage - GoMessage
    @staticmethod
    def cffi_cgopy_cnv_py2c_trygopy_GoMessage(o):
        if type(o) is GoMessage:
            return o.cgopy
    
    @staticmethod
    def cffi_cgopy_cnv_c2py_trygopy_GoMessage(c):
        o = GoMessage()
        o.cgopy = c
        return o
    
    @staticmethod
    def cffi_cgopy_cnv_py2c_trygopy_GoMessage(o):
        return o.cgopy
        
    @staticmethod
    def cffi_cgopy_cnv_c2py_trygopy_GoMessage(c):
        o = GoMessage()
        o.cgopy = ffi.gc(c, _cffi_helper.lib.cgopy_decref)
        return o
        
# make sure Cgo is loaded and initialized
_cffi_helper.lib.cgo_pkg_trygopy_init()

# Python type for trygopy.cgo_type_0x552445933
class cgo_type_0x552445933(object):
    """"""
    def __init__(self, *args, **kwargs):
        nkwds = len(kwargs)
        nargs = len(args)
        if nkwds + nargs > 1:
            raise TypeError('[]string.__init__ takes at most 1 argument(s)')
        self.cgopy = _cffi_helper.lib.cgo_func_0x552445933_new()
        if args:
            if not isinstance(args[0], collections.Iterable):
                raise TypeError('[]string.__init__ takes a sequence as argument')
            for elt in args[0]:
                pyitem = _cffi_helper.cffi_cgopy_cnv_py2c_string(elt)
                _cffi_helper.lib.cgo_func_0x552445933_append(self.cgopy, pyitem)
    
    # methods for []string
    
    def __repr__(self):
        cret = _cffi_helper.lib.cgo_func_0x552445933_str(self.cgopy)
        ret = _cffi_helper.cffi_cgopy_cnv_c2py_string(cret)
        return ret
    
    def __str__(self):
        cret = _cffi_helper.lib.cgo_func_0x552445933_str(self.cgopy)
        ret = _cffi_helper.cffi_cgopy_cnv_c2py_string(cret)
        return ret
    
    def __len__(self):
        return ffi.cast('GoSlice*', self.cgopy).len
    
    def __getitem__(self, idx):
        if idx >= len(self):
            raise IndexError('slice index out of range')
        item = _cffi_helper.lib.cgo_func_0x552445933_item(self.cgopy, idx)
        pyitem = _cffi_helper.cffi_cgopy_cnv_c2py_string(item)
        return pyitem
    
    def __setitem__(self, idx, item):
        if idx >= len(self):
            raise IndexError('slice index out of range')
        pyitem = _cffi_helper.cffi_cgopy_cnv_py2c_string(item)
        _cffi_helper.lib.cgo_func_0x552445933_ass_item(self.cgopy, idx, pyitem)
    
    def __iadd__(self, value):
        if not isinstance(value, collections.Iterable):
            raise TypeError('[]string.__iadd__ takes a iterable type as argument')
        for elt in value:
            pyitem = _cffi_helper.cffi_cgopy_cnv_py2c_string(elt)
            _cffi_helper.lib.cgo_func_0x552445933_append(self.cgopy, pyitem)
        return self
    

# Python type for struct trygopy.GoMessage
class GoMessage(object):
    """"""
    def __init__(self, *args, **kwargs):
        nkwds = len(kwargs)
        nargs = len(args)
        if nkwds + nargs > 3:
            raise TypeError('GoMessage.__init__ takes at most 3 argument(s)')
        cgopy = _cffi_helper.lib.cgo_func_trygopy_GoMessage_new()
        if cgopy == ffi.NULL:
            raise MemoryError('gopy: could not allocate GoMessage.')
        self.cgopy = ffi.gc(cgopy, _cffi_helper.lib.cgopy_decref)
        
        py_kwd_001 = None
        if  0 < nargs:
            py_kwd_001 = args[0]
        if "Number" in kwargs:
            py_kwd_001 = kwargs["Number"]
        if py_kwd_001 != None:
            if not isinstance(py_kwd_001, int):
                raise TypeError("invalid type for 'Number' attribute")
            _cffi_helper.lib.cgo_func_trygopy_GoMessage_setter_1(self.cgopy, py_kwd_001)
        py_kwd_002 = None
        if  1 < nargs:
            py_kwd_002 = args[1]
        if "String" in kwargs:
            py_kwd_002 = kwargs["String"]
        if py_kwd_002 != None:
            if not isinstance(py_kwd_002, str):
                raise TypeError("invalid type for 'String' attribute")
            c_kwd_002 = _cffi_helper.cffi_cgopy_cnv_py2c_string(py_kwd_002)
            _cffi_helper.lib.cgo_func_trygopy_GoMessage_setter_2(self.cgopy, c_kwd_002)
        py_kwd_003 = None
        if  2 < nargs:
            py_kwd_003 = args[2]
        if "Decimal" in kwargs:
            py_kwd_003 = kwargs["Decimal"]
        if py_kwd_003 != None:
            if not isinstance(py_kwd_003, float):
                raise TypeError("invalid type for 'Decimal' attribute")
            _cffi_helper.lib.cgo_func_trygopy_GoMessage_setter_3(self.cgopy, py_kwd_003)
    
    @property
    def Number(self):
        cret =  _cffi_helper.lib.cgo_func_trygopy_GoMessage_getter_1(self.cgopy)
        return cret
        
    @Number.setter
    def Number(self, value):
        _cffi_helper.lib.cgo_func_trygopy_GoMessage_setter_1(self.cgopy, value)
        
    @property
    def String(self):
        cret =  _cffi_helper.lib.cgo_func_trygopy_GoMessage_getter_2(self.cgopy)
        ret = _cffi_helper.cffi_cgopy_cnv_c2py_string(cret)
        return ret
        
    @String.setter
    def String(self, value):
        c_value = _cffi_helper.cffi_cgopy_cnv_py2c_string(value)
        _cffi_helper.lib.cgo_func_trygopy_GoMessage_setter_2(self.cgopy, c_value)
        
    @property
    def Decimal(self):
        cret =  _cffi_helper.lib.cgo_func_trygopy_GoMessage_getter_3(self.cgopy)
        return cret
        
    @Decimal.setter
    def Decimal(self, value):
        _cffi_helper.lib.cgo_func_trygopy_GoMessage_setter_3(self.cgopy, value)
        
    def __repr__(self):
        cret = _cffi_helper.lib.cgo_func_trygopy_GoMessage_str(self.cgopy)
        ret = _cffi_helper.cffi_cgopy_cnv_c2py_string(cret)
        return ret
        
    def __str__(self):
        cret = _cffi_helper.lib.cgo_func_trygopy_GoMessage_str(self.cgopy)
        ret = _cffi_helper.cffi_cgopy_cnv_c2py_string(cret)
        return ret
        

# pythonization of: trygopy.EchoGoMessage 
def EchoGoMessage(s):
    """EchoGoMessage(object s) object"""
    c_s = _cffi_helper.cffi_cgopy_cnv_py2c_trygopy_GoMessage(s)
    cret = _cffi_helper.lib.cgo_func_trygopy_EchoGoMessage(c_s)
    ret = _cffi_helper.cffi_cgopy_cnv_c2py_trygopy_GoMessage(cret)
    return ret


# pythonization of: trygopy.GoPyStringSliceHelper 
def GoPyStringSliceHelper(s, i):
    """GoPyStringSliceHelper([]str s, int i) str"""
    c_s = _cffi_helper.cffi_cgopy_cnv_py2c_0x552445933(s)
    cret = _cffi_helper.lib.cgo_func_trygopy_GoPyStringSliceHelper(c_s, i)
    ret = _cffi_helper.cffi_cgopy_cnv_c2py_string(cret)
    return ret


# pythonization of: trygopy.HeavyCalc 
def HeavyCalc(k):
    """HeavyCalc(int k) int"""
    cret = _cffi_helper.lib.cgo_func_trygopy_HeavyCalc(k)
    return cret


# pythonization of: trygopy.BatchEcho 
def BatchEcho(s):
    """BatchEcho([]str s) []str"""
    c_s = _cffi_helper.cffi_cgopy_cnv_py2c_0x552445933(s)
    cret = _cffi_helper.lib.cgo_func_trygopy_BatchEcho(c_s)
    ret = _cffi_helper.cffi_cgopy_cnv_c2py_0x552445933(cret)
    return ret


# pythonization of: trygopy.Echo 
def Echo(s):
    """Echo(str s) str"""
    c_s = _cffi_helper.cffi_cgopy_cnv_py2c_string(s)
    cret = _cffi_helper.lib.cgo_func_trygopy_Echo(c_s)
    ret = _cffi_helper.cffi_cgopy_cnv_c2py_string(cret)
    return ret

