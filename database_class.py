import psycopg2
from setting_class import ConfigClass



class DatabaseManager():
    def __init__(self):
        super().__init__()

        settings = ConfigClass()
        settings_loaded = settings.load_item("settings")

        self.conn = psycopg2.connect(database=settings_loaded['database']['name'],
                        host=settings_loaded["database"]["url"],
                        user=settings_loaded["database"]["username"],
                        password=settings_loaded["database"]["password"],
                        port=settings_loaded["database"]["port"])

        self.cursor = self.conn.cursor()
    def table_creation(self, table_name, table_string):

        testo='''CREATE TABLE '''+table_name+''' ('''

        for x in table_string:
            testo = testo + x[0]+" "+x[1]+ ","
        testo = testo[0:-1] + ");"
        print(testo)

        table_creation = testo
        try:
            self.cursor.execute(table_creation)
            self.conn.commit()
        except:
            print("error - might already exists")
        self.cursor.close()
        self.conn.close()

    def insert_value(self, table_name, field,id_value, name_value):
        insert_value = '''INSERT INTO '''+table_name+''' (stf_id, stf_name) VALUES('%s', '%s');'''%(id_value, name_value)
        self.cursor.execute(insert_value)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def delete_value(self, table_name, field,id_value):
        insert_value = '''DELETE FROM '''+table_name+''' WHERE stf_id = %s;'''%(id_value)
        self.cursor.execute(insert_value)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def update_value(self, table_name, field,id_value):
        update_value = '''UPDATE '''+table_name+''' SET stf_name='Marco' WHERE stf_id = %s;'''%(id_value)
        self.cursor.execute(update_value)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()