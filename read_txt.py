def open_name_list(file_name):
    try:
        with open(file_name, 'r') as file:
            name_list = file.readlines()
        for names in name_list:
            print(names)

    except FileNotFoundError as errmsg:
        print('Check your file name!')
        print(errmsg)

    finally:
        print('These are a list of names!')




# open_name_list('names.txt')

# def add_number(x,y):
#     x + y
#     return x + y            Remember the function syntax!
# print(add_number(4,5))
