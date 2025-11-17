from flask import jsonify
from functools import wraps
from Base.ApiResponse import ApiResponse

def route(bp,*args,**kwargs):
    def decorator(f):
        @bp.route(*args,**kwargs)
        @wraps(f)
        def wrapper(*args,**kwargs):
            result = f(*args,**kwargs)
            res = ApiResponse(result)
            return jsonify(res.body())
        return f
    return decorator