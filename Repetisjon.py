# Oppgave 1
# for i in range(1,11):
#     print(i)

# Oppgave 2
# sum = 0
# for i in range(1,101):
#     sum +=i
#     print(f"{i}. {sum}")

# Oppgave 3
# i = 1
# while i <= 30:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# Oppgave 4
# a = 4
# b = 4847447
# def sum_of_two(a,b):
#     return a+b
# 
# print(sum_of_two(a,b))

# Oppgave 5
# list_of_nums = [5,7,22,345,2,2,9]
# def find_average(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return (sum/len(list))
# 
# print(find_average(list_of_nums))



# Ekstra 1
# a = 1
# b = 100
# 
# def find_primes(from_num, to_num):
#     primes = []
#     for i in range(from_num, to_num):
#         k = 0
#         for j in range(2, i //2 +1):
#             if (i % j ==0):
#                 k += 1
#         if k <= 0:
#             primes.append(i)
# 
#     print(primes)
# 
# find_primes(1, 100)

# Ekstra 2
u_num = int(input("Enter your num: "))

i = 1
previous = 0
while i <= u_num:
    print(i)
    previous, i = i, i+previous
