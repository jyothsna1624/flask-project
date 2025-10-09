from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# optional: resume download route (you can also link directly to static)
@app.route("/resume")
def resume():
    return send_from_directory("static/resume", "Jyothsna_CV.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
