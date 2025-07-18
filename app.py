from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

menu_items = [
    {'id': 1, 'name': 'Spaghetti Carbonara', 'description': 'Creamy egg-based sauce with pancetta, black pepper, and Parmesan.', 'price': 9.5},
    {'id': 2, 'name': 'Penne Arrabbiata', 'description': 'Spicy tomato sauce with garlic, chili flakes, and parsley.', 'price': 8.0},
    {'id': 3, 'name': 'Fettuccine Alfredo', 'description': 'Rich and creamy sauce with butter and Parmesan.', 'price': 9.0},
    {'id': 4, 'name': 'Lasagna Bolognese', 'description': 'Layered pasta with beef ragu, béchamel, and mozzarella.', 'price': 10.5},
    {'id': 5, 'name': 'Linguine Pesto Genovese', 'description': 'Fresh basil pesto with pine nuts and Parmesan.', 'price': 8.5},
    {'id': 6, 'name': 'Tortellini alla Panna', 'description': 'Cheese-filled tortellini in a creamy ham sauce.', 'price': 9.2},
    {'id': 7, 'name': 'Tagliatelle Funghi', 'description': 'Mushroom medley in a garlic cream sauce.', 'price': 9.8},
    {'id': 8, 'name': 'Gnocchi Sorrentina', 'description': 'Potato gnocchi baked with tomato sauce and mozzarella.', 'price': 8.9}
]

@app.route('/')
def home():
    basket = session.get('basket', [])
    basket_items = [item for item in menu_items if item['id'] in basket]
    total = sum(item['price'] for item in basket_items)
    return render_template('home.html', menu=menu_items,basket=basket_items, total=total)


@app.route('/add/<int:item_id>', methods=['POST'])
def add_to_basket(item_id):
    if 'basket' not in session:
        session['basket'] = []
    session['basket'].append(item_id)
    session.modified = True
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)