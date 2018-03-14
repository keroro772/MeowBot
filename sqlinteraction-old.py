import sqlite3
# import pymysql
# import pymysql.cursors

#conn = pymysql.connect(user='Dukekero', password='', host='Dukekero.mysql.pythonanywhere-services.com', database='Dukekero$cookies')
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def check_in_db(name):
    c.execute('SELECT currentAmount FROM Catnip_catnip WHERE name=?', (name,))
    data=c.fetchone()
    if data is None:
        return None
    else:
        return data[0]

def gettotal():
    c.execute('SELECT name FROM Catnip_catnip ORDER BY amount ASC')
    data = c.fetchall()
    data = list(data)
    y = []
    for x in data:
        y.append(x[0])
    return y

def gettotalcatnip():
    c.execute('SELECT currentAmount FROM Catnip_catnip ORDER BY currentAmount ASC')
    data = c.fetchall()
    data = list(data)
    y = 0
    for x in data:
        y += x[0]
    return y

def deta_entry_add(name, addcatnip):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute('SELECT amount FROM Catnip_catnip WHERE name=?', (name,))
    data = c.fetchone()
    if data is None:
        c.execute('INSERT INTO Catnip_catnip (name, amount, currentAmount) VALUES (?, ?, ?)', (name, addcatnip, addcatnip))
        conn.commit()
    else:
        c.execute('UPDATE Catnip_catnip SET amount=amount + ?, currentAmount=currentAmount + ? WHERE name=?',(addcatnip,addcatnip,name))
        conn.commit()
    c.close()
    conn.close()

def deta_entry_del(name, delcatnip):
    c.execute('SELECT amount, currentAmount FROM Catnip_catnip WHERE name=?', (name,))
    data=c.fetchall()
    if data is None:
        pass
    else:
        c.execute('UPDATE Catnip_catnip SET currentAmount=currentAmount - ? WHERE name=?',(delcatnip,name))
        conn.commit()

def read_from_db(name):
    data = check_in_db(name)
    if data is None:
        return 0
    else:
        c.execute('SELECT CurrentAmount FROM Catnip_catnip WHERE name=?', (name,))
        data = c.fetchone()
        return data[0]

def getnamefromid(id):
    c.execute('SELECT name FROM throwthursday_throw WHERE id=?', (id,))
    data = c.fetchone()
    return data

def get_clip_from_id(id):
    c.execute('SELECT link FROM command_clip WHERE id=?', (id,))
    data = c.fetchone()
    if data is None:
        return None
    else:
        return data[0]

def get_all_clips():
    c.execute('SELECT link FROM command_clip')
    data = c.fetchall()
    if data is None:
        return None
    else:
        return data

def get_id_from_clip(clip):
    c.execute('SELECT id FROM command_clip WHERE link=?', (str(clip),))
    data = c.fetchall()
    if data is None:
        return None
    else:
        return data

def get_name_from_id(id):
    c.execute('SELECT name FROM command_clip WHERE id=?', (str(id),))
    data = c.fetchall()
    if data is None:
        return None
    else:
        return data