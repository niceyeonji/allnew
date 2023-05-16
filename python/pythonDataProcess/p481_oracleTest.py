import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir="/usr/local/OracleXE/instantclient_19_19")

import matplotlib.pyplot as plt
from pandas import Series

plt.rc('font', family="AppleGothic")

conn = None
cur = None

try:
    loginfo = 'hr/1234@192.168.1.150:1521/xe'
    conn = cx_Oracle.connect(loginfo)
    cur = conn.cursor()

    sql = 'select * from country_summary_top_10'
    cur.execute(sql)

    data = []
    country = []

    for result in cur:
        data.append(result[1])
        country.append(result[0])
    mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#fff0f0', '#ccffbb', '#05ccFF', '#11ccff']

    charData = Series(data, index=country)
    charData.plot(kind='bar', rot=18, grid=False, title='범죄 빈도 Top 10 국가', color=mycolor, alpha=0.7)

    plt.ylabel('빈도 수', rotation=0)
    filename = 'oracleChart01.png'
    plt.savefig(filename, dpi=400, bbox_inches='tight')
    print(filename + ' file saved...')

    plt.show()

    myframe = pd.read_sql(sql, conn, index_col="COUNTRY_TXT")
    print(type(myframe))
    print(myframe)

except Exception as err:
    print(err)

finally:
    if cur != None:
        cur.close()

    if conn != None:
        conn.close()
print('finished')