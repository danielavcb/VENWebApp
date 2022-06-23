from flask import Flask, render_template

# initializing application
app = Flask(__name__)

# run application
if __name__ == '__main__' :
    # if any files are changed, the app will automatically
    # refresh itself to adapt 
    app.run(debug = True, port = 8000)

# ---------------------- ROUTES --------------------------
# main tab
@app.route("/main", method = ['GET', 'POST'])
def main():
    return render_template('main.html', title='Main')

# data tab
@app.route("/data")
def data():
    return "data"

# about us tab
@app.route("/about_us")
def about_us():
    return "about us"
