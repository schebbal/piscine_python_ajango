# **************************************************************************** #
#                                                           LE - /             #
#                                                               /              #
#    var.py                                           .::    .:/ .      .::    #
#                                                  +:+:+   +:    +:  +:+:+     #
#    By: schebbal <marvin@le-101.fr>                +:+   +:    +:    +:+      #
#                                                  #+#   #+    #+    #+#       #
#    Created: 2019/06/11 02:53:44 by schebbal     #+#   ##    ##    #+#        #
#    Updated: 2019/06/11 03:15:54 by schebbal    ###    #+. /#+    ###.fr      #
#                                                          /                   #
#                                                         /                    #
# **************************************************************************** #

def my_var(a):
    print (a, ' est de type ', type(a))

if __name__ == '__main__':
    a = 42
    my_var(a)
    a = '42' 
    my_var(a)
    q = 'uarante-deux' 
    my_var(a)
    a = 42.0 
    my_var(a)
    a = True 
    my_var(a)
    a = [42] 
    my_var(a)
    a = {42: 42} 
    my_var(a)
    a = (42,) 
    my_var(a)
    a = set() 
    my_var(a)
