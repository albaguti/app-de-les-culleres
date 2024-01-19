import sqlite3
import datetime

def save_data(dia: datetime,
            hores: float,
            cites: int,
            nens: bool,
            hores_de_son: float,
            qualitat:str,
            estat:int,
            despertat: int,
            benestar: list):
   try:
       conn = sqlite3.connect('culleres.db')
       cur = conn.cursor()
       sql = """
       INSERT INTO estat (timestamp, hores_treballades, cites, nens, hores_de_son, qualitat_del_son, estat, despertat, benestar)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
       """
       params = (dia, hores, cites, nens, hores_de_son, qualitat, estat, despertat, ",".join(benestar))
       cur.execute(sql, params)
       conn.commit()
   except sqlite3.Error as e:
       print(f"An error occurred: {e}")
   finally:
       if conn:
           conn.close()
