from database_class import DatabaseManager


database = DatabaseManager()

table_string=(["id","SERIAL PRIMARY KEY"],["name", "TEXT NOT NULL"],["cognome", "TEXT"])

DatabaseManager.table_creation(database,"aquarium",table_string)

#database.insert_value("claudio",0,5,"Marta")