# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    numbers.py                                       .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: schebbal <marvin@le-101.fr>                +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/06/11 02:53:44 by schebbal     #+#   ##    ##    #+#        #
#    Updated: 2019/06/11 03:15:54 by schebbal    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

def my_numbers():
    filename = 'numbers.txt'
    with open(filename,'r') as f:
        line = f.read().split(",")
        for number in line:
            print(number.strip())

if __name__ == '__main__':
    my_numbers()