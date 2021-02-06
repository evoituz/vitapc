import os

DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE', 'LOCAL')

if DEVELOPMENT_MODE == 'PRODUCTION':
    from .prod import *
# elif DEVELOPMENT_MODE == 'DEVELOPER':
#     from .develope import *
else:
    from .locale import *

