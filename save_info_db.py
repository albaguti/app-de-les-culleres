import sqlite3
import datetime

def save_data(dia: datetime.date, hores: float, cites: int, nens: bool, hores_de_son: float, qualitat:int, estat:int):
    conn = sqlite3.connect('culleres.db')
    cur = conn.cursor()
    sql = "INSERT INTO estat (timestamp, hores_treballades, cites, nens, hores_de_son, qualitat_del_son) VALUES (?, ?, ?, ?, ?, ?)"
    params = (dia, hores, cites, nens, estat, hores_de_son, qualitat)
    cur.execute(sql, params)
    conn.commit()
    conn.close()
    pass
