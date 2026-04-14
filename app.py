"""T-Shirt Store – a simple Flask web application for selling T-shirts."""

from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "change-me-before-production"

# ---------------------------------------------------------------------------
# Sample product catalogue
# ---------------------------------------------------------------------------
PRODUCTS = [
    {
        "id": 1,
        "name": "Classic White Tee",
        "price": 19.99,
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400",
        "description": "A timeless white cotton T-shirt that goes with everything.",
        "sizes": ["S", "M", "L", "XL"],
        "colors": ["White"],
    },
    {
        "id": 2,
        "name": "Urban Black Tee",
        "price": 24.99,
        "image": "https://images.unsplash.com/photo-1503341455253-b2e723bb3dbb?w=400",
        "description": "Sleek black T-shirt for a cool urban look.",
        "sizes": ["S", "M", "L", "XL", "XXL"],
        "colors": ["Black"],
    },
    {
        "id": 3,
        "name": "Ocean Blue Tee",
        "price": 22.99,
        "image": "https://images.unsplash.com/photo-1562157873-818bc0726f68?w=400",
        "description": "Refreshing ocean-blue T-shirt made from organic cotton.",
        "sizes": ["S", "M", "L"],
        "colors": ["Blue"],
    },
    {
        "id": 4,
        "name": "Sunset Orange Tee",
        "price": 21.99,
        "image": "https://images.unsplash.com/photo-1529374255404-311a2a4f1fd9?w=400",
        "description": "Vibrant orange tee inspired by summer sunsets.",
        "sizes": ["M", "L", "XL"],
        "colors": ["Orange"],
    },
    {
        "id": 5,
        "name": "Forest Green Tee",
        "price": 23.99,
        "image": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=400",
        "description": "Nature-inspired green T-shirt, soft and breathable.",
        "sizes": ["S", "M", "L", "XL"],
        "colors": ["Green"],
    },
    {
        "id": 6,
        "name": "Vintage Grey Tee",
        "price": 20.99,
        "image": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=400",
        "description": "Comfortable vintage-wash grey tee with a relaxed fit.",
        "sizes": ["S", "M", "L", "XL", "XXL"],
        "colors": ["Grey"],
    },
]


def _get_product(product_id: int) -> dict | None:
    """Return a product dict by its id, or None."""
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def home():
    """Landing page showcasing featured products."""
    featured = PRODUCTS[:3]
    return render_template("home.html", featured=featured)


@app.route("/products")
def products():
    """Full product listing."""
    return render_template("products.html", products=PRODUCTS)


@app.route("/product/<int:product_id>")
def product_detail(product_id: int):
    """Detail page for a single product."""
    product = _get_product(product_id)
    if product is None:
        return redirect(url_for("products"))
    return render_template("product_detail.html", product=product)


@app.route("/cart")
def cart():
    """Display the shopping cart."""
    cart_items = session.get("cart", [])
    enriched: list[dict] = []
    total = 0.0
    for item in cart_items:
        product = _get_product(item["product_id"])
        if product:
            subtotal = product["price"] * item["quantity"]
            total += subtotal
            enriched.append({
                "product": product,
                "size": item["size"],
                "quantity": item["quantity"],
                "subtotal": round(subtotal, 2),
            })
    return render_template("cart.html", items=enriched, total=round(total, 2))


@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():
    """Add a product to the session-based cart."""
    product_id = int(request.form["product_id"])
    size = request.form.get("size", "M")
    quantity = int(request.form.get("quantity", 1))

    cart_items: list[dict] = session.get("cart", [])

    # If already in cart with same size, bump quantity
    for item in cart_items:
        if item["product_id"] == product_id and item["size"] == size:
            item["quantity"] += quantity
            break
    else:
        cart_items.append({
            "product_id": product_id,
            "size": size,
            "quantity": quantity,
        })

    session["cart"] = cart_items
    return redirect(url_for("cart"))


@app.route("/remove-from-cart/<int:index>")
def remove_from_cart(index: int):
    """Remove an item from the cart by its list index."""
    cart_items: list[dict] = session.get("cart", [])
    if 0 <= index < len(cart_items):
        cart_items.pop(index)
        session["cart"] = cart_items
    return redirect(url_for("cart"))


@app.route("/checkout")
def checkout():
    """Simple checkout / thank-you page."""
    cart_items = session.get("cart", [])
    if not cart_items:
        return redirect(url_for("products"))
    total = 0.0
    for item in cart_items:
        product = _get_product(item["product_id"])
        if product:
            total += product["price"] * item["quantity"]
    return render_template("checkout.html", total=round(total, 2))


@app.route("/place-order", methods=["POST"])
def place_order():
    """Clear the cart and show an order-confirmation page."""
    session.pop("cart", None)
    return render_template("order_confirmation.html")


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
