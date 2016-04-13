from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
#from redis import StrictRedis
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

class WordCounter(Bolt):

	def initialize(self, conf, ctx):
		self.counts = Counter()
		#cur.execute("DROP TABLE Tweetwordcount;")
		#conn.commit()
		#cur.execute("CREATE TABLE Tweetwordcount (word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);")
		#conn.commit()
		#self.redis = StrictRedis()
				
	def process(self, tup):
		word = tup.values[0]
				
		# If local count == 0 (new word), then insert new word into database
		if self.counts[word] == 0:
			self.counts[word] += 1 # Add to local counter
			# Add new row with word
			cur.execute("INSERT INTO tweetwordcount (word, count) \
				VALUES (%s, %s);", (word, 1))
			conn.commit()
			
		# If local counter already has word, then update values
		else:
			self.counts[word] += 1 # Add to local counter
			# Update counter
			cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s;", (self.counts[word], word)) 
			conn.commit()
			
		self.emit([word, self.counts[word]])	
		# Log the count - just to see the topology running
		self.log('%s: %d' % (word, self.counts[word]))
