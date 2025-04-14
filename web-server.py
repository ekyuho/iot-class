import json
from flask import Flask, request
app = Flask(__name__)


@app.route("/send", methods=['GET', 'POST'])
def bus():
    if request.method == 'GET':
        r='<H3>GET Method </H3>'
        r+='서버는 다음과 같은 GET 파라미터값을 받았습니다<p>'
        r+= json.dumps(request.args, indent=4, ensure_ascii=False)
        return r

    if request.method == 'POST':
        r='POST Method\n'
        r+='서버는 다음과 같은 GET 파라미터값을 받았습니다\n'
        r+= json.dumps(request.args, indent=4, ensure_ascii=False) + '\n'
        r+='서버는 다음과 같은 POST 데이타를 받았습니다\n'
        r+= json.dumps(request.json, indent=4, ensure_ascii=False)
        return r


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
