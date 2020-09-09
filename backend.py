import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer , isbn integer)")
    conn.commit()
    conn.close()

#insert(feed) the data related to book....
def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)" , (title,author,year,isbn))
    conn.commit()
    conn.close()
    view()

#view all the rows and columns of the data....
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

#fetching the information from data using search....
def search(title="" , author="" , year="" , isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?" , (title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

#delete the item as per the command from listbox....
def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?" , (id,))
    conn.commit()
    conn.close()
    

#update the listbox....
def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?" , (title,author,year,isbn,id))
    conn.commit()
    conn.close()
    


connect() 