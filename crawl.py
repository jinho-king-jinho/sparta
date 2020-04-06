from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.


target = list(db.movies.find({'title':'어벤져스: 엔드게임'},{'_id':None}))
# print(target[0]['star'])



# same_star = db.movies.find({'star':target[0]['star']})
# list를 만들어야하는이유.!!
same_star = list(db.movies.find({'star':'9.38'}, {'_id':False}))
# print(same_star)


# for movie in same_star :
#     print(movie['title'])

#for 문을 써야하는 이유

db.movies.update_many({'star': '0.00'}, {'$set':{'star':'9.38'}})
