from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return "Hello world!"

@app.route('/order')
def show_orders():
    return render_template('index.html', title='List of Orders', orders=orders)

@app.route('/order/<int:order_id>')
def show_one_order(order_id):
    order = orders[order_id]
    return render_template('order.html', title=f'Order no: {order_id}', order=order, orders=orders)

#