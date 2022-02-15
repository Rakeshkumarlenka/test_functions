'''
import psycopg2 #import the postgres library

#connect to the database
conn = psycopg2.connect(host='localhost',
                       dbname='postgres',
                       user='postgres',
                       password='root',
                       port='5432')
#create a cursor object
#cursor object is used to interact with the database
cur = conn.cursor()

#create table with same headers as csv file
cur.execute("CREATE TABLE student_result(name char(20), english int, math int, chemistry int ")

#open the csv file using python standard file I/O
#copy file into the table just created
with open('student_result.csv', 'r') as f:
    next(f) # Skip the header row.
    #f , <database name>, Comma-Seperated
    cur.copy_from(f, 'postgres', sep=',')
    #Commit Changes
    conn.commit()
    #Close connection
    conn.close()


f.close()
'''
import d6tstack
import glob

c = d6tstack.combine_csv.CombinerCSV([r'C:\Users\RAJESH\Documents\GitHub\test_functions\FEBRUARY\11-02-2022\student_result.csv']) # single-file
#c = d6tstack.combine_csv.CombinerCSV(glob.glob('*.csv')) # multi-file
c.to_psql_combine('postgresql+psycopg2://postgres:root@localhost/5432', 'student_result')