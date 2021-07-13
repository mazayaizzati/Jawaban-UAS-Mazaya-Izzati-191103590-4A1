#!/usr/bin/env python
# coding: utf-8

# In[6]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

if db.is_connected():
    print("Berhasil terhubung ke database")


# In[16]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE db_film")

print("Database berhasil dibuat!")


# In[18]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = """CREATE TABLE tblFilm (
    kode_id INT AUTO_INCREMENT PRIMARY KEY,
    JudulFilm VARCHAR(255),
    Jenis_Film Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel Film berhasil dibuat!")


# In[22]:


import mysql.connector 

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "INSERT INTO tblfilm (JudulFilm, Jenis_Film) VALUES(%s,%s)"
val = ("X-Men: Dark Phoenix", "Action")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))


# In[23]:


import mysql.connector 

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "INSERT INTO tblfilm (JudulFilm, Jenis_Film) VALUES(%s, %s)"
values = [
    ("Aladdin", "Fantasy"),
    ("Godzilla II: King of Monsters","Fantasy"),
    ("John Wick: Chapter 3 - Parabellum","Action")
]

for val in values:
    cursor.execute(sql, val)
    db.commit()
    
print("{} data ditambahkan".format(len(values)))


# In[32]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "SELECT * FROM tblFilm"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)


# In[33]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "SELECT * FROM tblFilm"
cursor.execute(sql)

result = cursor.fetchone()

print(result)


# In[26]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "UPDATE tblFilm SET JudulFilm=%s, Jenis_Film=%s WHERE Kode_id=%s"
val = ("X-Men: Dark Phoenix", "Fantasy Action", 1)
cursor.execute(sql, val)

db.commit()

print("{} data diubah".format(cursor.rowcount))


# In[28]:


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_film"
)

cursor = db.cursor()
sql = "DELETE FROM tblFilm WHERE Kode_id=%s"
val = (1, )
cursor.execute(sql, val)

db.commit()

print("{} data dihapus".format(cursor.rowcount))


# In[ ]:


import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin",
  database="toko_mainan"
)


def insert_data(db):
  name = input("Masukan nama: ")
  address = input("Masukan alamat: ")
  val = (name, address)
  cursor = db.cursor()
  sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM customers"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("pilih id customer> ")
  name = input("Nama baru: ")
  address = input("Alamat baru: ")

  sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s"
  val = (name, address, customer_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  customer_id = input("pilih id customer> ")
  sql = "DELETE FROM customers WHERE customer_id=%s"
  val = (customer_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM customers WHERE name LIKE %s OR address LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)


# In[ ]:




