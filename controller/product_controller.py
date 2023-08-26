from app import app

@app.route("/product/add")
def add_product():
    return "This route is for adding products"