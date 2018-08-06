from functools import wraps
from flask import g
from ..models import Permission
from .errors import forbidden

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*nkwargs, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return f(*nkwargs, **kwargs)
        return decorated_function
    return decorator
