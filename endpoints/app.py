import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/guest")
def guest_page():
    return render_template('guest_pass.html')

@app.route("/home")
def home_page():
    return render_template('index.html')

@app.route("/create")
def create_guest_page():
    return render_template('create_guest.html')

@app.route("/delivery")
def delivery_page():
    return render_template('delivery.html')

@app.route("/parking")
def parking_page():
    return render_template('parking.html')

@app.route("/concierge_panel")
def concierge_panel_page():
    return render_template('concierge_panel.html')

if __name__ == "__main__":  # <-- also fix here!
    app.run(debug=True)