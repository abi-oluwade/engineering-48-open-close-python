from read_txt import *


class NewUsers():
    def __init__(self, user_name):
        self.name = user_name

    def add_fav_colour(self, colour):
        self.colour = colour
        f = open('names.txt', 'a+')
        for i in range(10):
            (f.write("I am user ID: %d\r\n" % (i + 1)))
        f.close()
        return 'Hi I am ' + self.name + ' and my favourite colour is ' + self.colour + '.'


def read_names(file_name):
    names = {}
    name_list = open_name_list(file_name)
    for name in name_list:
        words = name.split()
        if len(words) == 2 and words[0] == 'star':
            new_user_name = words[1]
            names[new_user_name] = NewUsers(name)
    return names


user1 = NewUsers('Luke')
user2 = NewUsers('Abi')
user3 = NewUsers('Mike')
user4 = NewUsers('Will')
user5 = NewUsers('Joana')
user6 = NewUsers('Hannah')
user7 = NewUsers('Natasha')
user8 = NewUsers('Katy')
user9 = NewUsers('Jonathan')
user10 = NewUsers('Sindy')
#
print(user1.add_fav_colour('green'))
# read_names('names.txt')
