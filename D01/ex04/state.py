# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    state.py                                         .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: schebbal <marvin@le-101.fr>                +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/06/11 02:53:44 by schebbal     #+#   ##    ##    #+#        #
#    Updated: 2019/06/11 03:15:54 by schebbal    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #
import sys
def state(capital):
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
    if capital in capital_cities.values():
        x = [c for c, v in capital_cities.items() if v == capital]
        y = [c for c, v in states.items() if v == x[0]]
        print(y[0])
    else:
        print("Unknown capital city")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        state(sys.argv[1])