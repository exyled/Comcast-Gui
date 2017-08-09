// Generated code for Python source for module '__main__'
// created by Nuitka version 0.5.5.3

// This code is in part copyright 2014 Kay Hayen.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "nuitka/prelude.hpp"

#include "__helpers.hpp"

// The _module___main__ is a Python object pointer of module type.

// Note: For full compatability with CPython, every module variable access
// needs to go through it except for cases where the module cannot possibly
// have changed in the mean time.

PyObject *module___main__;
PyDictObject *moduledict___main__;

// The module constants used
extern PyObject *const_int_0;
static PyObject *const_int_neg_1;
extern PyObject *const_dict_empty;
extern PyObject *const_tuple_empty;
static PyObject *const_str_plain_Tk;
static PyObject *const_str_plain_tk;
static PyObject *const_str_plain_app;
static PyObject *const_str_plain_Quit;
static PyObject *const_str_plain_blue;
static PyObject *const_str_plain_main;
static PyObject *const_str_plain_pack;
static PyObject *const_str_plain_self;
extern PyObject *const_str_plain_site;
static PyObject *const_str_plain_text;
static PyObject *const_str_plain_Label;
static PyObject *const_str_plain_title;
static PyObject *const_str_plain_white;
static PyObject *const_str_angle_module;
static PyObject *const_str_plain_Button;
static PyObject *const_str_plain_b_exit;
static PyObject *const_str_plain_Tkinter;
extern PyObject *const_str_plain___doc__;
static PyObject *const_str_plain_command;
static PyObject *const_str_plain_destroy;
extern PyObject *const_str_plain___file__;
static PyObject *const_str_plain___init__;
extern PyObject *const_str_plain___main__;
static PyObject *const_str_plain_mainloop;
static PyObject *const_str_plain_configure;
static PyObject *const_str_plain_lab_hello;
static PyObject *const_str_plain_WidgetDemo;
extern PyObject *const_str_plain___module__;
static PyObject *const_str_plain_background;
static PyObject *const_str_plain_foreground;
extern PyObject *const_str_plain___metaclass__;
static PyObject *const_tuple_str_plain_app_tuple;
static PyObject *const_tuple_str_plain_self_tuple;
static PyObject *const_dict_04588d8bc5177744f4d6e4195b93d9d6;
static PyObject *const_dict_e29e1387a4cb6955671919d9bd3d0499;
static PyObject *const_str_digest_313225d0405f74a210d28ee46a25fcc7;
static PyObject *const_str_digest_4a55219495777c37beda546fcd3d926d;
static PyObject *const_str_digest_bc35b76845cd49d655b08bd6d2a79faa;
static PyObject *const_str_digest_c833aa7a8bd3c01404d835d9501b6fb7;
static PyObject *const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328;
static PyObject *const_tuple_str_plain_self_str_plain_lab_hello_str_plain_b_exit_tuple;

static void _initModuleConstants(void)
{
    const_int_neg_1 = PyInt_FromLong( -1l );
    const_str_plain_Tk = UNSTREAM_STRING( &constant_bin[ 170 ], 2, 1 );
    const_str_plain_tk = UNSTREAM_STRING( &constant_bin[ 6 ], 2, 1 );
    const_str_plain_app = UNSTREAM_STRING( &constant_bin[ 172 ], 3, 1 );
    const_str_plain_Quit = UNSTREAM_STRING( &constant_bin[ 175 ], 4, 1 );
    const_str_plain_blue = UNSTREAM_STRING( &constant_bin[ 179 ], 4, 1 );
    const_str_plain_main = UNSTREAM_STRING( &constant_bin[ 30 ], 4, 1 );
    const_str_plain_pack = UNSTREAM_STRING( &constant_bin[ 183 ], 4, 1 );
    const_str_plain_self = UNSTREAM_STRING( &constant_bin[ 136 ], 4, 1 );
    const_str_plain_text = UNSTREAM_STRING( &constant_bin[ 187 ], 4, 1 );
    const_str_plain_Label = UNSTREAM_STRING( &constant_bin[ 191 ], 5, 1 );
    const_str_plain_title = UNSTREAM_STRING( &constant_bin[ 196 ], 5, 1 );
    const_str_plain_white = UNSTREAM_STRING( &constant_bin[ 201 ], 5, 1 );
    const_str_angle_module = UNSTREAM_STRING( &constant_bin[ 206 ], 8, 0 );
    const_str_plain_Button = UNSTREAM_STRING( &constant_bin[ 214 ], 6, 1 );
    const_str_plain_b_exit = UNSTREAM_STRING( &constant_bin[ 220 ], 6, 1 );
    const_str_plain_Tkinter = UNSTREAM_STRING( &constant_bin[ 226 ], 7, 1 );
    const_str_plain_command = UNSTREAM_STRING( &constant_bin[ 233 ], 7, 1 );
    const_str_plain_destroy = UNSTREAM_STRING( &constant_bin[ 240 ], 7, 1 );
    const_str_plain___init__ = UNSTREAM_STRING( &constant_bin[ 247 ], 8, 1 );
    const_str_plain_mainloop = UNSTREAM_STRING( &constant_bin[ 255 ], 8, 1 );
    const_str_plain_configure = UNSTREAM_STRING( &constant_bin[ 263 ], 9, 1 );
    const_str_plain_lab_hello = UNSTREAM_STRING( &constant_bin[ 272 ], 9, 1 );
    const_str_plain_WidgetDemo = UNSTREAM_STRING( &constant_bin[ 63 ], 10, 1 );
    const_str_plain_background = UNSTREAM_STRING( &constant_bin[ 281 ], 10, 1 );
    const_str_plain_foreground = UNSTREAM_STRING( &constant_bin[ 291 ], 10, 1 );
    const_tuple_str_plain_app_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_app_tuple, 0, const_str_plain_app ); Py_INCREF( const_str_plain_app );
    const_tuple_str_plain_self_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_self_tuple, 0, const_str_plain_self ); Py_INCREF( const_str_plain_self );
    const_dict_04588d8bc5177744f4d6e4195b93d9d6 = _PyDict_NewPresized( 1 );
    const_str_digest_4a55219495777c37beda546fcd3d926d = UNSTREAM_STRING( &constant_bin[ 301 ], 20, 0 );
    PyDict_SetItem( const_dict_04588d8bc5177744f4d6e4195b93d9d6, const_str_plain_text, const_str_digest_4a55219495777c37beda546fcd3d926d );
    const_dict_e29e1387a4cb6955671919d9bd3d0499 = _PyDict_NewPresized( 2 );
    PyDict_SetItem( const_dict_e29e1387a4cb6955671919d9bd3d0499, const_str_plain_foreground, const_str_plain_white );
    PyDict_SetItem( const_dict_e29e1387a4cb6955671919d9bd3d0499, const_str_plain_background, const_str_plain_blue );
    const_str_digest_313225d0405f74a210d28ee46a25fcc7 = UNSTREAM_STRING( &constant_bin[ 321 ], 42, 0 );
    const_str_digest_bc35b76845cd49d655b08bd6d2a79faa = UNSTREAM_STRING( &constant_bin[ 363 ], 18, 0 );
    const_str_digest_c833aa7a8bd3c01404d835d9501b6fb7 = UNSTREAM_STRING( &constant_bin[ 381 ], 41, 0 );
    const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328 = UNSTREAM_STRING( &constant_bin[ 422 ], 13, 0 );
    const_tuple_str_plain_self_str_plain_lab_hello_str_plain_b_exit_tuple = PyTuple_New( 3 );
    PyTuple_SET_ITEM( const_tuple_str_plain_self_str_plain_lab_hello_str_plain_b_exit_tuple, 0, const_str_plain_self ); Py_INCREF( const_str_plain_self );
    PyTuple_SET_ITEM( const_tuple_str_plain_self_str_plain_lab_hello_str_plain_b_exit_tuple, 1, const_str_plain_lab_hello ); Py_INCREF( const_str_plain_lab_hello );
    PyTuple_SET_ITEM( const_tuple_str_plain_self_str_plain_lab_hello_str_plain_b_exit_tuple, 2, const_str_plain_b_exit ); Py_INCREF( const_str_plain_b_exit );
}

// The module code objects.
static PyCodeObject *codeobj_ae7d60acb34059627f4a268a1c024c6c;
static PyCodeObject *codeobj_10287389bdce4027bba08c715722073a;
static PyCodeObject *codeobj_236c2a45d30aceb0eb190e3b241f0226;
static PyCodeObject *codeobj_dfe196699204d7df86fcc77d588622e4;
static PyCodeObject *codeobj_635b15c8ce432d146f5ed6c08279ff74;
static PyCodeObject *codeobj_91a04261e62a72c535b9ae34e911aa9b;

static void _initModuleCodeObjects(void)
{
    codeobj_ae7d60acb34059627f4a268a1c024c6c = MAKE_CODEOBJ( const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328, const_str_angle_module, 0, const_tuple_empty, 0, CO_NOFREE );
    codeobj_10287389bdce4027bba08c715722073a = MAKE_CODEOBJ( const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328, const_str_plain_WidgetDemo, 12, const_tuple_empty, 0, CO_NEWLOCALS | CO_NOFREE );
    codeobj_236c2a45d30aceb0eb190e3b241f0226 = MAKE_CODEOBJ( const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328, const_str_plain___init__, 14, const_tuple_str_plain_self_tuple, 1, CO_NEWLOCALS | CO_OPTIMIZED | CO_NOFREE );
    codeobj_dfe196699204d7df86fcc77d588622e4 = MAKE_CODEOBJ( const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328, const_str_plain___init__, 14, const_tuple_str_plain_self_str_plain_lab_hello_str_plain_b_exit_tuple, 1, CO_NEWLOCALS | CO_OPTIMIZED | CO_NOFREE );
    codeobj_635b15c8ce432d146f5ed6c08279ff74 = MAKE_CODEOBJ( const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328, const_str_plain_main, 7, const_tuple_empty, 0, CO_NEWLOCALS | CO_OPTIMIZED | CO_NOFREE );
    codeobj_91a04261e62a72c535b9ae34e911aa9b = MAKE_CODEOBJ( const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328, const_str_plain_main, 7, const_tuple_str_plain_app_tuple, 0, CO_NEWLOCALS | CO_OPTIMIZED | CO_NOFREE );
}

// The module function declarations.
NUITKA_LOCAL_MODULE PyObject *impl_class_2_WidgetDemo_of_module___main__(  );


static PyObject *MAKE_FUNCTION_function_1___init___of_class_2_WidgetDemo_of_module___main__(  );


static PyObject *MAKE_FUNCTION_function_1_main_of_module___main__(  );


// The module function definitions.
static PyObject *impl_function_1_main_of_module___main__( Nuitka_FunctionObject *self )
{
    // No context is used.

    // Local variable declarations.
    PyObjectLocalVariable var_app;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_called_1;
    PyObject *tmp_called_2;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    tmp_return_value = NULL;

    // Actual function code.
    static PyFrameObject *cache_frame_function = NULL;
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_635b15c8ce432d146f5ed6c08279ff74, module___main__ );
    PyFrameObject *frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    tmp_called_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WidgetDemo );

    if (unlikely( tmp_called_1 == NULL ))
    {
        tmp_called_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_WidgetDemo );
    }

    if ( tmp_called_1 == NULL )
    {

        exception_type = INCREASE_REFCOUNT( PyExc_NameError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 50 ], 39, 0 );
        exception_tb = NULL;

        frame_function->f_lineno = 9;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 9;
    tmp_assign_source_1 = CALL_FUNCTION_NO_ARGS( tmp_called_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 9;
        goto frame_exception_exit_1;
    }
    assert( var_app.object == NULL );
    var_app.object = tmp_assign_source_1;

    tmp_source_name_1 = var_app.object;

    tmp_called_2 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_mainloop );
    if ( tmp_called_2 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 10;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 10;
    tmp_unused = CALL_FUNCTION_NO_ARGS( tmp_called_2 );
    Py_DECREF( tmp_called_2 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 10;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( INCREASE_REFCOUNT( frame_function ) );
    }
    else if ( exception_tb->tb_frame != frame_function )
    {
        PyTracebackObject *traceback_new = (PyTracebackObject *)MAKE_TRACEBACK( INCREASE_REFCOUNT( frame_function ) );
        traceback_new->tb_next = exception_tb;
        exception_tb = traceback_new;
    }


    tmp_frame_locals = PyDict_New();
    if ((var_app.object != NULL))
    {
        PyDict_SetItem(
            tmp_frame_locals,
            const_str_plain_app,
            var_app.object
        );

    }
    detachFrame( exception_tb, tmp_frame_locals );


    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto function_return_exit;

    // Return statement must be present.
    assert(false);
function_exception_exit:
    assert( exception_type );
    PyErr_Restore( exception_type, exception_value, (PyObject *)exception_tb );
    return NULL;
function_return_exit:
    return tmp_return_value;

}
static PyObject *fparse_function_1_main_of_module___main__( Nuitka_FunctionObject *self, PyObject **args, Py_ssize_t args_size, PyObject *kw )
{
    assert( kw == NULL || PyDict_Check( kw ) );

    NUITKA_MAY_BE_UNUSED Py_ssize_t kw_size = kw ? PyDict_Size( kw ) : 0;
    NUITKA_MAY_BE_UNUSED Py_ssize_t kw_found = 0;
    NUITKA_MAY_BE_UNUSED Py_ssize_t kw_only_found = 0;
    Py_ssize_t args_given = args_size;

    if (unlikely( args_given + kw_size > 0 ))
    {
#if PYTHON_VERSION < 330
        ERROR_NO_ARGUMENTS_ALLOWED(
           self,
           args_given + kw_size
        );
#else
        ERROR_NO_ARGUMENTS_ALLOWED(
           self,
           kw_size > 0 ? kw : NULL,
           args_given
        );
#endif

        goto error_exit;
    }


    return impl_function_1_main_of_module___main__( self );

error_exit:;


    return NULL;
}

static PyObject *dparse_function_1_main_of_module___main__( Nuitka_FunctionObject *self, PyObject **args, int size )
{
    if ( size == 0 )
    {
        return impl_function_1_main_of_module___main__( self );
    }
    else
    {
        PyObject *result = fparse_function_1_main_of_module___main__( self, args, size, NULL );
        return result;
    }

}



NUITKA_LOCAL_MODULE PyObject *impl_class_2_WidgetDemo_of_module___main__(  )
{
    // No context is used.

    // Local variable declarations.
    PyObjectLocalVariable var___module__;
    PyObjectLocalVariable var___init__;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    tmp_return_value = NULL;

    // Actual function code.
    tmp_assign_source_1 = const_str_plain___main__;
    assert( var___module__.object == NULL );
    var___module__.object = INCREASE_REFCOUNT( tmp_assign_source_1 );

    static PyFrameObject *cache_frame_function = NULL;
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_10287389bdce4027bba08c715722073a, module___main__ );
    PyFrameObject *frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    tmp_assign_source_2 = MAKE_FUNCTION_function_1___init___of_class_2_WidgetDemo_of_module___main__(  );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );
        Py_DECREF( tmp_assign_source_2 );

        frame_function->f_lineno = 14;
        goto frame_exception_exit_1;
    }
    assert( var___init__.object == NULL );
    var___init__.object = tmp_assign_source_2;


#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( INCREASE_REFCOUNT( frame_function ) );
    }
    else if ( exception_tb->tb_frame != frame_function )
    {
        PyTracebackObject *traceback_new = (PyTracebackObject *)MAKE_TRACEBACK( INCREASE_REFCOUNT( frame_function ) );
        traceback_new->tb_next = exception_tb;
        exception_tb = traceback_new;
    }


    tmp_frame_locals = PyDict_New();
    if ((var___module__.object != NULL))
    {
        PyDict_SetItem(
            tmp_frame_locals,
            const_str_plain___module__,
            var___module__.object
        );

    }
    if ((var___init__.object != NULL))
    {
        PyDict_SetItem(
            tmp_frame_locals,
            const_str_plain___init__,
            var___init__.object
        );

    }
    detachFrame( exception_tb, tmp_frame_locals );


    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;
    tmp_return_value = PyDict_New();
    if ((var___module__.object != NULL))
    {
        PyDict_SetItem(
            tmp_return_value,
            const_str_plain___module__,
            var___module__.object
        );

    }
    if ((var___init__.object != NULL))
    {
        PyDict_SetItem(
            tmp_return_value,
            const_str_plain___init__,
            var___init__.object
        );

    }
    goto function_return_exit;

    // Return statement must be present.
    assert(false);
function_exception_exit:
    assert( exception_type );
    PyErr_Restore( exception_type, exception_value, (PyObject *)exception_tb );
    return NULL;
function_return_exit:
    return tmp_return_value;

}


static PyObject *impl_function_1___init___of_class_2_WidgetDemo_of_module___main__( Nuitka_FunctionObject *self, PyObject *_python_par_self )
{
    // No context is used.

    // Local variable declarations.
    PyObjectLocalVariable par_self; par_self.object = _python_par_self;
    PyObjectLocalVariable var_lab_hello;
    PyObjectLocalVariable var_b_exit;
    PyObject *exception_type = NULL, *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_call_arg_element_1;
    PyObject *tmp_call_arg_element_2;
    PyObject *tmp_call_kw_1;
    PyObject *tmp_call_kw_2;
    PyObject *tmp_call_kw_3;
    PyObject *tmp_called_1;
    PyObject *tmp_called_2;
    PyObject *tmp_called_3;
    PyObject *tmp_called_4;
    PyObject *tmp_called_5;
    PyObject *tmp_called_6;
    PyObject *tmp_called_7;
    PyObject *tmp_dict_key_1;
    PyObject *tmp_dict_key_2;
    PyObject *tmp_dict_value_1;
    PyObject *tmp_dict_value_2;
    PyObject *tmp_frame_locals;
    PyObject *tmp_return_value;
    PyObject *tmp_source_name_1;
    PyObject *tmp_source_name_2;
    PyObject *tmp_source_name_3;
    PyObject *tmp_source_name_4;
    PyObject *tmp_source_name_5;
    PyObject *tmp_source_name_6;
    PyObject *tmp_source_name_7;
    PyObject *tmp_source_name_8;
    PyObject *tmp_source_name_9;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;
    tmp_return_value = NULL;

    // Actual function code.
    static PyFrameObject *cache_frame_function = NULL;
    MAKE_OR_REUSE_FRAME( cache_frame_function, codeobj_236c2a45d30aceb0eb190e3b241f0226, module___main__ );
    PyFrameObject *frame_function = cache_frame_function;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_function );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    Py_INCREF( frame_function );
    assert( Py_REFCNT( frame_function ) == 2 ); // Frame stack

#if PYTHON_VERSION >= 340
    frame_function->f_executing += 1;
#endif

    // Framed code:
    tmp_source_name_2 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_tk );

    if (unlikely( tmp_source_name_2 == NULL ))
    {
        tmp_source_name_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_tk );
    }

    if ( tmp_source_name_2 == NULL )
    {

        exception_type = INCREASE_REFCOUNT( PyExc_NameError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 89 ], 31, 0 );
        exception_tb = NULL;

        frame_function->f_lineno = 15;
        goto frame_exception_exit_1;
    }

    tmp_source_name_1 = LOOKUP_ATTRIBUTE( tmp_source_name_2, const_str_plain_Tk );
    if ( tmp_source_name_1 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 15;
        goto frame_exception_exit_1;
    }
    tmp_called_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain___init__ );
    Py_DECREF( tmp_source_name_1 );
    if ( tmp_called_1 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 15;
        goto frame_exception_exit_1;
    }
    tmp_call_arg_element_1 = par_self.object;

    if ( tmp_call_arg_element_1 == NULL )
    {
        Py_DECREF( tmp_called_1 );
        exception_type = INCREASE_REFCOUNT( PyExc_UnboundLocalError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 120 ], 50, 0 );
        exception_tb = NULL;

        frame_function->f_lineno = 15;
        goto frame_exception_exit_1;
    }

    frame_function->f_lineno = 15;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_1, tmp_call_arg_element_1 );
    Py_DECREF( tmp_called_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 15;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_3 = par_self.object;

    if ( tmp_source_name_3 == NULL )
    {

        exception_type = INCREASE_REFCOUNT( PyExc_UnboundLocalError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 120 ], 50, 0 );
        exception_tb = NULL;

        frame_function->f_lineno = 17;
        goto frame_exception_exit_1;
    }

    tmp_called_2 = LOOKUP_ATTRIBUTE( tmp_source_name_3, const_str_plain_title );
    if ( tmp_called_2 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 17;
        goto frame_exception_exit_1;
    }
    tmp_call_arg_element_2 = const_str_digest_bc35b76845cd49d655b08bd6d2a79faa;
    frame_function->f_lineno = 17;
    tmp_unused = CALL_FUNCTION_WITH_ARGS1( tmp_called_2, tmp_call_arg_element_2 );
    Py_DECREF( tmp_called_2 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 17;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_4 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_tk );

    if (unlikely( tmp_source_name_4 == NULL ))
    {
        tmp_source_name_4 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_tk );
    }

    if ( tmp_source_name_4 == NULL )
    {

        exception_type = INCREASE_REFCOUNT( PyExc_NameError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 89 ], 31, 0 );
        exception_tb = NULL;

        frame_function->f_lineno = 19;
        goto frame_exception_exit_1;
    }

    tmp_called_3 = LOOKUP_ATTRIBUTE( tmp_source_name_4, const_str_plain_Label );
    if ( tmp_called_3 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 19;
        goto frame_exception_exit_1;
    }
    tmp_call_kw_1 = PyDict_Copy( const_dict_04588d8bc5177744f4d6e4195b93d9d6 );
    frame_function->f_lineno = 19;
    tmp_assign_source_1 = CALL_FUNCTION_WITH_KEYARGS( tmp_called_3, tmp_call_kw_1 );
    Py_DECREF( tmp_called_3 );
    Py_DECREF( tmp_call_kw_1 );
    if ( tmp_assign_source_1 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 19;
        goto frame_exception_exit_1;
    }
    assert( var_lab_hello.object == NULL );
    var_lab_hello.object = tmp_assign_source_1;

    tmp_source_name_5 = var_lab_hello.object;

    tmp_called_4 = LOOKUP_ATTRIBUTE( tmp_source_name_5, const_str_plain_configure );
    if ( tmp_called_4 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 20;
        goto frame_exception_exit_1;
    }
    tmp_call_kw_2 = PyDict_Copy( const_dict_e29e1387a4cb6955671919d9bd3d0499 );
    frame_function->f_lineno = 20;
    tmp_unused = CALL_FUNCTION_WITH_KEYARGS( tmp_called_4, tmp_call_kw_2 );
    Py_DECREF( tmp_called_4 );
    Py_DECREF( tmp_call_kw_2 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 20;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_6 = var_lab_hello.object;

    tmp_called_5 = LOOKUP_ATTRIBUTE( tmp_source_name_6, const_str_plain_pack );
    if ( tmp_called_5 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 21;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 21;
    tmp_unused = CALL_FUNCTION_NO_ARGS( tmp_called_5 );
    Py_DECREF( tmp_called_5 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 21;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_source_name_7 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_tk );

    if (unlikely( tmp_source_name_7 == NULL ))
    {
        tmp_source_name_7 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_tk );
    }

    if ( tmp_source_name_7 == NULL )
    {

        exception_type = INCREASE_REFCOUNT( PyExc_NameError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 89 ], 31, 0 );
        exception_tb = NULL;

        frame_function->f_lineno = 23;
        goto frame_exception_exit_1;
    }

    tmp_called_6 = LOOKUP_ATTRIBUTE( tmp_source_name_7, const_str_plain_Button );
    if ( tmp_called_6 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 23;
        goto frame_exception_exit_1;
    }
    tmp_call_kw_3 = _PyDict_NewPresized( 2 );
    tmp_dict_value_1 = const_str_plain_Quit;
    tmp_dict_key_1 = const_str_plain_text;
    PyDict_SetItem( tmp_call_kw_3, tmp_dict_key_1, tmp_dict_value_1 );
    tmp_source_name_8 = par_self.object;

    if ( tmp_source_name_8 == NULL )
    {
        Py_DECREF( tmp_called_6 );
        Py_DECREF( tmp_call_kw_3 );
        exception_type = INCREASE_REFCOUNT( PyExc_UnboundLocalError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 120 ], 50, 0 );
        exception_tb = NULL;

        frame_function->f_lineno = 23;
        goto frame_exception_exit_1;
    }

    tmp_dict_value_2 = LOOKUP_ATTRIBUTE( tmp_source_name_8, const_str_plain_destroy );
    if ( tmp_dict_value_2 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );
        Py_DECREF( tmp_called_6 );
        Py_DECREF( tmp_call_kw_3 );

        frame_function->f_lineno = 23;
        goto frame_exception_exit_1;
    }
    tmp_dict_key_2 = const_str_plain_command;
    PyDict_SetItem( tmp_call_kw_3, tmp_dict_key_2, tmp_dict_value_2 );
    Py_DECREF( tmp_dict_value_2 );
    frame_function->f_lineno = 23;
    tmp_assign_source_2 = CALL_FUNCTION_WITH_KEYARGS( tmp_called_6, tmp_call_kw_3 );
    Py_DECREF( tmp_called_6 );
    Py_DECREF( tmp_call_kw_3 );
    if ( tmp_assign_source_2 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 23;
        goto frame_exception_exit_1;
    }
    assert( var_b_exit.object == NULL );
    var_b_exit.object = tmp_assign_source_2;

    tmp_source_name_9 = var_b_exit.object;

    tmp_called_7 = LOOKUP_ATTRIBUTE( tmp_source_name_9, const_str_plain_pack );
    if ( tmp_called_7 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 24;
        goto frame_exception_exit_1;
    }
    frame_function->f_lineno = 24;
    tmp_unused = CALL_FUNCTION_NO_ARGS( tmp_called_7 );
    Py_DECREF( tmp_called_7 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_function->f_lineno = 24;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif
    // Put the previous frame back on top.
    popFrameStack();
#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );
    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_function );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( INCREASE_REFCOUNT( frame_function ) );
    }
    else if ( exception_tb->tb_frame != frame_function )
    {
        PyTracebackObject *traceback_new = (PyTracebackObject *)MAKE_TRACEBACK( INCREASE_REFCOUNT( frame_function ) );
        traceback_new->tb_next = exception_tb;
        exception_tb = traceback_new;
    }


    tmp_frame_locals = PyDict_New();
    if ((var_lab_hello.object != NULL))
    {
        PyDict_SetItem(
            tmp_frame_locals,
            const_str_plain_lab_hello,
            var_lab_hello.object
        );

    }
    if ((var_b_exit.object != NULL))
    {
        PyDict_SetItem(
            tmp_frame_locals,
            const_str_plain_b_exit,
            var_b_exit.object
        );

    }
    if ((par_self.object != NULL))
    {
        PyDict_SetItem(
            tmp_frame_locals,
            const_str_plain_self,
            par_self.object
        );

    }
    detachFrame( exception_tb, tmp_frame_locals );


    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_function->f_executing -= 1;
#endif
    Py_DECREF( frame_function );

    // Return the error.
    goto function_exception_exit;
    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto function_return_exit;

    // Return statement must be present.
    assert(false);
function_exception_exit:
    assert( exception_type );
    PyErr_Restore( exception_type, exception_value, (PyObject *)exception_tb );
    return NULL;
function_return_exit:
    return tmp_return_value;

}
static PyObject *fparse_function_1___init___of_class_2_WidgetDemo_of_module___main__( Nuitka_FunctionObject *self, PyObject **args, Py_ssize_t args_size, PyObject *kw )
{
    assert( kw == NULL || PyDict_Check( kw ) );

    NUITKA_MAY_BE_UNUSED Py_ssize_t kw_size = kw ? PyDict_Size( kw ) : 0;
    NUITKA_MAY_BE_UNUSED Py_ssize_t kw_found = 0;
    NUITKA_MAY_BE_UNUSED Py_ssize_t kw_only_found = 0;
    Py_ssize_t args_given = args_size;
    PyObject *_python_par_self = NULL;
    // Copy given dictionary values to the the respective variables:
    if ( kw_size > 0 )
    {
        Py_ssize_t ppos = 0;
        PyObject *key, *value;

        while( PyDict_Next( kw, &ppos, &key, &value ) )
        {
#if PYTHON_VERSION < 300
            if (unlikely( !PyString_Check( key ) && !PyUnicode_Check( key ) ))
#else
            if (unlikely( !PyUnicode_Check( key ) ))
#endif
            {
                PyErr_Format( PyExc_TypeError, "__init__() keywords must be strings" );
                goto error_exit;
            }

            NUITKA_MAY_BE_UNUSED bool found = false;

            Py_INCREF( key );
            Py_INCREF( value );

            // Quick path, could be our value.
            if ( found == false && const_str_plain_self == key )
            {
                assert( _python_par_self == NULL );
                _python_par_self = value;

                found = true;
                kw_found += 1;
            }

            // Slow path, compare against all parameter names.
            if ( found == false && RICH_COMPARE_BOOL_EQ( const_str_plain_self, key ) == 1 )
            {
                assert( _python_par_self == NULL );
                _python_par_self = value;

                found = true;
                kw_found += 1;
            }


            Py_DECREF( key );

            if ( found == false )
            {
               Py_DECREF( value );

               PyErr_Format(
                   PyExc_TypeError,
                   "__init__() got an unexpected keyword argument '%s'",
                   Nuitka_String_Check( key ) ? Nuitka_String_AsString( key ) : "<non-string>"
               );

               goto error_exit;
            }
        }

#if PYTHON_VERSION < 300
        assert( kw_found == kw_size );
        assert( kw_only_found == 0 );
#endif
    }

    // Check if too many arguments were given in case of non star args
    if (unlikely( args_given > 1 ))
    {
#if PYTHON_VERSION < 270
        ERROR_TOO_MANY_ARGUMENTS( self, args_given, kw_size );
#elif PYTHON_VERSION < 330
        ERROR_TOO_MANY_ARGUMENTS( self, args_given + kw_found );
#else
        ERROR_TOO_MANY_ARGUMENTS( self, args_given, kw_only_found );
#endif
        goto error_exit;
    }


    // Copy normal parameter values given as part of the args list to the respective variables:

    if (likely( 0 < args_given ))
    {
         if (unlikely( _python_par_self != NULL ))
         {
             ERROR_MULTIPLE_VALUES( self, 0 );
             goto error_exit;
         }

        _python_par_self = INCREASE_REFCOUNT( args[ 0 ] );
    }
    else if ( _python_par_self == NULL )
    {
        if ( 0 + self->m_defaults_given >= 1  )
        {
            _python_par_self = INCREASE_REFCOUNT( PyTuple_GET_ITEM( self->m_defaults, self->m_defaults_given + 0 - 1 ) );
        }
#if PYTHON_VERSION < 330
        else
        {
#if PYTHON_VERSION < 270
            ERROR_TOO_FEW_ARGUMENTS( self, kw_size, args_given + kw_found );
#elif PYTHON_VERSION < 300
            ERROR_TOO_FEW_ARGUMENTS( self, args_given + kw_found );
#else
            ERROR_TOO_FEW_ARGUMENTS( self, args_given + kw_found - kw_only_found );
#endif

            goto error_exit;
        }
#endif
    }

#if PYTHON_VERSION >= 330
    if (unlikely( _python_par_self == NULL ))
    {
        PyObject *values[] = { _python_par_self };
        ERROR_TOO_FEW_ARGUMENTS( self, values );

        goto error_exit;
    }
#endif


    return impl_function_1___init___of_class_2_WidgetDemo_of_module___main__( self, _python_par_self );

error_exit:;

    Py_XDECREF( _python_par_self );

    return NULL;
}

static PyObject *dparse_function_1___init___of_class_2_WidgetDemo_of_module___main__( Nuitka_FunctionObject *self, PyObject **args, int size )
{
    if ( size == 1 )
    {
        return impl_function_1___init___of_class_2_WidgetDemo_of_module___main__( self, INCREASE_REFCOUNT( args[ 0 ] ) );
    }
    else
    {
        PyObject *result = fparse_function_1___init___of_class_2_WidgetDemo_of_module___main__( self, args, size, NULL );
        return result;
    }

}




static PyObject *MAKE_FUNCTION_function_1___init___of_class_2_WidgetDemo_of_module___main__(  )
{
    PyObject *result = Nuitka_Function_New(
        fparse_function_1___init___of_class_2_WidgetDemo_of_module___main__,
        dparse_function_1___init___of_class_2_WidgetDemo_of_module___main__,
        const_str_plain___init__,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_dfe196699204d7df86fcc77d588622e4,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module___main__,
        Py_None
    );

    return result;
}



static PyObject *MAKE_FUNCTION_function_1_main_of_module___main__(  )
{
    PyObject *result = Nuitka_Function_New(
        fparse_function_1_main_of_module___main__,
        dparse_function_1_main_of_module___main__,
        const_str_plain_main,
#if PYTHON_VERSION >= 330
        NULL,
#endif
        codeobj_91a04261e62a72c535b9ae34e911aa9b,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        const_dict_empty,
#endif
        module___main__,
        const_str_digest_313225d0405f74a210d28ee46a25fcc7
    );

    return result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef___main__ =
{
    PyModuleDef_HEAD_INIT,
    "__main__",   /* m_name */
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

#define _MODULE_UNFREEZER 0

#if _MODULE_UNFREEZER

#include "nuitka/unfreezing.hpp"

// Table for lookup to find "frozen" modules or DLLs, i.e. the ones included in
// or along this binary.

static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] =
{

    { NULL, NULL, 0 }
};

#endif

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( __main__ )
{

#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Packages can be imported recursively in deep executables.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module___main__ );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    _initConstants();

    // Initialize the compiled types of Nuitka.
    PyType_Ready( &Nuitka_Generator_Type );
    PyType_Ready( &Nuitka_Function_Type );
    PyType_Ready( &Nuitka_Method_Type );
    PyType_Ready( &Nuitka_Frame_Type );
#if PYTHON_VERSION < 300
    initSlotCompare();
#endif

    patchBuiltinModule();
    patchTypeComparison();

#endif

#if _MODULE_UNFREEZER
    registerMetaPathBasedUnfreezer( meta_path_loader_entries );
#endif

    _initModuleConstants();
    _initModuleCodeObjects();

    // puts( "in init__main__" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module___main__ = Py_InitModule4(
        "__main__",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No __doc__ is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else
    module___main__ = PyModule_Create( &mdef___main__ );
#endif

    moduledict___main__ = (PyDictObject *)((PyModuleObject *)module___main__)->md_dict;

    assertObject( module___main__ );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PySys_GetObject( (char *)"modules" ), const_str_plain___main__, module___main__ );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    PyObject *module_dict = PyModule_GetDict( module___main__ );

    if ( PyDict_GetItem( module_dict, const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then.
#if !defined(_NUITKA_EXE) || !1
        value = PyModule_GetDict( value );
#endif

#ifndef __NUITKA_NO_ASSERT__
        int res =
#endif
            PyDict_SetItem( module_dict, const_str_plain___builtins__, value );

        assert( res == 0 );
    }

#if PYTHON_VERSION >= 330
#if _MODULE_UNFREEZER
    PyDict_SetItem( module_dict, const_str_plain___loader__, metapath_based_loader );
#else
    PyDict_SetItem( module_dict, const_str_plain___loader__, Py_None );
#endif
#endif

    // Temp variables if any
    PyObjectTempVariable tmp_class_creation_1__bases;
    PyObjectTempVariable tmp_class_creation_1__class_dict;
    PyObjectTempVariable tmp_class_creation_1__metaclass;
    PyObjectTempVariable tmp_class_creation_1__class;
    PyObject *exception_type, *exception_value;
    PyTracebackObject *exception_tb;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    PyObject *tmp_assign_source_1;
    PyObject *tmp_assign_source_2;
    PyObject *tmp_assign_source_3;
    PyObject *tmp_assign_source_4;
    PyObject *tmp_assign_source_5;
    PyObject *tmp_assign_source_6;
    PyObject *tmp_assign_source_7;
    PyObject *tmp_assign_source_8;
    PyObject *tmp_assign_source_9;
    PyObject *tmp_call_arg_element_1;
    PyObject *tmp_call_arg_element_2;
    PyObject *tmp_call_arg_element_3;
    PyObject *tmp_called_1;
    PyObject *tmp_called_2;
    PyObject *tmp_class_bases_1;
    int tmp_cmp_In_1;
    PyObject *tmp_compare_left_1;
    PyObject *tmp_compare_right_1;
    PyObject *tmp_dget_dict_1;
    PyObject *tmp_dget_key_1;
    PyObject *tmp_import_globals_1;
    PyObject *tmp_import_globals_2;
    PyObject *tmp_source_name_1;
    int tmp_tried_lineno_1;
    PyObject *tmp_tuple_element_1;
    NUITKA_MAY_BE_UNUSED PyObject *tmp_unused;

    // Module code.
    // Frame without reuse.
    PyFrameObject *frame_module = MAKE_FRAME( codeobj_ae7d60acb34059627f4a268a1c024c6c, module___main__ );

    // Push the new frame as the currently active one, and we should be exlusively
    // owning it.
    pushFrameStack( frame_module );
    assert( Py_REFCNT( frame_module ) == 1 );

#if PYTHON_VERSION >= 340
    frame_module->f_executing += 1;
#endif

    // Framed code:
    tmp_import_globals_1 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 1;
    tmp_unused = IMPORT_MODULE( const_str_plain_site, tmp_import_globals_1, tmp_import_globals_1, const_tuple_empty, const_int_neg_1 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_module->f_lineno = 1;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );
    tmp_assign_source_1 = const_str_digest_c833aa7a8bd3c01404d835d9501b6fb7;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    tmp_assign_source_2 = const_str_digest_cf5a0ecec5de0a4ef69cd6b30b1e4328;
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    tmp_import_globals_2 = ((PyModuleObject *)module___main__)->md_dict;
    frame_module->f_lineno = 3;
    tmp_assign_source_3 = IMPORT_MODULE( const_str_plain_Tkinter, tmp_import_globals_2, tmp_import_globals_2, Py_None, const_int_neg_1 );
    if ( tmp_assign_source_3 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_module->f_lineno = 3;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_tk, tmp_assign_source_3 );
    tmp_assign_source_4 = MAKE_FUNCTION_function_1_main_of_module___main__(  );
    if ( tmp_assign_source_4 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );
        Py_DECREF( tmp_assign_source_4 );

        frame_module->f_lineno = 7;
        goto frame_exception_exit_1;
    }
    UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_main, tmp_assign_source_4 );
    // Tried code
    tmp_assign_source_5 = PyTuple_New( 1 );
    tmp_source_name_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_tk );

    if (unlikely( tmp_source_name_1 == NULL ))
    {
        tmp_source_name_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_tk );
    }

    if ( tmp_source_name_1 == NULL )
    {
        Py_DECREF( tmp_assign_source_5 );
        exception_type = INCREASE_REFCOUNT( PyExc_NameError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 0 ], 24, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 12;
        goto try_finally_handler_1;
    }

    tmp_tuple_element_1 = LOOKUP_ATTRIBUTE( tmp_source_name_1, const_str_plain_Tk );
    if ( tmp_tuple_element_1 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );
        Py_DECREF( tmp_assign_source_5 );

        frame_module->f_lineno = 12;
        goto try_finally_handler_1;
    }
    PyTuple_SET_ITEM( tmp_assign_source_5, 0, tmp_tuple_element_1 );
    assert( tmp_class_creation_1__bases.object == NULL );
    tmp_class_creation_1__bases.object = tmp_assign_source_5;

    tmp_assign_source_6 = impl_class_2_WidgetDemo_of_module___main__(  );
    if ( tmp_assign_source_6 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_module->f_lineno = 12;
        goto try_finally_handler_1;
    }
    assert( tmp_class_creation_1__class_dict.object == NULL );
    tmp_class_creation_1__class_dict.object = tmp_assign_source_6;

    tmp_compare_left_1 = const_str_plain___metaclass__;
    tmp_compare_right_1 = tmp_class_creation_1__class_dict.object;

    tmp_cmp_In_1 = PySequence_Contains( tmp_compare_right_1, tmp_compare_left_1 );
    if ( tmp_cmp_In_1 == -1 )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_module->f_lineno = 12;
        goto try_finally_handler_1;
    }
    if (tmp_cmp_In_1 == 1)
    {
        goto condexpr_true_1;
    }
    else
    {
        goto condexpr_false_1;
    }
    condexpr_true_1:;
    tmp_dget_dict_1 = tmp_class_creation_1__class_dict.object;

    tmp_dget_key_1 = const_str_plain___metaclass__;
    tmp_assign_source_7 = DICT_GET_ITEM( tmp_dget_dict_1, tmp_dget_key_1 );
    if ( tmp_assign_source_7 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_module->f_lineno = 12;
        goto try_finally_handler_1;
    }
    goto condexpr_end_1;
    condexpr_false_1:;
    tmp_class_bases_1 = tmp_class_creation_1__bases.object;

    tmp_assign_source_7 = SELECT_METACLASS( tmp_class_bases_1, GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___metaclass__ ) );
    condexpr_end_1:;
    assert( tmp_class_creation_1__metaclass.object == NULL );
    tmp_class_creation_1__metaclass.object = tmp_assign_source_7;

    tmp_called_1 = tmp_class_creation_1__metaclass.object;

    tmp_call_arg_element_1 = const_str_plain_WidgetDemo;
    tmp_call_arg_element_2 = tmp_class_creation_1__bases.object;

    tmp_call_arg_element_3 = tmp_class_creation_1__class_dict.object;

    frame_module->f_lineno = 12;
    tmp_assign_source_8 = CALL_FUNCTION_WITH_ARGS3( tmp_called_1, tmp_call_arg_element_1, tmp_call_arg_element_2, tmp_call_arg_element_3 );
    if ( tmp_assign_source_8 == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_module->f_lineno = 12;
        goto try_finally_handler_1;
    }
    assert( tmp_class_creation_1__class.object == NULL );
    tmp_class_creation_1__class.object = tmp_assign_source_8;

    tmp_assign_source_9 = tmp_class_creation_1__class.object;

    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain_WidgetDemo, tmp_assign_source_9 );
    // Final block of try/finally
    // Tried block ends with no exception occured, note that.
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    try_finally_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;

    tmp_tried_lineno_1 = frame_module->f_lineno;
    Py_XDECREF( tmp_class_creation_1__class.object );
    tmp_class_creation_1__class.object = NULL;

    Py_XDECREF( tmp_class_creation_1__bases.object );
    tmp_class_creation_1__bases.object = NULL;

    Py_XDECREF( tmp_class_creation_1__class_dict.object );
    tmp_class_creation_1__class_dict.object = NULL;

    Py_XDECREF( tmp_class_creation_1__metaclass.object );
    tmp_class_creation_1__metaclass.object = NULL;

    frame_module->f_lineno = tmp_tried_lineno_1;
    // Re-reraise as necessary after finally was executed.
    // Reraise exception if any.
    if ( exception_keeper_type_1 != NULL )
    {
        exception_type = exception_keeper_type_1;
        exception_value = exception_keeper_value_1;
        exception_tb = exception_keeper_tb_1;

        goto frame_exception_exit_1;
    }

    goto finally_end_1;
    finally_end_1:;
    tmp_called_2 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_main );

    if (unlikely( tmp_called_2 == NULL ))
    {
        tmp_called_2 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_main );
    }

    if ( tmp_called_2 == NULL )
    {

        exception_type = INCREASE_REFCOUNT( PyExc_NameError );
        exception_value = UNSTREAM_STRING( &constant_bin[ 24 ], 26, 0 );
        exception_tb = NULL;

        frame_module->f_lineno = 27;
        goto frame_exception_exit_1;
    }

    frame_module->f_lineno = 27;
    tmp_unused = CALL_FUNCTION_NO_ARGS( tmp_called_2 );
    if ( tmp_unused == NULL )
    {
        assert( ERROR_OCCURED() );

        PyErr_Fetch( &exception_type, &exception_value, (PyObject **)&exception_tb );


        frame_module->f_lineno = 27;
        goto frame_exception_exit_1;
    }
    Py_DECREF( tmp_unused );

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif
    popFrameStack();

    assertFrameObject( frame_module );
    Py_DECREF( frame_module );

    goto frame_no_exception_1;
    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_module );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( INCREASE_REFCOUNT( frame_module ) );
    }
    else if ( exception_tb->tb_frame != frame_module )
    {
        PyTracebackObject *traceback_new = (PyTracebackObject *)MAKE_TRACEBACK( INCREASE_REFCOUNT( frame_module ) );
        traceback_new->tb_next = exception_tb;
        exception_tb = traceback_new;
    }

    // Put the previous frame back on top.
    popFrameStack();

#if PYTHON_VERSION >= 340
    frame_module->f_executing -= 1;
#endif
    Py_DECREF( frame_module );

    // Return the error.
    goto module_exception_exit;
    frame_no_exception_1:;

    return MOD_RETURN_VALUE( module___main__ );
module_exception_exit:
    PyErr_Restore( exception_type, exception_value, (PyObject *)exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
// The main program for C++. It needs to prepare the interpreter and then
// calls the initialization code of the __main__ module.

#include "structseq.h"

#if 0
extern PyObject *const_str_plain_ignore;
#endif

#ifdef _NUITKA_WINMAIN_ENTRY_POINT
int __stdcall WinMain( HINSTANCE hInstance, HINSTANCE hPrevInstance, char* lpCmdLine, int nCmdShow )
{
    int argc = __argc;
    char** argv = __argv;
#else
int main( int argc, char *argv[] )
{
#endif
#ifdef _NUITKA_STANDALONE
    prepareStandaloneEnvironment();
#endif

    // Initialize Python environment.
    Py_DebugFlag = 0;
#if 0
    Py_Py3kWarningFlag = 0;
#endif
#if 0
    Py_DivisionWarningFlag =
#if 0
        Py_Py3kWarningFlag ||
#endif
        0;
#endif
    Py_InspectFlag = 0;
    Py_InteractiveFlag = 0;
    Py_OptimizeFlag = 0;
    Py_DontWriteBytecodeFlag = 0;
    Py_NoUserSiteDirectory = 0;
    Py_IgnoreEnvironmentFlag = 0;
#if 0
    Py_TabcheckFlag = 0;
#endif
    Py_VerboseFlag = 0;
#if 0
    Py_UnicodeFlag = 0;
#endif
    Py_BytesWarningFlag = 0;
#if 1
    Py_HashRandomizationFlag = 1;
#endif

    // We want to import the site module, but only after we finished our own
    // setup. The site module import will be the first thing, the main module
    // does.
    Py_NoSiteFlag = 1;

    // Initialize the embedded CPython interpreter.
    setCommandLineParameters( argc, argv, true );
    Py_Initialize();

    // Lie about it, believe it or not, there are "site" files, that check
    // against later imports, see below.
    Py_NoSiteFlag = 0;

    // Set the command line parameters for run time usage.
    setCommandLineParameters( argc, argv, false );

#ifdef _NUITKA_STANDALONE
    restoreStandaloneEnvironment();
#endif

    // Initialize the constant values used.
    _initBuiltinModule();
    _initConstants();
    _initBuiltinOriginalValues();

    // Revert the wrong sys.flags value, it's used by "site" on at least Debian
    // for Python3.3, more uses may exist.
#if 0 == 0
#if PYTHON_VERSION >= 330
    PyStructSequence_SetItem( PySys_GetObject( "flags" ), 6, const_int_0 );
#elif PYTHON_VERSION >= 320
    PyStructSequence_SetItem( PySys_GetObject( "flags" ), 7, const_int_0 );
#elif PYTHON_VERSION >= 260
    PyStructSequence_SET_ITEM( PySys_GetObject( (char *)"flags" ), 9, const_int_0 );
#endif
#endif

    // Initialize the compiled types of Nuitka.
    PyType_Ready( &Nuitka_Generator_Type );
    PyType_Ready( &Nuitka_Function_Type );
    PyType_Ready( &Nuitka_Method_Type );
    PyType_Ready( &Nuitka_Frame_Type );
#if PYTHON_VERSION < 300
    initSlotCompare();
#endif

    enhancePythonTypes();

    // Set the sys.executable path to the original Python executable on Linux
    // or to python.exe on Windows.
    PySys_SetObject(
        (char *)"executable",
        UNSTREAM_STRING( &constant_bin[ 435 ], 28, 0 )
    );

    patchBuiltinModule();
    patchTypeComparison();

    // Allow to override the ticker value, to remove checks for threads in
    // CPython core from impact on benchmarks.
    char const *ticker_value = getenv( "NUITKA_TICKER" );
    if ( ticker_value != NULL )
    {
        _Py_Ticker = atoi( ticker_value );
        assert ( _Py_Ticker >= 20 );
    }

#ifdef _NUITKA_STANDALONE
    setEarlyFrozenModulesFileAttribute();
#endif

    // Disable Python warnings if requested to.
#if 0
    // Should be same as:
    //   warnings.simplefilter("ignore", UserWarning)
    //   warnings.simplefilter("ignore", DeprecationWarning)
    // There is no C-API to control warnings. We don't care if it actually
    // works, i.e. return code of "simplefilter" function is not checked.
    {
        PyObject *warnings = PyImport_ImportModule( "warnings" );
        if ( warnings != NULL )
        {
            PyObject *simplefilter = PyObject_GetAttrString( warnings, "simplefilter" );

            if ( simplefilter != NULL )
            {
                PyObject *result1 = PyObject_CallFunctionObjArgs( simplefilter, const_str_plain_ignore, PyExc_UserWarning, NULL );
                Py_XDECREF( result1 );
                PyObject *result2 = PyObject_CallFunctionObjArgs( simplefilter, const_str_plain_ignore, PyExc_DeprecationWarning, NULL );
                Py_XDECREF( result2 );
            }
        }
    }
#endif

    // Execute the "__main__" module init function.
    MOD_INIT_NAME( __main__ )();

    if ( ERROR_OCCURED() )
    {
        // Cleanup code may need a frame, so put one back.
        PyThreadState_GET()->frame = MAKE_FRAME( codeobj_ae7d60acb34059627f4a268a1c024c6c, module___main__ );

        PyErr_PrintEx( 0 );
        Py_Exit( 1 );
    }
    else
    {
        Py_Exit( 0 );
    }

    // Dead code, just for the compiler to be happy. The above branches both
    // do Py_Exit() which is not supposed to return.
    assert(false);
    return 0;
}
