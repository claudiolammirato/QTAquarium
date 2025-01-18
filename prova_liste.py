table_string=(["id","SERIAL PRIMARY KEY"],["name", "TEXT NOT NULL"],["cognome", "TEXT"])


def string_table(table_string):
    testo="CREATE TABLE '''+table_name+''' ("

    for x in table_string:
        testo = testo + x[0]+" "+x[1]+ ","
    testo = testo[0:-1] + ")"
    print(testo)

string_table(table_string)




