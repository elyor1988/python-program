# # int, str, float, bool
# #
# #
# # list, tuple, dict, set
# #
# # primitive type
# #
# # _
# #
# #
# # a-zA-Z, 0-9, _
# #
# # var_1 = 2
# # var1
# # _var
# #
# # class
# #
# # #include
# #
# # void function(){
# # 	return
# # }
# #
# #
#
# a_int = 2  # int type
# a_float = 0.5  # float type
# a_bool = False  # boolean type
# a_str_0 = 'hel\'lo'  # string type
# a_str_1 = "hello"  # string type
# a_str_2 = """hello"""  # string type docstring
# a_str_3 = '''hello'''  # string type
#
# # comment #, ''', """
# import keyword
# print(keyword.kwlist) # keyword larni listini olish
#
# a_list = [1, [1, 2], '']
# a_tuple = (1, 2, 3)
# a_set = {1, 2, 3}
# a_dict = {'key_1': 1, 'key_2': 2}
#
# print(b)

# a,b = 5,8
# b,a = a,b
# # c = a
# # a = b
# # b = c
# print(a, b)
# print(2,3, end='')
# print(1)

# a, b = 1, 2
#
# print(int)
# a = 2
# print(a)
#
# del a
# print(a)
# var_1 = '22' # int(var_1) type casting

# print(var_1 + str(1))
# print('hello' + ' world')
# print('hello' ' world')
#
# var_2 = '22 ' "123"
# print(var_2)
# 2+3
# print(2+3)


# a = b = 2
#
# a,b = 2,3,4
# c = 2,3,4
# a = 2
# a = 2+1
#
# a = [[1,2,3],
#      [2,3,4]] # nested list and matrix
#
# a = [1,6,2,4,5,6] # list sekin chunki qiymatlar o'zgaradi
# b = (1,2,3) # tuple tezroq listga qaraganda, qiymatlar o'zgarmaydi
#
# print(a)
# a = 2
# a = False
# a = 2.2
# a = [] # type list
# a = [1,'2',3, [2,3,], (1,2)] # type list
# a = list() # type list
#
# b = tuple() # type tuple
# b = ('2', )
# b = '2',
# b = '2', 1
# b = (1,2,3)
#
#
# print(b[1])
# print(type(b))




# mutable  - o'zgaruvchi, list, dict, set
# immutable- o'zgarmas, int, float, bool, tuple, str

# a = 0 # ~id, referance, ~content
# a = 5 # ~id, referance, ~content
#
# list_1 = [1,2,4,5]
# print(list_1)
# print(id(list_1), hex(id(list_1)))
# print(type(list_1))
#
# list_1.append(2)
# print(list_1)
# print(id(list_1), hex(id(list_1)))
# print(type(list_1))
# list_1 reference o'zgarmagan, content o'zgardi, id o'zgarmadi, shuning uchun mutable


#id, referance, content
#
# print(a)
# print(id(b))
# print(id(a))
# print(hex(id(a)))

# a = 20
# print(a)
# print(id(a), hex(id(a)))
# print(type(a))
#
# a = a+2
# print(a)
# print(id(a), hex(id(a)))
# print(type(a))
# a reference o'zgarmagan, content o'zgardi, id o'zgardi, shuning uchun immutable


# a = 20
# print(a)
# print(id(a), hex(id(a)))
# print(type(a))
#
# a = a+2
# print(a)
# print(id(a), hex(id(a)))
# print(type(a))

# list_1 = [1,2,4,5]
# list_1 = [1,'2',4,5]
# list_1[2] += 2
#
# list_1[0] += 1 #
# print(list_1)

# list_1 = [1,2,4,5]
# print(list_1)
# print(id(list_1), hex(id(list_1)))
# print(type(list_1))
#
# list_1 = list(list_1)
# print(list_1)
# print(id(list_1), hex(id(list_1)))
# print(type(list_1))
# list_1 reference o'zgarmagan, content o'zgardi, id o'zgarmadi, shuning uchun mutable



a = '20'
print(a, id(a), hex(id(a)))
print(type(a))

a = a+'2'
print(a, id(a), hex(id(a)))
print(type(a))
