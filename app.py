from flask import Flask, render_template, session

app = Flask(__name__)

menu_items = [
    {'id': 1, 'name': 'Margherita Pizzas', 'description': 'Classic cheese and tomato pizza.', 'price': 8.5},
    {'id': 2, 'name': 'Veggie Burger', 'description': 'Grilled veggie patty with lettuce and tomato.', 'price': 7.0},
    {'id': 3, 'name': 'Caesar Salad', 'description': 'Crisp romaine with Caesar dressing.', 'price': 6.5}
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