my_list = list(["first", 1]);
[name, value] = my_list;

print(my_list);
print(my_list.count(1))

# concat lists
print(my_list*10)

# funciones
my_list.append("Hola") # insertar al final
my_list.insert(1, "negro") # insertar donde sea
my_list.remove("negro") # remover valores
my_list.pop() # remover último valor de la lista

numbers = [10, 8, 3, 1]
numbers.sort()
print(numbers)

strings = ["hola", "adios", "hasta luego", "saca ya el album petardo"]
strings.sort()
print(strings)