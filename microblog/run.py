#!flask/bin/python3

##The shebang above defines the route to the python 
#	version to use

##To start the app, remember to indicate that this file
#	is an executable file: chmod a+x run.py

##Remember: 127.0.0.1:5000 or localhost:5000

from my_app import app
app.run(debug=True)
