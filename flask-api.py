from flask import Flask, request

# Create a Flask application
app = Flask("george")

# Define a route for the root URL '/'
@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/cars/george', methods=['GET'])
def motorsg():
    return "Hello, subaru, torino, toyota, seat, renault, citroen"

@app.route('/cars', methods=['GET','POST'])
def cars():
    if request.method == "GET":
        return "mazda, hyundai, honda"
    elif request.method == "POST":
        return "creating new car"


@app.route('/motors', methods=['GET','POST'])
def motors():
    if request.method == "GET":
        return "royal, yamaha"
    elif request.method == "POST":
        return "creating new car"


# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5010)