import psycopg2
import matplotlib
matplotlib.use('Agg') # Need this as we can't visualize the plots in our instance
import matplotlib.pyplot as plt
import numpy as np

# Define connection
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# Run query for top 20 words by count
cur.execute("select * from tweetwordcount order by count desc limit 20;")
records = cur.fetchall()

# Initialize words and frequency
frequency = []
words = []

# Create X and Y arrays
for line in records:
    frequency.append(line[1])
    words.append(line[0])

# Initialize X axis
x_axis = np.arange(1, len(words) * 5, 5)

# Plot title
plt.title('Top 20 Words from Twitter Stream')

#shift plot away from y axis for aestheics
plt.bar(x_axis+2, frequency, width = 1.6, align='center')
plt.xticks(x_axis+2, words, rotation = 45, ha = 'right')

# plt.show() # We don't have ability to visualize plot in our instance so we skip this and just save to PNG

# Pad the bottom of the plot to show all words without cropping
plt.gcf().subplots_adjust(bottom=0.20)

# Save as PNG
plt.savefig('top20.png')
