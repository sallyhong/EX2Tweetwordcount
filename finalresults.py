import psycopg2
import sys

 
# Get the total number of args passed to the finalresults.py
total = len(sys.argv)
 
# Get the arguments list 
#cmdargs = str(sys.argv)

#def wrapper(s1):
#    return """%s""" % s1
 

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
    
if total > 1:

    input_word = sys.argv[1]
    cur.execute("""SELECT count FROM Tweetwordcount WHERE word=%s""", (input_word,))
    input_count = cur.fetchall()
    if input_count:
        print """ Total number of occurences of "%s": %s"""%(input_word,input_count[0][0])
    else:
        print """ Total number of occurences of "%s": 0"""%(input_word)
    conn.commit()
else:
    cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY word ASC")
    records = cur.fetchall()
    for rec in records:
       print rec, "\n"
    conn.commit()
