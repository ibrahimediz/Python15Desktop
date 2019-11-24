import sqlite3 as sql

class DB():
    def __init__(self):
        self.baglan()


    def baglan(self):
        self.db = sql.connect(r"DB\FACEDET.db")
        self.cur = self.db.cursor()

    def ekleme(self,yazi="Boş Geldi"):
        try:
            query = " INSERT INTO PYQTDENEME (YAZI) VALUES ('{}')"
            query = query.format(yazi)
            self.cur.execute(query)
            self.db.commit()
            return True
        except:
            return False
        finally:
            self.db.close()
        
    def ilListele(self):
        try:
            self.baglan()
            query =""" SELECT 
                IL_ID,IL_ADI 
                FROM ST_ILLER"""
            self.cur.execute(query)
            return self.cur.fetchall()
        except Exception as hata:
            liste = []
            liste.append((1,hata))
            return liste
        finally:
            self.db.close()
        
 

