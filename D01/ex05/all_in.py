# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    all_in.py                                        .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: schebbal <marvin@le-101.fr>                +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/06/11 02:53:44 by schebbal     #+#   ##    ##    #+#        #
#    Updated: 2019/06/11 03:15:54 by schebbal    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #
import sys
states = {
    "Oregon"    : "OR",
    "Alabama"   : "AL",
    "New Jersey": "NJ",
    "Colorado"  : "CO"
}
capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
}

def all_in(item):
    ret_state = all_state(item)
    
    if ret_state:
        print("{0} is the capital city of {1}".format(ret_state[0], ret_state[1]))
    else:
        ret_cap = all_capital_city(item)
        if ret_cap:
            print("{0} is the capital city of {1}".format(ret_cap[0], ret_cap[1]))
        else:
            print("{0} is neither a capital city nor a state".format(item))

def all_state(cap):
	""" cette fonction parcours des dictionnaires """

	for abbrev, capital in capital_cities.items():
		if cap.lower() == capital.lower():
			for state, abbreviation in states.items():
				if abbreviation.lower() == abbrev.lower():
					return [capital, state]
	return None

def all_capital_city(state):
	""" cette fonction parcours des dictionnaires """

	for state_key in states:
		if state_key.lower() == state.lower():
			if capital_cities.get(states[state_key]):
				return [capital_cities[states[state_key]], state_key]
	return None

def all_split(str):
    items = str.split(",")
    for item in items:
        if len(item.strip()) != 0:
            #print(item.strip())
            all_in(item.strip())

if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_split(sys.argv[1])