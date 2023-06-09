# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_partio', [dirname(__file__)])
        except ImportError:
            import _partio
            return _partio
        if fp is not None:
            try:
                _mod = imp.load_module('_partio', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _partio = swig_import_helper()
    del swig_import_helper
else:
    import _partio
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _partio.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _partio.SwigPyIterator_value(self)
    def incr(self, n=1): return _partio.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _partio.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _partio.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _partio.SwigPyIterator_equal(self, *args)
    def copy(self): return _partio.SwigPyIterator_copy(self)
    def next(self): return _partio.SwigPyIterator_next(self)
    def __next__(self): return _partio.SwigPyIterator___next__(self)
    def previous(self): return _partio.SwigPyIterator_previous(self)
    def advance(self, *args): return _partio.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _partio.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _partio.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _partio.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _partio.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _partio.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _partio.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _partio.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

NONE = _partio.NONE
VECTOR = _partio.VECTOR
FLOAT = _partio.FLOAT
INT = _partio.INT
INDEXEDSTR = _partio.INDEXEDSTR
class ParticleAttribute(_object):
    """A handle for operating on attribbutes of a particle set"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParticleAttribute, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ParticleAttribute, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _partio.ParticleAttribute_type_set
    __swig_getmethods__["type"] = _partio.ParticleAttribute_type_get
    if _newclass:type = _swig_property(_partio.ParticleAttribute_type_get, _partio.ParticleAttribute_type_set)
    __swig_setmethods__["count"] = _partio.ParticleAttribute_count_set
    __swig_getmethods__["count"] = _partio.ParticleAttribute_count_get
    if _newclass:count = _swig_property(_partio.ParticleAttribute_count_get, _partio.ParticleAttribute_count_set)
    __swig_setmethods__["name"] = _partio.ParticleAttribute_name_set
    __swig_getmethods__["name"] = _partio.ParticleAttribute_name_get
    if _newclass:name = _swig_property(_partio.ParticleAttribute_name_get, _partio.ParticleAttribute_name_set)
    def __init__(self): 
        """
        __init__(ParticleAttribute self) -> ParticleAttribute

        Attribute name
        """
        this = _partio.new_ParticleAttribute()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _partio.delete_ParticleAttribute
    __del__ = lambda self : None;
ParticleAttribute_swigregister = _partio.ParticleAttribute_swigregister
ParticleAttribute_swigregister(ParticleAttribute)

class FixedAttribute(_object):
    """A handle for operating on fixed attribbutes of a particle set"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FixedAttribute, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FixedAttribute, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _partio.FixedAttribute_type_set
    __swig_getmethods__["type"] = _partio.FixedAttribute_type_get
    if _newclass:type = _swig_property(_partio.FixedAttribute_type_get, _partio.FixedAttribute_type_set)
    __swig_setmethods__["count"] = _partio.FixedAttribute_count_set
    __swig_getmethods__["count"] = _partio.FixedAttribute_count_get
    if _newclass:count = _swig_property(_partio.FixedAttribute_count_get, _partio.FixedAttribute_count_set)
    __swig_setmethods__["name"] = _partio.FixedAttribute_name_set
    __swig_getmethods__["name"] = _partio.FixedAttribute_name_get
    if _newclass:name = _swig_property(_partio.FixedAttribute_name_get, _partio.FixedAttribute_name_set)
    def __init__(self): 
        """
        __init__(FixedAttribute self) -> FixedAttribute

        Attribute name
        """
        this = _partio.new_FixedAttribute()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _partio.delete_FixedAttribute
    __del__ = lambda self : None;
FixedAttribute_swigregister = _partio.FixedAttribute_swigregister
FixedAttribute_swigregister(FixedAttribute)

class ParticlesInfo(_object):
    """A set of particles with associated data attributes."""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParticlesInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ParticlesInfo, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def numParticles(self):
        """
        numParticles(ParticlesInfo self) -> int

        Returns the number of particles in the set
        """
        return _partio.ParticlesInfo_numParticles(self)

    def numAttributes(self):
        """
        numAttributes(ParticlesInfo self) -> int

        Returns the number of particles in the set
        """
        return _partio.ParticlesInfo_numAttributes(self)

    def numFixedAttributes(self):
        """
        numFixedAttributes(ParticlesInfo self) -> int

        Returns the number of fixed attributes
        """
        return _partio.ParticlesInfo_numFixedAttributes(self)

    def attributeInfo(self, *args):
        """
        attributeInfo(ParticlesInfo self, char const * name) -> ParticleAttribute
        attributeInfo(ParticlesInfo self, int const index) -> ParticleAttribute

        Returns the attribute handle by index
        """
        return _partio.ParticlesInfo_attributeInfo(self, *args)

    def fixedAttributeInfo(self, *args):
        """
        fixedAttributeInfo(ParticlesInfo self, char const * name) -> FixedAttribute
        fixedAttributeInfo(ParticlesInfo self, int const index) -> FixedAttribute

        Returns the fixed attribute handle by index
        """
        return _partio.ParticlesInfo_fixedAttributeInfo(self, *args)

    __swig_destroy__ = _partio.delete_ParticlesInfo
    __del__ = lambda self : None;
ParticlesInfo_swigregister = _partio.ParticlesInfo_swigregister
ParticlesInfo_swigregister(ParticlesInfo)

class ParticlesData(ParticlesInfo):
    """A reader for a set of particles."""
    __swig_setmethods__ = {}
    for _s in [ParticlesInfo]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParticlesData, name, value)
    __swig_getmethods__ = {}
    for _s in [ParticlesInfo]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParticlesData, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def lookupIndexedStr(self, *args):
        """
        lookupIndexedStr(ParticlesData self, ParticleAttribute attribute, char const * str) -> int

        Looks up a given indexed string given the index, returns -1 if not found
        """
        return _partio.ParticlesData_lookupIndexedStr(self, *args)

    def lookupFixedIndexedStr(self, *args):
        """
        lookupFixedIndexedStr(ParticlesData self, FixedAttribute attribute, char const * str) -> int

        Looks up a given fixed indexed string given the index, returns -1 if not found
        """
        return _partio.ParticlesData_lookupFixedIndexedStr(self, *args)

    def findNPoints(self, *args):
        """
        findNPoints(ParticlesData self, fixedFloatArray center, int nPoints, float maxRadius) -> PyObject *

        Searches for the N nearest points to the center location
        or as many as can be found within maxRadius distance.
        """
        return _partio.ParticlesData_findNPoints(self, *args)

    def findPoints(self, *args):
        """
        findPoints(ParticlesData self, fixedFloatArray bboxMin, fixedFloatArray bboxMax) -> PyObject *

        Returns the indices of all points within the bounding
        box defined by the two cube corners bboxMin and bboxMax
        """
        return _partio.ParticlesData_findPoints(self, *args)

    def get(self, *args):
        """
        get(ParticlesData self, ParticleAttribute attr, ParticleIndex const particleIndex) -> PyObject *

        Gets attribute data for particleIndex'th particle
        """
        return _partio.ParticlesData_get(self, *args)

    def getFixed(self, *args):
        """
        getFixed(ParticlesData self, FixedAttribute attr) -> PyObject *

        Gets fixed attribute data
        """
        return _partio.ParticlesData_getFixed(self, *args)

    def indexedStrs(self, *args):
        """
        indexedStrs(ParticlesData self, ParticleAttribute attr) -> PyObject *

        Gets a list of all indexed strings for the given attribute handle
        """
        return _partio.ParticlesData_indexedStrs(self, *args)

    def fixedIndexedStrs(self, *args):
        """
        fixedIndexedStrs(ParticlesData self, FixedAttribute attr) -> PyObject *

        Gets a list of all indexed strings for the given fixed attribute handle
        """
        return _partio.ParticlesData_fixedIndexedStrs(self, *args)

    __swig_destroy__ = _partio.delete_ParticlesData
    __del__ = lambda self : None;
ParticlesData_swigregister = _partio.ParticlesData_swigregister
ParticlesData_swigregister(ParticlesData)

class ParticleIteratorTrue(_object):
    """A reader for a set of particles."""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParticleIteratorTrue, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ParticleIteratorTrue, name)
    __repr__ = _swig_repr
    def __init__(self): 
        """
        __init__(ParticleIterator<(true)> self) -> ParticleIteratorTrue

        Return string name of given attribute type
        """
        this = _partio.new_ParticleIteratorTrue()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _partio.delete_ParticleIteratorTrue
    __del__ = lambda self : None;
ParticleIteratorTrue_swigregister = _partio.ParticleIteratorTrue_swigregister
ParticleIteratorTrue_swigregister(ParticleIteratorTrue)

class ParticleIteratorFalse(_object):
    """A reader for a set of particles."""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParticleIteratorFalse, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ParticleIteratorFalse, name)
    __repr__ = _swig_repr
    def __init__(self): 
        """
        __init__(ParticleIterator<(false)> self) -> ParticleIteratorFalse

        Return string name of given attribute type
        """
        this = _partio.new_ParticleIteratorFalse()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _partio.delete_ParticleIteratorFalse
    __del__ = lambda self : None;
ParticleIteratorFalse_swigregister = _partio.ParticleIteratorFalse_swigregister
ParticleIteratorFalse_swigregister(ParticleIteratorFalse)

class ParticlesDataMutable(ParticlesData):
    """A writer for a set of particles."""
    __swig_setmethods__ = {}
    for _s in [ParticlesData]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParticlesDataMutable, name, value)
    __swig_getmethods__ = {}
    for _s in [ParticlesData]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParticlesDataMutable, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    def registerIndexedStr(self, *args):
        """
        registerIndexedStr(ParticlesDataMutable self, ParticleAttribute attribute, char const * str) -> int

        Registers a string in the particular attribute
        """
        return _partio.ParticlesDataMutable_registerIndexedStr(self, *args)

    def registerFixedIndexedStr(self, *args):
        """
        registerFixedIndexedStr(ParticlesDataMutable self, FixedAttribute attribute, char const * str) -> int

        Registers a string in the particular fixed attribute
        """
        return _partio.ParticlesDataMutable_registerFixedIndexedStr(self, *args)

    def setIndexedStr(self, *args):
        """
        setIndexedStr(ParticlesDataMutable self, ParticleAttribute attribute, int particleAttributeHandle, char const * str)

        Changes a given index's associated string (for all particles that use this index too)
        """
        return _partio.ParticlesDataMutable_setIndexedStr(self, *args)

    def setFixedIndexedStr(self, *args):
        """
        setFixedIndexedStr(ParticlesDataMutable self, FixedAttribute attribute, int particleAttributeHandle, char const * str)

        Changes a given fixed index's associated string
        """
        return _partio.ParticlesDataMutable_setFixedIndexedStr(self, *args)

    def sort(self):
        """
        sort(ParticlesDataMutable self)

        Prepares data for N nearest neighbor searches using the
        attribute in the file with name 'position'
        """
        return _partio.ParticlesDataMutable_sort(self)

    def addAttribute(self, *args):
        """
        addAttribute(ParticlesDataMutable self, char const * attribute, ParticleAttributeType type, int const count) -> ParticleAttribute

        Adds a new attribute of given name, type and count. If type is
        partio.VECTOR, then count must be 3
        """
        return _partio.ParticlesDataMutable_addAttribute(self, *args)

    def addFixedAttribute(self, *args):
        """
        addFixedAttribute(ParticlesDataMutable self, char const * attribute, ParticleAttributeType type, int const count) -> FixedAttribute

        Adds a new fixed attribute of given name, type and count. If type is
        partio.VECTOR, then count must be 3
        """
        return _partio.ParticlesDataMutable_addFixedAttribute(self, *args)

    def addParticle(self):
        """
        addParticle(ParticlesDataMutable self) -> ParticleIndex

        Adds a new particle and returns the index
        """
        return _partio.ParticlesDataMutable_addParticle(self)

    def addParticles(self, *args):
        """
        addParticles(ParticlesDataMutable self, int const count) -> ParticleIteratorFalse

        Adds count particles and returns the offset to the first one
        """
        return _partio.ParticlesDataMutable_addParticles(self, *args)

    def set(self, *args):
        """
        set(ParticlesDataMutable self, ParticleAttribute attr, uint64_t const particleIndex, PyObject * tuple) -> PyObject *

        Sets data on a given attribute for a single particle.
        Data must be specified as tuple.
        """
        return _partio.ParticlesDataMutable_set(self, *args)

    def setFixed(self, *args):
        """
        setFixed(ParticlesDataMutable self, FixedAttribute attr, PyObject * tuple) -> PyObject *

        Sets data on a given fixed attribute.
        Data must be specified as tuple.
        """
        return _partio.ParticlesDataMutable_setFixed(self, *args)

    def ptr(self):
        """
        ptr(ParticlesDataMutable self) -> unsigned long

        Workaround to get the address to the ptr to help with interop python binding
        """
        return _partio.ParticlesDataMutable_ptr(self)

    __swig_destroy__ = _partio.delete_ParticlesDataMutable
    __del__ = lambda self : None;
ParticlesDataMutable_swigregister = _partio.ParticlesDataMutable_swigregister
ParticlesDataMutable_swigregister(ParticlesDataMutable)


def create():
  """
    create() -> ParticlesDataMutable

    Create an empty particle array
    """
  return _partio.create()

def read(*args):
  """
    read(char const * filename, bool verbose=True, std::ostream & error=std::cerr) -> ParticlesDataMutable
    read(char const * filename, bool verbose=True) -> ParticlesDataMutable
    read(char const * filename) -> ParticlesDataMutable

    Reads a particle set from disk
    """
  return _partio.read(*args)

def readVerbose(*args):
  """
    readVerbose(char const * filename) -> PyObject *

    Reads a particle set from disk and returns the tuple particleObject,errorMsg
    """
  return _partio.readVerbose(*args)

def readHeadersVerbose(*args):
  """
    readHeadersVerbose(char const * filename) -> PyObject *

    Reads the header/attribute information from disk and returns the tuple particleObject,errorMsg
    """
  return _partio.readHeadersVerbose(*args)

def readCachedVerbose(*args):
  """
    readCachedVerbose(char const * filename, bool sort) -> PyObject *

    Reads the header/attribute information from disk and returns the tuple particleObject,errorMsg
    """
  return _partio.readCachedVerbose(*args)

def readHeaders(*args):
  """
    readHeaders(char const * filename, bool verbose=True, std::ostream & error=std::cerr) -> ParticlesInfo
    readHeaders(char const * filename, bool verbose=True) -> ParticlesInfo
    readHeaders(char const * filename) -> ParticlesInfo

    Reads a particle set headers from disk
    """
  return _partio.readHeaders(*args)

def write(*args):
  """
    write(char const * filename, ParticlesData arg2, bool const arg3=False, bool const arg4=True)
    write(char const * filename, ParticlesData arg2, bool const arg3=False)
    write(char const * filename, ParticlesData arg2)

    Writes a particle set to disk
    """
  return _partio.write(*args)

def _print(*args):
  """
    _print(ParticlesData particles)

    Print a summary of particle file
    """
  return _partio._print(*args)

def computeClustering(*args):
  """
    computeClustering(ParticlesDataMutable particles, int const numNeighbors, double const radiusSearch, 
        double const radiusInside, int const connections, double const density) -> ParticlesDataMutable

    Creates a clustered particle set
    """
  return _partio.computeClustering(*args)

def merge(*args):
  """
    merge(ParticlesDataMutable base, ParticlesData delta, std::string const & identifier=std::string())
    merge(ParticlesDataMutable base, ParticlesData delta)

    Merge two particle sets
    """
  return _partio.merge(*args)
class attrNameMap(_object):
    """Merge two particle sets"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, attrNameMap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, attrNameMap, name)
    __repr__ = _swig_repr
    def iterator(self):
        """
        iterator(attrNameMap self) -> SwigPyIterator

        Merge two particle sets
        """
        return _partio.attrNameMap_iterator(self)

    def __iter__(self): return self.iterator()
    def __nonzero__(self):
        """
        __nonzero__(attrNameMap self) -> bool

        Merge two particle sets
        """
        return _partio.attrNameMap___nonzero__(self)

    def __bool__(self):
        """
        __bool__(attrNameMap self) -> bool

        Merge two particle sets
        """
        return _partio.attrNameMap___bool__(self)

    def __len__(self):
        """
        __len__(attrNameMap self) -> std::map< std::string,std::string >::size_type

        Merge two particle sets
        """
        return _partio.attrNameMap___len__(self)

    def __iter__(self): return self.key_iterator()
    def iterkeys(self): return self.key_iterator()
    def itervalues(self): return self.value_iterator()
    def iteritems(self): return self.iterator()
    def __getitem__(self, *args):
        """
        __getitem__(attrNameMap self, std::map< std::string,std::string >::key_type const & key) -> std::map< std::string,std::string >::mapped_type const &

        Merge two particle sets
        """
        return _partio.attrNameMap___getitem__(self, *args)

    def __delitem__(self, *args):
        """
        __delitem__(attrNameMap self, std::map< std::string,std::string >::key_type const & key)

        Merge two particle sets
        """
        return _partio.attrNameMap___delitem__(self, *args)

    def has_key(self, *args):
        """
        has_key(attrNameMap self, std::map< std::string,std::string >::key_type const & key) -> bool

        Merge two particle sets
        """
        return _partio.attrNameMap_has_key(self, *args)

    def keys(self):
        """
        keys(attrNameMap self) -> PyObject *

        Merge two particle sets
        """
        return _partio.attrNameMap_keys(self)

    def values(self):
        """
        values(attrNameMap self) -> PyObject *

        Merge two particle sets
        """
        return _partio.attrNameMap_values(self)

    def items(self):
        """
        items(attrNameMap self) -> PyObject *

        Merge two particle sets
        """
        return _partio.attrNameMap_items(self)

    def __contains__(self, *args):
        """
        __contains__(attrNameMap self, std::map< std::string,std::string >::key_type const & key) -> bool

        Merge two particle sets
        """
        return _partio.attrNameMap___contains__(self, *args)

    def key_iterator(self):
        """
        key_iterator(attrNameMap self) -> SwigPyIterator

        Merge two particle sets
        """
        return _partio.attrNameMap_key_iterator(self)

    def value_iterator(self):
        """
        value_iterator(attrNameMap self) -> SwigPyIterator

        Merge two particle sets
        """
        return _partio.attrNameMap_value_iterator(self)

    def __setitem__(self, *args):
        """
        __setitem__(attrNameMap self, std::map< std::string,std::string >::key_type const & key)
        __setitem__(attrNameMap self, std::map< std::string,std::string >::key_type const & key, std::map< std::string,std::string >::mapped_type const & x)

        Merge two particle sets
        """
        return _partio.attrNameMap___setitem__(self, *args)

    def asdict(self):
        """
        asdict(attrNameMap self) -> PyObject *

        Merge two particle sets
        """
        return _partio.attrNameMap_asdict(self)

    def __init__(self, *args): 
        """
        __init__(std::map<(std::string,std::string)> self, std::less< std::string > const & arg2) -> attrNameMap
        __init__(std::map<(std::string,std::string)> self) -> attrNameMap
        __init__(std::map<(std::string,std::string)> self, attrNameMap arg2) -> attrNameMap

        Merge two particle sets
        """
        this = _partio.new_attrNameMap(*args)
        try: self.this.append(this)
        except: self.this = this
    def empty(self):
        """
        empty(attrNameMap self) -> bool

        Merge two particle sets
        """
        return _partio.attrNameMap_empty(self)

    def size(self):
        """
        size(attrNameMap self) -> std::map< std::string,std::string >::size_type

        Merge two particle sets
        """
        return _partio.attrNameMap_size(self)

    def clear(self):
        """
        clear(attrNameMap self)

        Merge two particle sets
        """
        return _partio.attrNameMap_clear(self)

    def swap(self, *args):
        """
        swap(attrNameMap self, attrNameMap v)

        Merge two particle sets
        """
        return _partio.attrNameMap_swap(self, *args)

    def get_allocator(self):
        """
        get_allocator(attrNameMap self) -> std::map< std::string,std::string >::allocator_type

        Merge two particle sets
        """
        return _partio.attrNameMap_get_allocator(self)

    def begin(self):
        """
        begin(attrNameMap self) -> std::map< std::string,std::string >::iterator

        Merge two particle sets
        """
        return _partio.attrNameMap_begin(self)

    def end(self):
        """
        end(attrNameMap self) -> std::map< std::string,std::string >::iterator

        Merge two particle sets
        """
        return _partio.attrNameMap_end(self)

    def rbegin(self):
        """
        rbegin(attrNameMap self) -> std::map< std::string,std::string >::reverse_iterator

        Merge two particle sets
        """
        return _partio.attrNameMap_rbegin(self)

    def rend(self):
        """
        rend(attrNameMap self) -> std::map< std::string,std::string >::reverse_iterator

        Merge two particle sets
        """
        return _partio.attrNameMap_rend(self)

    def count(self, *args):
        """
        count(attrNameMap self, std::map< std::string,std::string >::key_type const & x) -> std::map< std::string,std::string >::size_type

        Merge two particle sets
        """
        return _partio.attrNameMap_count(self, *args)

    def erase(self, *args):
        """
        erase(attrNameMap self, std::map< std::string,std::string >::key_type const & x) -> std::map< std::string,std::string >::size_type
        erase(attrNameMap self, std::map< std::string,std::string >::iterator position)
        erase(attrNameMap self, std::map< std::string,std::string >::iterator first, std::map< std::string,std::string >::iterator last)

        Merge two particle sets
        """
        return _partio.attrNameMap_erase(self, *args)

    def find(self, *args):
        """
        find(attrNameMap self, std::map< std::string,std::string >::key_type const & x) -> std::map< std::string,std::string >::iterator

        Merge two particle sets
        """
        return _partio.attrNameMap_find(self, *args)

    def lower_bound(self, *args):
        """
        lower_bound(attrNameMap self, std::map< std::string,std::string >::key_type const & x) -> std::map< std::string,std::string >::iterator

        Merge two particle sets
        """
        return _partio.attrNameMap_lower_bound(self, *args)

    def upper_bound(self, *args):
        """
        upper_bound(attrNameMap self, std::map< std::string,std::string >::key_type const & x) -> std::map< std::string,std::string >::iterator

        Merge two particle sets
        """
        return _partio.attrNameMap_upper_bound(self, *args)

    __swig_destroy__ = _partio.delete_attrNameMap
    __del__ = lambda self : None;
attrNameMap_swigregister = _partio.attrNameMap_swigregister
attrNameMap_swigregister(attrNameMap)


def cloneSchema(*args):
  """
    cloneSchema(ParticlesData other, attrNameMap attrNameMap=nullptr) -> ParticlesDataMutable
    cloneSchema(ParticlesData other) -> ParticlesDataMutable

    Clone a particle set's attribute schema
    """
  return _partio.cloneSchema(*args)

def clone(*args):
  """
    clone(ParticlesData other, bool particles, attrNameMap attrNameMap=nullptr) -> ParticlesDataMutable
    clone(ParticlesData other, bool particles) -> ParticlesDataMutable

    Clone a particle set
    """
  return _partio.clone(*args)

def TypeName(*args):
  """
    TypeName(ParticleAttributeType attrType) -> std::string

    Return string name of given attribute type
    """
  return _partio.TypeName(*args)
# This file is compatible with both classic and new-style classes.


