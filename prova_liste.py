table_string=(["id","SERIAL PRIMARY KEY"],["name", "TEXT NOT NULL"],["cognome", "TEXT"])
values=(["name","Claudio"],["cognome","Marta"])


def string_table(table_string):
    testo="CREATE TABLE '''+table_name+''' ("

    for x in table_string:
        testo = testo + x[0]+" "+x[1]+ ","
    testo = testo[0:-1] + ")"
    print(testo)

#string_table(table_string)


def insert_value(table_name, values):
    testo='''INSERT INTO '''+table_name+''' ('''

    for x in values:
        if(x[0] != "id"):
            testo = testo + x[0]+","
    testo = testo[0:-1] + ") VALUES("
    for x in values:
        if(x[0] != "id"):
            testo = testo + x[1]+","
    testo = testo[0:-1] + ")"
    print(testo)

insert_value("aquarium",values)


#insert_value = '''INSERT INTO '''+table_name+''' (stf_id, stf_name) VALUES('%s', '%s');'''%(id_value, name_value)





