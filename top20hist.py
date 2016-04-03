import psycopg2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("select * from tweetwordcount order by count desc limit 20;")
records = cur.fetchall()
frequency = []
words = []

for line in records:
    frequency.append(line[1])
    words.append(line[0])

x_axis = np.arange(1, len(words) * 5, 5)

plt.bar(x_axis, frequency, width = 1.6, align='center')
plt.xticks(x_axis, words, rotation = 45, ha = 'right')
#plt.show()
plt.gcf().subplots_adjust(bottom=0.20)
plt.savefig('top20.png')