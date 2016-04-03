import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("drop table if exists tweetwordcount;")
conn.commit()

# The optoin 'if not exists' is unavailable in postgres 8.4. Use 9.0+ to use this option or take out.
cur.execute("CREATE TABLE if not exists Tweetwordcount (word TEXT NOT NULL PRIMARY KEY, count INT NOT NULL);")
conn.commit()
