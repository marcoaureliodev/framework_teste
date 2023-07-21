from functools import wraps

tokens = {
    "Framework",
    "MarcoMachado"
}
def auth_required(headers):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if 'X-API-KEY' in headers.headers:
                if headers.headers['X-API-KEY'] in tokens:
                    result = function(*args, **kwargs)
                    return result
                raise Exception('Not Authorization')
            raise Exception('Required Authorization')

        return wrapper
    return decorator
