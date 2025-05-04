all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here

def filter_name(name):
    aux = []
    if name[0] == "R":
        aux.append(name)

    return aux

resulting_names = list(filter(filter_name, all_names))

print(resulting_names)




