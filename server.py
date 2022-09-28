from flask import Flask

app = Flask(__name__)

# Members API Route

@app.route("/members")
def numbers():
	return {"members": ["Oscar", "Wilde", "Socrates", "Pluto", "Joker", "Jules"]}

if __name__ == "__main__":
	app.run(debug=True)