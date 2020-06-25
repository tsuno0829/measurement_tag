from flask import *

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def root():
    return make_response(jsonify({'success':'success'}),200)
    # make_responseでHTTPレスポンス作れる。make_response(json,ステータスコード)

@app.route('/1', methods = ['GET'])
def optional():

    # URL末尾のIDを受け取って、IDに対応するデータを取ってきたりする
    return make_response(jsonify({'ID': 1}, 200))

@app.route('/', methods = ['POST'])
def post():
    # POSTリクエストが来たら404エラーを返してみる
    return make_response(jsonify({'error':'Does not support POST method'}),404)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)