from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {"name": "Phone", "price": 200},
    {"name": "Laptop", "price": 800},
    {"name": "Mouse", "price": 20},
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = products

    if request.method == "POST":
        max_price = int(request.form["price"])
        result = [p for p in products if p["price"] <= max_price]

    return render_template("filter.html", products=result)

if __name__ == "__main__":
    app.run(debug=True)
