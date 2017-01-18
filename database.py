import sqlite3
import time
import datetime

conn = sqlite3.connect('Database.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE Huizen(Naam VARCHAR, Locatie VARCHAR, Camera VARCHAR, Noodknop VARCHAR)")
    c.execute("CREATE TABLE Esmeralda(Camera VARCHAR, Noodknop VARCHAR)")
    c.execute("CREATE TABLE Thomas(Camera VARCHAR, Noodknop VARCHAR)")
def enter_data():
    c.execute("INSERT INTO Huizen (Naam,Locatie,Noodknop) VALUES('Esmeralda','Vromaadweg 28, 1987 Haarlem','UIT')")
    c.execute("INSERT INTO Huizen (Naam,Locatie,Noodknop) VALUES('Thomas','Kerkweg 13, 2587 Groningen','AAN')")
    conn.commit()


def read_from_database():
    sql= "SELECT * FROM Huizen"
    nood= "SELECT * FROM Huizen WHERE Noodknop='AAN'"
    for row in c.execute(sql):
        print(row)

    for row in c.execute(nood):
        print(row)

def movement_esmeralda():
    currtime=str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M"))
    c.execute("INSERT INTO Esmeralda (Camera) VALUES(?)",(currtime,))
    c.execute("UPDATE Huizen SET Camera=? WHERE Naam='Esmeralda'",(currtime,))
    conn.commit()

def movement_thomas():
    currtime=str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M"))
    c.execute("INSERT INTO Thomas (Camera) VALUES(?)",(currtime,))
    c.execute("UPDATE Huizen SET Camera=? WHERE Naam='Thomas'",(currtime,))
    conn.commit()

def noodknop_esmeralda():
    currtime=str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M"))
    c.execute("INSERT INTO Esmeralda (Noodknop) VALUES(?)",(currtime,))
    c.execute("UPDATE Huizen SET Noodknop='AAN' WHERE Naam='Esmeralda'")
    conn.commit()
def noodknop_thomas():
    currtime=str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M"))
    c.execute("INSERT INTO Thomas (Noodknop) VALUES(?)",(currtime,))
    c.execute("UPDATE Huizen SET Noodknop='AAN' WHERE Naam='Thomas'")
    conn.commit()

def nood_verholpen():
    naam=input('Wie is de eigenaar van de noodknop die uitgeschakelt dient te worden?')
    c.execute("UPDATE Huizen SET Noodknop='UIT' WHERE Naam=?", (naam,))
    conn.commit()


conn.close()
