# TeeShop – T-Shirt Sales Website

A simple T-shirt e-commerce website built with **Python / Flask**, **HTML (Jinja2)** and **CSS**.

## Features

- 🏠 **Home page** with hero banner and featured products
- 👕 **Product catalogue** – browse all T-shirts
- 🔍 **Product detail** – choose size & quantity, add to cart
- 🛒 **Shopping cart** – view, update, and remove items (session-based)
- 💳 **Checkout** – enter shipping details and place an order
- 📱 **Responsive design** – works on desktop and mobile

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Project Structure

```
├── app.py                  # Flask application & routes
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # Stylesheet
├── templates/
│   ├── base.html           # Base layout (navbar + footer)
│   ├── home.html           # Landing page
│   ├── products.html       # All products listing
│   ├── product_detail.html # Single product view
│   ├── cart.html           # Shopping cart
│   ├── checkout.html       # Checkout form
│   └── order_confirmation.html
└── README.md
```

## Gałęzie / Branches

| Gałąź / Branch | Cel / Purpose |
|---|---|
| `main` | Główna gałąź produkcyjna / Main production branch |
| `copilot/track-code-changes` | Gałąź do śledzenia wszystkich zmian w kodzie / Branch for tracking all code changes |
