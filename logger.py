import logging
import datetime

def log_proc_call(log_path):
    logging.basicConfig(filename=log_path, level=logging.INFO, filemode='w')
    def lpc_decorator(proc):
        def lpc_main(*args, **kwargs):
            call_time = datetime.datetime.now()
            proc_call_descr = f'{call_time}: function {proc.__name__} called from module {proc.__module__} with args = {args} and kwargs = {kwargs}'
            logging.info(proc_call_descr)
            try:
                result = proc(*args, **kwargs)
            except Exception as e:
                logging.info(f'function terminated with {e.__class__.__name__}: {e}')
                raise e

            logging.info(f'returned value = {result}')
            return result
        return lpc_main
    return lpc_decorator


@log_proc_call('log.txt')
def foo(x):
    return (x - 5) * 2 + 8

if __name__ == '__main__':
    foo(6)
    foo(8)
    foo('s')


