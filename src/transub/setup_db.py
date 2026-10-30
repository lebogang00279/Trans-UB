from .db import initialize,DEFAULT_DB
def seed(c):
    for t in ['notifications','order_status_changes','orders','listings','student_accounts']: c.execute(f'DELETE FROM {t}')
    c.executemany('INSERT INTO student_accounts VALUES (?,?,?,?)',[
      ('202302072','Buyer',1,1),('202300001','Seller',1,1),('202300002','Buyer2',1,1),('202399999','Ineligible',0,1)])
    c.executemany('INSERT INTO listings VALUES (?,?,?,?,?)',[
      ('LIST-104','202300001','Calculator','Available',1),('LIST-OWN','202302072','Textbook','Available',1)])
def main():
    c=initialize(DEFAULT_DB); seed(c); c.close(); print('Created transub.db')
if __name__=='__main__': main()
