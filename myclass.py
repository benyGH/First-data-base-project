import sqlite3



class Contact():
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''create table if not exists 
                         Contacts( ID integer primary key,fname text , lname text , city text , tel integer )''')
        self.con.commit()
    def insert(self, fname , lname , city , tel):
        self.cur.execute('''insert into Contacts values( NULL , ? , ? , ? , ? )
                         ''' , (fname , lname , city , tel))    
        self.con.commit()

    def remove(self,id):
        self.cur.execute("delete from Contacts where ID = ?" , (id,))
        self.con.commit()

    def update(self,id,fname,lname,city,tel):
        self.cur.execute('''  
    update Contacts set fname = ?, lname= ?, city = ? , tel = ? where id = ?
    '''  , (fname , lname , city , tel , id))
        self.con.commit()
    def search(self,name):
        self.cur.execute('select * from Contacts where id = ? or fname = ? or lname = ? or city = ? or tel = ?'  , (name , name , name ,name , name))
        fe = self.cur.fetchall()
        return fe        

    
    def fetch(self):
        self.cur.execute("SELECT * from Contacts")
        fetch = self.cur.fetchall()
        return fetch


