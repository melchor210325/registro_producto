
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

sales = []
total_sales = 0.0

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', sales=sales, total_sales=total_sales)

@app.route('/add-sale', methods=['POST'])
def add_sale():
    product = request.form['product']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    total = quantity * price

    sale = {
        'product': product,
        'quantity': quantity,
        'price': price,
        'total': total
    }
    sales.append(sale)

    global total_sales
    total_sales += total

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

