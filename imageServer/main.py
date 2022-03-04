import sys
from bottle import run, default_app



import controller
#-----------------------------------------------------------------------------

# It might be a good idea to move the following settings to a config file and then load them
# Change this to your IP address or 0.0.0.0 when actually hosting
host = ''

# Test port, change to the appropriate port to host
port = 8080

# Turn this off for production
debug = True

# Turn this off for production
reloader = True






run(host=host, port=port, debug=debug)