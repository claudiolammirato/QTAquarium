from database_class import DatabaseManager


database = DatabaseManager()
values=(["name","Claudio"],["cognome",1])

table_string=(["id","SERIAL PRIMARY KEY"],["name", "TEXT NOT NULL"],["cognome", "TEXT"])

#DatabaseManager.table_creation(database,"aquarium",table_string)

#DatabaseManager.insert_value(database,"aquarium",values)

#DatabaseManager.delete_value(database, "aquarium", 1)

#DatabaseManager.update_value(database, "aquarium", 3, "name", 1)

DatabaseManager.create_database(database, "qtaquarium")


#database.insert_value("claudio",0,5,"Marta")