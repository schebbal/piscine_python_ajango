# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    periodic_table.py.py                                   .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: schebbal <marvin@le-101.fr>                +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/06/12 02:53:44 by schebbal     #+#   ##    ##    #+#        #
#    Updated: 2019/06/12 03:15:54 by schebbal    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

def string_to_dict(line):
    my_dict = dict()
    elem_split = line.split("=")
    #print(elem_split)
    my_dict['name'] = elem_split[0].strip(" ")
    posi_split = elem_split[1].split(",")
    #print(posi_split)
    
    for data in posi_split:
        data_split = data.split(":")
        #print(third_split)
        my_dict[data_split[0].strip(" ")] = data_split[1].strip(" \n")
    return my_dict

def read_file():
    """ renvoie un tableau rempli a partir du fichier """
    with open("periodic_table.txt") as f:
        my_tab = []
        for line in f:
            my_dict = string_to_dict(line)
            my_tab.append(my_dict)
            #print("------- : %s", my_tab, "\n")
        return my_tab

def header(f):
	f.write("<!DOCTYPE html>\n")
	f.write("<html lang='en'>\n")
	f.write("  <head>\n    <meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>\n    <title>Periodic table</title>\n")
	f.write("    <style>table {	width: 100%;} td {border: 1px solid black; padding:10px} </style>\n  </head>\n")

def footer(f):
	f.write("</html>\n")

def content(f, tab):
	previous = 0
	current = 0
	s = "    <table>\n"
	for elem in tab:
		current = int(elem['position'])
		if current == 0:
			s +="      <tr>\n"
		if current - previous > 1:
			s += "        <td colspan='" + str(current - previous - 1) + "'></td>\n"
        s += "        <td><h4>" + elem['name'] + "</h4>\n"
        s += "          <ul><li>" + elem['number'] +"</li><li>" + elem['small'] +"</li><li>" + elem['molar'] + "</li></ul></td>\n"
        if current == 17:
            s += "      </tr>\n"
            current = 0
        previous = current

	s += "    </table>\n"	
	f.write(s)

def body(f, tab):
	f.write("  <body>\n")
	content(f, tab)
	f.write("  </body>\n")

def write_to_file(tab):
	#print(tab)
	with open("periodic_table.html", "w") as f: 
		header(f)
		body(f, tab)
		footer(f)

def generate_html():
    my_tab = read_file()
    #for elem in my_tab:
    #    print(elem)
    write_to_file(my_tab)
    
if __name__ == '__main__' :
	generate_html()