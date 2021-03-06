from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# API 역할을 하는 부분
@app.route('/api/list', methods=['GET'])
def chart1_list():
    chart1 = list(db.geniekoreacrawl.find({}, {"_id":False}).sort('rank', 1))
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','msg':'list 연결되었습니다!', 'chart1_list': chart1});

@app.route('/api/like', methods=['POST'])
def chart1_like():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    title_receive = request.form["title_give"]
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    chart = db.geniekoreacrawl.find_one({"title": title_receive}, {"_id": False})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = chart["like"]+1
    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    db.geniekoreacrawl.update_one({"title": title_receive}, {'$set': {'like': new_like}})
    # 참고: '$set' 활용하기!
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg':'like!!'})

@app.route('/api/delete', methods=['POST'])
def chart1_delete():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    title_receive = request.form["title_give"]
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    chart = db.geniekoreacrawl.find_one({"title": title_receive}, {"_id": False})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = chart["like"]-1
    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    db.geniekoreacrawl.update_one({"title": title_receive}, {'$set': {'like': new_like}})
    # 참고: '$set' 활용하기!
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg':'ㅠㅠ'})

@app.route('/api/list2', methods=['GET'])
def chart2_list():
    chart2 = list(db.bugs_korea_crawl.find({}, {"_id":False}).sort('rank', 1))
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','msg':'list 연결되었습니다!', 'chart2_list': chart2});

@app.route('/api/like2', methods=['POST'])
def chart2_like():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    title_receive = request.form["title_give"]
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    chart = db.bugs_korea_crawl.find_one({"title": title_receive}, {"_id": False})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = chart["like"]+1
    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    db.bugs_korea_crawl.update_one({"title": title_receive}, {'$set': {'like': new_like}})
    # 참고: '$set' 활용하기!
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg':'like!!'})

@app.route('/api/delete2', methods=['POST'])
def chart2_delete():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    title_receive = request.form["title_give"]
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    chart = db.bugs_korea_crawl.find_one({"title": title_receive}, {"_id": False})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = chart["like"]-1
    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    db.bugs_korea_crawl.update_one({"title": title_receive}, {'$set': {'like': new_like}})
    # 참고: '$set' 활용하기!
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg':'ㅠㅠ'})

@app.route('/api/list3', methods=['GET'])
def chart3_list():
    chart3 = list(db.mellon_korea_crawl.find({}, {"_id":False}).sort('rank', 1))
    # 1. mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success','msg':'list 연결되었습니다!', 'chart3_list': chart3});

@app.route('/api/like3', methods=['POST'])
def chart3_like():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    title_receive = request.form["title_give"]
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    chart = db.mellon_korea_crawl.find_one({"title": title_receive}, {"_id": False})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = chart["like"]+1
    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    db.mellon_korea_crawl.update_one({"title": title_receive}, {'$set': {'like': new_like}})
    # 참고: '$set' 활용하기!
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg':'like!!'})

@app.route('/api/delete3', methods=['POST'])
def chart3_delete():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    title_receive = request.form["title_give"]
    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    chart = db.mellon_korea_crawl.find_one({"title": title_receive}, {"_id": False})
    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = chart["like"]-1
    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    db.mellon_korea_crawl.update_one({"title": title_receive}, {'$set': {'like': new_like}})
    # 참고: '$set' 활용하기!
    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg':'ㅠㅠ'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


