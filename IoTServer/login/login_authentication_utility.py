from flask import abort, g


# def authentication(func):
#     def wrapper(*args, **kwargs):
#         if g.username == 'admin' and g.password == '123':
#             return func(*args, **kwargs)
#         else:
#             abort(401)
#
#     return wrapper
