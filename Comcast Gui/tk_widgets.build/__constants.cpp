
#include "nuitka/prelude.hpp"

// Sentinel PyObject to be used for all our call iterator endings. It will
// become a PyCObject pointing to NULL. It's address is unique, and that's
// enough for us to use it as sentinel value.
PyObject *_sentinel_value = NULL;

PyObject *const_dict_empty;
PyObject *const_int_0;
PyObject *const_int_pos_1;
PyObject *const_str_empty;
PyObject *const_str_plain___all__;
PyObject *const_str_plain___builtins__;
PyObject *const_str_plain___class__;
PyObject *const_str_plain___cmp__;
PyObject *const_str_plain___delattr__;
PyObject *const_str_plain___dict__;
PyObject *const_str_plain___doc__;
PyObject *const_str_plain___enter__;
PyObject *const_str_plain___exit__;
PyObject *const_str_plain___file__;
PyObject *const_str_plain___getattr__;
PyObject *const_str_plain___import__;
PyObject *const_str_plain___main__;
PyObject *const_str_plain___metaclass__;
PyObject *const_str_plain___module__;
PyObject *const_str_plain___name__;
PyObject *const_str_plain___setattr__;
PyObject *const_str_plain_compile;
PyObject *const_str_plain_exc_traceback;
PyObject *const_str_plain_exc_type;
PyObject *const_str_plain_exc_value;
PyObject *const_str_plain_inspect;
PyObject *const_str_plain_int;
PyObject *const_str_plain_iter;
PyObject *const_str_plain_len;
PyObject *const_str_plain_long;
PyObject *const_str_plain_open;
PyObject *const_str_plain_range;
PyObject *const_str_plain_repr;
PyObject *const_str_plain_site;
PyObject *const_str_plain_type;
PyObject *const_str_plain_xrange;
PyObject *const_tuple_empty;

#if defined(_WIN32) && defined(_NUITKA_EXE)
#include <Windows.h>
const unsigned char* constant_bin;
struct __initResourceConstants
{
    __initResourceConstants()
    {
        constant_bin = (const unsigned char*)LockResource(
            LoadResource(
                NULL,
                FindResource(NULL, MAKEINTRESOURCE(3), RT_RCDATA)
            )
        );
    }
} __initResourceConstants_static_initializer;
#else
extern "C" const unsigned char constant_bin[];
#endif

static void __initConstants( void )
{
    NUITKA_MAY_BE_UNUSED PyObject *exception_type, *exception_value;
    NUITKA_MAY_BE_UNUSED PyTracebackObject *exception_tb;

#ifdef _MSC_VER
    // Prevent unused warnings in case of simple programs.
    (void *)exception_type; (void *)exception_value; (void *)exception_tb;
#endif

    const_dict_empty = _PyDict_NewPresized( 0 );
    const_int_0 = PyInt_FromLong( 0l );
    const_int_pos_1 = PyInt_FromLong( 1l );
    const_str_empty = UNSTREAM_STRING( &constant_bin[ 0 ], 0, 0 );
    const_str_plain___all__ = UNSTREAM_STRING( &constant_bin[ 463 ], 7, 1 );
    const_str_plain___builtins__ = UNSTREAM_STRING( &constant_bin[ 470 ], 12, 1 );
    const_str_plain___class__ = UNSTREAM_STRING( &constant_bin[ 482 ], 9, 1 );
    const_str_plain___cmp__ = UNSTREAM_STRING( &constant_bin[ 491 ], 7, 1 );
    const_str_plain___delattr__ = UNSTREAM_STRING( &constant_bin[ 498 ], 11, 1 );
    const_str_plain___dict__ = UNSTREAM_STRING( &constant_bin[ 509 ], 8, 1 );
    const_str_plain___doc__ = UNSTREAM_STRING( &constant_bin[ 517 ], 7, 1 );
    const_str_plain___enter__ = UNSTREAM_STRING( &constant_bin[ 524 ], 9, 1 );
    const_str_plain___exit__ = UNSTREAM_STRING( &constant_bin[ 533 ], 8, 1 );
    const_str_plain___file__ = UNSTREAM_STRING( &constant_bin[ 541 ], 8, 1 );
    const_str_plain___getattr__ = UNSTREAM_STRING( &constant_bin[ 549 ], 11, 1 );
    const_str_plain___import__ = UNSTREAM_STRING( &constant_bin[ 560 ], 10, 1 );
    const_str_plain___main__ = UNSTREAM_STRING( &constant_bin[ 570 ], 8, 1 );
    const_str_plain___metaclass__ = UNSTREAM_STRING( &constant_bin[ 578 ], 13, 1 );
    const_str_plain___module__ = UNSTREAM_STRING( &constant_bin[ 591 ], 10, 1 );
    const_str_plain___name__ = UNSTREAM_STRING( &constant_bin[ 601 ], 8, 1 );
    const_str_plain___setattr__ = UNSTREAM_STRING( &constant_bin[ 609 ], 11, 1 );
    const_str_plain_compile = UNSTREAM_STRING( &constant_bin[ 620 ], 7, 1 );
    const_str_plain_exc_traceback = UNSTREAM_STRING( &constant_bin[ 627 ], 13, 1 );
    const_str_plain_exc_type = UNSTREAM_STRING( &constant_bin[ 640 ], 8, 1 );
    const_str_plain_exc_value = UNSTREAM_STRING( &constant_bin[ 648 ], 9, 1 );
    const_str_plain_inspect = UNSTREAM_STRING( &constant_bin[ 657 ], 7, 1 );
    const_str_plain_int = UNSTREAM_STRING( &constant_bin[ 228 ], 3, 1 );
    const_str_plain_iter = UNSTREAM_STRING( &constant_bin[ 664 ], 4, 1 );
    const_str_plain_len = UNSTREAM_STRING( &constant_bin[ 668 ], 3, 1 );
    const_str_plain_long = UNSTREAM_STRING( &constant_bin[ 671 ], 4, 1 );
    const_str_plain_open = UNSTREAM_STRING( &constant_bin[ 675 ], 4, 1 );
    const_str_plain_range = UNSTREAM_STRING( &constant_bin[ 679 ], 5, 1 );
    const_str_plain_repr = UNSTREAM_STRING( &constant_bin[ 684 ], 4, 1 );
    const_str_plain_site = UNSTREAM_STRING( &constant_bin[ 688 ], 4, 1 );
    const_str_plain_type = UNSTREAM_STRING( &constant_bin[ 644 ], 4, 1 );
    const_str_plain_xrange = UNSTREAM_STRING( &constant_bin[ 692 ], 6, 1 );
    const_tuple_empty = PyTuple_New( 0 );

    return;
}

void _initConstants( void )
{
    if ( _sentinel_value == NULL )
    {
#if PYTHON_VERSION < 300
        _sentinel_value = PyCObject_FromVoidPtr( NULL, NULL );
#else
        // The NULL value is not allowed for a capsule, so use something else.
        _sentinel_value = PyCapsule_New( (void *)27, "sentinel", NULL );
#endif
        assert( _sentinel_value );

        __initConstants();
    }
}
