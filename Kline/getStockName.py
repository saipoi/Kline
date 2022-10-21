#将股票名插入到数据库中


#导入tushare mysql
import tushare as ts
import database_connection
from sqlalchemy import create_engine

# 初始化pro接口
pro = ts.pro_api('f558cbc6b24ed78c2104e209a8a8986b33ec66b7c55bcfa2f46bc108')
engine = create_engine('mysql+pymysql://root:qwer12345@23.94.43.9:3306/stock?charset=utf8')


def getname():
    # 拉取数据
    df = pro.stock_basic(**{
        "ts_code": "",
        "name": "",
        "exchange": "",
        "market": "",
        "is_hs": "",
        "list_status": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "symbol",
        "name"
    ])
    return df


def createtable():
    db = database_connection.MySQLDb()
    sql = "CREATE TABLE `stockname` ( 'index' varchar(10) , `symbol` varchar(10) COMMENT '股票代码', `name` varchar(10) COMMENT '日期', " \
          "PRIMARY KEY (`symbol`) ) ENGINE = InnoDB DEFAULT CHARSET=utf8; "
    db.commit_data(sql)


def insertinfo():
    con = engine.connect()
    df = getname()
    df.to_sql(name='stockname', con=con, if_exists='fail')
    con.close()


def getname(symbol):
    con = engine.connect()
