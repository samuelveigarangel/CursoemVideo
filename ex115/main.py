from ex115.lib.interface import *
from ex115.lib.arquivo import *


create_file('register.txt')

while True:
    option = menu('Show logs', 'Registered', 'Exit')
    if option == 1:
        see_register()
    elif option == 2:
        register()
    elif option == 3:
        break