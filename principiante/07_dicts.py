my_dict = dict();
other_dict = {
    "name" : "go",
    "lastname" : "Baños",
    "age" : 16,
};

print(my_dict)

# Funciones
print(other_dict.values());
print(other_dict.items() );
print(other_dict.keys());
print(dict.fromkeys(other_dict)); # crea un nuevo diccionario con claves pero sin valores

other_dict.update({"number_prefix" : 34}) # el equivalente de un concat, vaya
other_dict.setdefault('name', 'Hugo'); # busca una llave y la devuelve. Si no lo encuentra, mete la llave con su valor | NoneType

other_dict.pop('name'); # elimina la clave:valor que quieras
other_dict.popitem(); # elimina la última clave:valor del diccionario
other_dict.clear(); # elimina todas las claves