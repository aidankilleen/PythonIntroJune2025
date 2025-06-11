# sqlite_investigation.py
import sqlite3

"""
SELECT * FROM members;

INSERT INTO members (name, email, active)
VALUES('Orla', 'orla@gmail.com', 0)

DELETE FROM members WHERE id=11;

UPDATE members 
SET name="CHANGED"
WHERE id=12;
"""


FILE_NAME = "C:\\work\\training\\python\\testdb.db"

with sqlite3.connect(FILE_NAME) as conn:
    
    cursor = conn.cursor()
    sql = "SELECT * FROM members"
    cursor.execute(sql)

    rows = cursor.fetchall()

    print("ID\tName\t")
    for row in rows:
        print (f"{row[0]}\t{row[1]}\t")








