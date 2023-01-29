name = 'hbc';
lastname = '167';
age = 16;

print("Mi nombre es {} {} y tengo {} años".format(name, lastname, age));
print("Mi nombre es %s %s y tengo %d años" %(name, lastname, age));

# inferencia de datos
print(f"Mi nombre es {name} {lastname} y tengo {age} años"); # importante la "f" al inicio!
# f = format

# Desempaquetado de caracteres
language = "Python";
a, b, c, d, e, f = language;
# P Y T H O N

# print(a);
# print(b);

# División
language_slice = language[1:3];
print(language_slice);

# Reverse
reversed_language = language[::-1];
print(reversed_language);

# Funciones
print(language.capitalize()); # Pone en mayúsculas un texto
print(language.upper()); # Todo mayus
print(language.count('t'));# Cuenta cuantas cosas ahí, ns
print(language.isnumeric());# Verifica si es un número
print(language.lower());# Pasa todo a minúsculas
print(language.upper().isupper()); # ¿Es PYTHON está en mayúsculas?
print(language.startswith('Py')); # como en JS ya tu sabes
print(language.endswith('hon'))
