# app.py
from flask import Flask, render_template
from flask import request

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/main') # 접속하는 url

def index():
    #return "안녕하세요"
    
    temp = request.args.get('uid')
    temp1 = request.args.get('cid')
    
    print(temp,temp1)
    
    return render_template('index.html')



@app.route('/test') # 접속하는 url

def test():
    #return "안녕하세요"
    return render_template('test.html')


if __name__ == "__main__":
    app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1",port -"5000",debug=Ture)