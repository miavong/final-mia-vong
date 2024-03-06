from flask import Flask, render_template, request

import functions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("result.html")

@app.route("/submit_result", methods=['GET', 'POST'])
def submit_result():
    if request.method == "POST":
        plant_name = request.form["plant_name"]
        plants = functions.extract_plant_data(plant_name)
        if plants:
            return render_template("result.html", plants=plants, error_message=None)
        else:
            error_message = f"Sorry, the plant '{plant_name}' does not exist in our system."
            return render_template("result.html", plants=None, error_message=error_message)
    
if __name__ == '__main__':
    app.run(debug=True)