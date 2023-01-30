"""
Un set no es una estructura ordenada (tienen un hash)
Los elementos no se repiten
"""

my_set = set();
other_set = {"Hugo", "Baños", 16, 172};

my_set.add('Toyota');
print("Baños" in my_set);

other_set.remove(172);
my_set.clear();
print(my_set);

my_set.add('Audi');

my_new_set = my_set.union(other_set); # une dos sets sin alterarlos
print(my_new_set.difference(my_set)); # almacena en un set sin alterar el original los
# valores que tengan ambos entre sí