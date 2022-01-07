import psycopg2
import datetime
from bullet import Bullet


class DbConnect:
 
 def __init__(self):
  self.rows=[]
  self.limit_reached=0
  self.conn=psycopg2.connect(
    database="d6kb86r00f9rno",
    user="uyeseufvhzragg",
    host="ec2-34-255-21-191.eu-west-1.compute.amazonaws.com",
    port="5432",
    password="1e2901550a3614c56949eba40ea34df80b29d8febcbf67c048cd611850a3c9be"
  )
  # Open a cursor to perform database operations
  self.cur = self.conn.cursor()
  
 def create_table_crypto_value(self,crypto_name):
  
  # SQL statement to create a table
  if (crypto_name!="1INCH"):
   if (crypto_name!="FOR"): 
    if (crypto_name!="ANY"): 
     sqlCreateTable = "CREATE TABLE IF NOT EXISTS "+crypto_name+" (cryptovalue numeric, joindate timestamp);"

  # Execute CREATE TABLE command

    self.cur.execute(sqlCreateTable)
    self.conn.commit()

  # Insert statements


 
 def fill_table(self,crypto_name,value):
  
  if (crypto_name!="1INCH"): 
   if (crypto_name!="FOR"): 
    if (crypto_name!="ANY"): 
     sqlInsertRow= "INSERT INTO "+crypto_name+" values("+value+", current_timestamp)"

  # Insert statement

    self.cur.execute(sqlInsertRow)
    self.conn.commit()
    print("\n\n\n\n\nrow "+crypto_name+" added")
   
  

  # Select statement
 def pick_from_table_check(self,crypto_name):
  
  if (crypto_name!="1INCH"):
   if (crypto_name!="FOR"): 
    if (crypto_name!="ANY"): 
     self.crypto_name=crypto_name.replace(" ", "")
     sqlSelect = "select * from "+self.crypto_name+" where joindate < now() - interval '4 hours' and joindate > now() - interval '5 hours';"
     self.cur.execute(sqlSelect)

     self.rows = self.cur.fetchall()
     
     sqlSelect = "select * from "+self.crypto_name+" where joindate > now() - interval '4 minutes';"
     self.cur.execute(sqlSelect)

     self.rows_current = self.cur.fetchall()

   # Print rows 

     for row in self.rows:
      print("now old row: ")
      print(row)
     print("now row current \n")
      
     for row_current in self.rows_current:
       print(row_current)
      
     if(len(self.rows_current)>1):
      difference_time=self.rows_current[-1][1]-self.rows_current[-2][1]
      print("difference_time="+str(difference_time))
        
      
     
     constant=1
       
     if len(self.rows)>2:
      if len(self.rows_current)>1:
         if (self.rows_current[-1][0]>0.130):
              if (((self.rows_current[-constant][0]-self.rows[-1][0])/self.rows_current[-constant][0])>0.08):
                         if (self.rows_current[-1][1]-self.rows[-constant][1])>datetime.timedelta(seconds=13000):   
                          
                          print("entereeeeeeeeeed") 
                          
                          string_to_send="\n new local minimum detected!!----------crypto: "+crypto_name+" current value is "+str(self.rows_current[-constant][0])+"\n previous value was "+str(self.rows[-constant][0])+"\n at timestamp: "+str(self.rows[-constant][1])
                           
                          Bullet(string_to_send)
                 

     self.conn.commit()
     
 def check_if_full(self,crypto_name):
      sqlSelect = "select * from "+crypto_name+";"
      self.cur.execute(sqlSelect)
      self.all_rows = self.cur.fetchall()
      if len(self.all_rows)>35:
       sqlSelect = "delete from "+crypto_name+" where joindate > now() - interval '210 minutes' or joindate < now() - interval '290 minutes';"
       self.cur.execute(sqlSelect)
       self.conn.commit()
 
     
 def close(self):
  # Close the session and free up the resources   
  self.conn.close() 
