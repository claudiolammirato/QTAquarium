from setting_class import ConfigClass


lista = ConfigClass()

prova = lista.load_item("settings")

prova1 = prova.keys()

print(list(prova1)[0])

lista.save_item("settings","server","nome","claudio1")