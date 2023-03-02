is_simple_core = True

if is_simple_core:
    from dlscratch.core_simple import Variable
    from dlscratch.core_simple import Function
    from dlscratch.core_simple import using_config
    from dlscratch.core_simple import no_grad
    from dlscratch.core_simple import as_array
    from dlscratch.core_simple import as_variable
    from dlscratch.core_simple import setup_variable

setup_variable()