# #1
# x = lambda h,a,b: f'Обьём бассейна: {h*a*b}'
# print(x(4,4,4))

# #2
# days_pass = int(input('Сколько дней прошло с начала года?: '))
# days_left = lambda x: f'Осталось дней до нового года {365-x}'
# print(days_left(days_pass))

#3
# def odd_numbers(n):
#     if n > 0:
#         if n % 2 != 0:
#             print(n)
#         odd_numbers(n+1)
# print(odd_numbers(2))

# #4
# a = input('Введите что нибудь сюда?: ')
# a = set(a)
# def delete_element(x):
#     if len(x) > 0:
#         x.pop()
#         print(x)
#         delete_element(x)
# print(delete_element(a))

# #5
# import random
# def random_list(x):
#     result = random.sample(range(10,50), 100)
#     return result
# print(random_list)

# #6
# def log_pass():
#     login = input('login: ')
#     password = input('password: ')
#     return login, password
# @log_pass
#     def ord():
#         ord_login = []
#         ord_password = []
#         for x in login:
#             ord_login.append(ord(x))
#         for x in password:
#             ord_password.append(ord(x))
#         return ord_login, ord_password
# print(log_pass())

# #7
# list = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
# for x in list:
#     result = lambda x: f'result {x*1.185}'
#     print(result(x))
