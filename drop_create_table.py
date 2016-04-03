import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("drop table tweetwordcount;")
conn.commit()

cur.execute("CREATE TABLE Tweetwordcount (word TEXT NOT NULL PRIMARY KEY, count INT NOT NULL);")
conn.commit()
