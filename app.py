from flask import Flask, render_template

app = Flask(__name__)

menu_items = [
    {'id': 1, 'name': 'Margherita Pizza', 'description': 'Classic cheese and tomato pizza.', 'price': 8.5},
    {'id': 2, 'name': 'Veggie Burger', 'description': 'Grilled veggie patty with lettuce and tomato.', 'price': 7.0},
    {'id': 3, 'name': 'Caesar Salad', 'description': 'Crisp romaine with Caesar dressing.', 'price': 6.5}
]

@app.route('/')
def home():
    return render_template('home.html', menu=menu_items)

if __name__ == '__main__':
    app.run(debug=True)