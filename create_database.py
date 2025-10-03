import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
from setting_class import ConfigClass


settings = ConfigClass()
settings_loaded = settings.load_item("settings")





#CREATE DATABASE
def create_database(database_name):
    try:
        conn = psycopg2.connect(database=settings_loaded['database']['initial_name'],
                        host=settings_loaded["database"]["url"],
                        user=settings_loaded["database"]["username"],
                        password=settings_loaded["database"]["password"],
                        port=settings_loaded["database"]["port"])
        # handle in case of error
        cursor = conn.cursor()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE
    except:
          print("create out")
    try:
        create_database = '''CREATE DATABASE '''+database_name

        

        #print(sql.SQL('CREATE DATABASE {};').format(sql.Identifier(database_name)))
        cursor.execute(sql.SQL('CREATE DATABASE {};').format(sql.Identifier(database_name)))
        #self.cursor.execute(create_database)
        conn.commit()
        cursor.close()
        conn.close()
        print("Database Created!!!")
    except:
        print("Database already exist")
        
        