import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
    
if len(sys.argv) > 1:
    arg = (sys.argv[1]).split(',')
    low = arg[0]
    high = arg[1]
    cur.execute("SELECT word, count FROM Tweetwordcount WHERE count >= %s AND count <= %s",(low, high))
    records = cur.fetchall()
    for rec in records:
        print """  "%s": %s"""%(rec[0],rec[1])
    conn.commit()
else:
    print "Please define range argument 'MIN,MAX'"