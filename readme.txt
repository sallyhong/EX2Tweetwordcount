W205 Exercise 2 Readme
Sally Hong

1. Create and run EC2 instance with AMI 'ucbw205_complete_plus_postgres_PY2.7 (ami-558fc730)'
	m3.medium was used for this exercise.
2. Install postgres (follow the below instructions or you can can use shell script from earlier lab)
	$ yum install postgres 
	$ vim /etc/yum.repos.d/CentOS-Base.repo
		Append 'exclude=postgresql*' to [base] and [updates]
		: wq # to save
	$ yum localinstall https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-6-x86_64/pgdg-centos95-9.5-2.noarch.rpm
	$ yum install postgresql95 postgresql95-server
	$ ln -sf /usr/pgsql-9.5/bin/psql /usr/bin/psql #to update link to postgresql 9.5
	$service postgresql-9.5 initdb #to initialize db
	$ service postgresql-9.5 start #to start service
	Edit /var/lib/pgsql/9.5/data/postgresql.conf
		$ vim /var/lib/pgsql/9.5/data/postgresql.conf
		change
			#listen_address = 'localhost'
		to
			listen_addresses = ‘*’
		Change
			#standard_conforming_strings = off
		to
			standard_conforming_strings = off
	Edit /var/lib/pgsql/9.5/data/pg_hba.conf
		$ vim /var/lib/pgsql/9.5/data/pg_hba.conf
		Append to last line
			host all all 0.0.0.0 0.0.0.0 md5
3. Install anaconda python # this comes with matplotlib which is used to bar plot. Alternatively python 2.7 can be installed via yum along with dependencies in the next step.
	$ wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda2-4.0.0-Linux-x86_64.sh
	$ bash Anaconda2-4.0.0-Linux-x86_64.sh
		<Enter>
		yes <Enter>
		<Enter>
		yes <Enter>
	Restart terminal
4. Install the following if not already installed (dependencies to run exercise 2)
	python 2.7
	a. pip
	b. ez_setup
	c. lein
		$ wget --directory-prefix=/usr/bin https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
		$ chmod a+x /usr/bin/lein
		$ sudo /usr/bin/lein
	d. virtualenv 
		$ pip install virtualenv
	e. tweepy
		$ pip install tweepy
	f. streamparse
		$ pip install streamparse
	g. psycopg2
		$ pip install psycopg2
	h. matplotlib (This comes with anaconda which was installed earlier)
		$ pip install matplotlib
5. Run 'sparse quickstart Tweetwordcount' to create folder with quickstart files
6. Copy over files from git repository to replace files in 'src' 'topologies' and the serving scripts
	$ git clone git@github.com:sallyhong/EX2Tweetwordcount.git
7. In postgres, create database tcount with user postgres.
	$ su - postgres
	$ psql
	postgres # create database tcount;
	postgres # \q
	$ exit
7. Run drop_create_table.py as this will drop table tweetwordcount and create table tweetwordcount in database tcount.
	$ python drop_create_table.py
8. Run 'sparse run' and press ctrl-c to break out of program
	If running as root, Lein will give warning that the program is being run as root. Press enter to continue running the program.
	$ sparse run
9. Run serving scripts
	a. finalresults.py
		Run without an option to show full results of all words and counts. Run with words you wish to query separated by a space (use double quotes around words that contain single quotes e.g. you're) to return their counts.
	b. histogram.py
		Run with argument MIN,MAX (e.g. 3,8) for a list of words and their counts between MIN and MAX inclusive sorted in ascending order by word.
	c. top20hist.py
		Will generate PNG file of bar plot of top 20 words and counts in same directory.
