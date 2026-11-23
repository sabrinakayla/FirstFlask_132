from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = ""
    if request.method == "POST":
        nama_input = request.form.get("nama_input", "").strip()
        if nama_input:
            hasil = f"Halo, {nama_input}! Data berhasil dikirim via POST."
    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)