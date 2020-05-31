import json
import db
from functions import *

with open('config.json', 'r') as f:
    config = json.load(f)

connection = db.db(
    host=config['DATABASE']['HOST'],
    username=config['DATABASE']['USERNAME'],
    password=config['DATABASE']['PASSWORD'],
    database=config['DATABASE']['DB_NAME']
)

insert_query = """INSERT INTO
                    speed_log(upload_speed,download_speed,latency,ip,isp,url)
                VALUES
                    (%s,%s,%s,%s,%s,%s)
"""
results = testSpeed()
connection.execute(query=insert_query, bindings=(
    round(results['upload']/(10 ** 6), 2), round(results['download']/(10 ** 6), 2), round(results['ping'], 2), results['client']['ip'], results['client']['isp'], results['share']))
# printDict(results)
