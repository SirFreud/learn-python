dicts = [
	{'name': 'Michelangelo',
	 'food': 'PIZZA'},
	{'name': 'Garfield',
	 'food': 'lasanga'},
	{'name': 'Walter',
	 'food': 'pancakes'},
	{'name': 'Galactus',
	 'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(st, di_list):
    new_list = []
    for i in di_list:
        new_list.append(st.format(**i))
        return new_list

my_variable = string_factory(string, dicts)

print(my_variable)
