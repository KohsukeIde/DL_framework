is_simple_core = False


if is_simple_core:
    from dlscratch.core_simple import Variable
    from dlscratch.core_simple import Function
    from dlscratch.core_simple import using_config
    from dlscratch.core_simple import no_grad
    from dlscratch.core_simple import as_array
    from dlscratch.core_simple import as_variable
    from dlscratch.core_simple import setup_variable
    
else:
    from dlscratch.core import Variable
    from dlscratch.core import Function
    from dlscratch.core import using_config
    from dlscratch.core import no_grad
    from dlscratch.core import as_array
    from dlscratch.core import as_variable
    from dlscratch.core import setup_variable
    
    import dlscratch.functions
    import dlscratch.utils
    
setup_variable()