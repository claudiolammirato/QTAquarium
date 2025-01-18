import psycopg2

class DatabaseManager():
    def __init__(self):
        super().__init__()

        self.conn = psycopg2.connect(database="qtaquarium",
                        host="192.168.1.113",
                        user="",
                        password="",
                        port="5432")

        self.cursor = self.conn.cursor()
    def table_creation(self, table_name):

        table_creation = '''
        CREATE TABLE '''+table_name+''' (
            stf_id SERIAL PRIMARY KEY,
            stf_name TEXT NOT NULL
        )
        '''
        self.cursor.execute(table_creation)
        self.conn.commit()
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