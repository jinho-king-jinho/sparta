from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta


@app.route('/')
def home():
    return render_template('4.6homework.html')


@app.route('/orders', methods=['POST'])
def write_order():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'number': number_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)
    return jsonify({'order': 'success', 'msg': '이 요청은 POST'})


@app.route('/orders', methods=['GET'])
def read_order():
    orders_read = list(db.orders.find({}, {'_id': False}))

    return jsonify({'result': 'success', 'orders': orders_read})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
