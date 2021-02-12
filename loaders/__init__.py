import os

CWD = os.path.abspath(os.path.dirname(__file__))
CONTEXT_DIR = os.path.abspath(os.path.join(CWD, '../jsonld-context/html'))

LD_10_DIR = os.path.join(CONTEXT_DIR, 'jsonld_10')
LD_11_DIR = os.path.join(CONTEXT_DIR, 'jsonld_11')
CONTEXT_SVR = 'http://localhost:8000/jsonld_11/'
CONTEXT_SSL_SVR = 'https://localhost:8443/jsonld_11/'