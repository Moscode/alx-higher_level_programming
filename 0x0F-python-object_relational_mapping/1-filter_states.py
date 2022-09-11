#!/usr/bin/python3
"""
Use MySQLdb to query a database for states whose names
start with the letter N
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    userInput = sys.argv[1]
    passwdInput = sys.argv[2]
    dbInput = sys.argv[3]
    db = MySQLdb.connect(
            host='localhost', user=userInput,
            passwd=passwdInput, db=dbInput,
            port=3306, charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
