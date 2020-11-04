from flask import Flask#render_template
import pymysql as mysql
from flask_cors import CORS
import json
app = Flask(__name__)

#day_records=Blueprint('day_records',__name__)
CORS(app, resources={r'/*': {'origins': '*'}}) #适用于全局的API接口配置

mysql_conn = mysql.Connect(host='localhost', user='root', password='root', charset='utf8',cursorclass=mysql.cursors.DictCursor)
mysql_cursor = mysql_conn.cursor()
mysql_cursor.execute('use student')
sql = 'select * from studentinfo'
mysql_cursor.execute(sql)
studentinfo = mysql_cursor.fetchall()
mysql_conn.close()

@app.route("/",methods=["GET"])         
def index():
    print(studentinfo)
    return json.dumps(studentinfo,ensure_ascii=False)
if __name__ == '__main__':
    app.run()