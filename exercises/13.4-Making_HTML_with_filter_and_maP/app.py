all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here

def filter_colors(obj):
	return obj["sexy"]

new_list = list(filter(filter_colors, all_colors))

def generate_li(lst):
    return f"<li>{lst['label']}</li>"

final_list = list(map(generate_li, new_list))

print(final_list)