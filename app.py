# app.py
from flask import Flask, render_template
from flask import request

import pymysql

# DB 연동
db_conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1202',
    db = 'test',
    charset ='utf8'
)
print(db_conn)



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
    return render_template('posttest.html')

@app.route('/test',methods=['POST']) # 접속하는 url
def testpost():
    id = request.form['cid']
    pwd = request.form['password']
    print(id,pwd)
    return render_template('posttest.html')


@app.route('/sqltest')
def sqltest():
    # 커서 객체 생성
    cursor = db_conn.cursor()

    query = "select * from player"

    cursor.execute(query)

    result = []
    
    for i in cursor:
        print(i)
        temp = {'player_id':i[0],'player_name':i[1]}
        result.append(temp)
        
    return render_template('sqltest.html',result_table =result)



@app.route('/detail')
def detailtest():
    temp = request.args.get('id') 
    temp1 = request.args.get('name') 
    cursor = db_conn.cursor()
                                                            # sql 쿼리에서 작은따옴표 쿼리문에 넣으니까 넣어줘야 한다!
    query = "select * from player where player_id = {} and player_name like '{}'".format(temp,temp1)
    print(query)

    cursor.execute(query)
    print('333')
    result = []
    for i in cursor:   # i는 ('2012136', '오비나', 'K10', '', '', '', 'MF', 26, '', datetime.date(1990, 6, 3), '1', 169, 70) 들어옴
        temp = {'player_id':i[0],'player_name':i[1],'team_name':i[2],'height':i[-2],'weight':i[-1] }
        print('111')
        result.append(temp)
    return render_template('detail.html', result_table = result)




if __name__ == "__main__":
    app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1",port -"5000",debug=Ture)