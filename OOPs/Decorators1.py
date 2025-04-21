import logging

def log_function_call(fun):
    def decorated(*args,**kwargs):
        logging.info(f"Calling {fun.__name__}with args={args},kwargs={kwargs}")

        result=fun(*args,**kwargs)
        logging.info(f"{fun.__name__}retured{result}")

        return result
    return decorated
@log_function_call
def my_function(a,b):
    return a+b