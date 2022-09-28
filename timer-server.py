# Import flask and datetime module for showing date and time 
from flask import Flask
import datetime

x =  datetime.datetime.now()

# Initialize flask app
app = Flask(__name__)

# Route for seeing data
@app.route('/data')
def get_time():

	 # Returning an api for showing in  reactjs
    return {
        'Name':"wilde", 
        "Age":"84",
		"Date":x, 
		"System":"iMac",
        "Programming":"python"
        }
  
		# Running app
if __name__ == '__main__':
	app.run(debug=True)