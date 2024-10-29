#number = 1234
#n1 = number // 1000
#n2 = number // 500
#n3 = number // 10 % 10
#n4 = number % 10

#print(n1)
#print(n2)
#print(n3)
#print(n4)


#number = 12345
#n1 = 1
#n2 = 2
#n3 = 3
#n4 = 4
#n5 = 5
#result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
#print(result)

#number = 37568
#n1 = 3
#n2 = 7
#n3 = 5
#n4 = 6
#n5 = 8
#result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
#print(result)







#first_lst = [12, 3, 4, 10 ]  #  завдання 3.2

#first_lst.insert(0, 10) # через insert(індекс, число) додаємо число.
#print(first_lst)
#first_lst = [10, 12, 3, 4, 10]
#x = first_lst.pop()             #значення х видаляє останній елемент в рядку.
#print(x)
#print(first_lst) # результат [10, 12, 3, 4]


#second_lst = [12, 3, 4, 10, 8]
#second_lst. insert (0,8)
#print(second_lst)
#x = second_lst.pop()             #значення х() видаляє останній елемент в рядку.
#print(x)
#print(second_lst)




#my_lst = [1, 2, 3, 4, 5, 6]         #завдання 3.3
#first_lst, second_lst = [[1, 2, 3],[ 4, 5, 6]]
#print(first_lst)
#print(second_lst)
#print(my_lst)

#my_lst = [1, 2, 3]
#first_lst, second_lst = [[1, 2],[3]]
#print(first_lst)
#print(second_lst)
#print(my_lst)

#my_lst = [1, 2, 3, 4, 5]
#first_lst, second_lst = [[1, 2, 3],[ 4, 5]]
##print(first_lst)
#print(second_lst)
#print(my_lst)

#my_lst = [1]
#first_lst, second_lst = [[1],[]]
#print(first_lst)
#print(second_lst)
#print(my_lst)

#my_lst = []
#first_lst, second_lst = [[],[]]
#print(first_lst)
#print(second_lst)
#print(my_lst)

#Завдання 4.1

 lst_nums = [0, 1, 0, 12, 3]
 count_of_zero = lst_nums.count(0)  #count(0) покаже скільки нулів ми маємо в рядку
 print(count_of_zero)  #2
 lst_nums.remove(0)   #по черзі видаляємо нулі
 print(lst_nums)
 lst_nums.remove(0)
 print(lst_nums)
 lst_nums.append(0)   # по черзі додаємо нулі
 print(lst_nums)
 lst_nums.append(0)
 print(lst_nums)   # [1, 12, 3, 0, 0]


my_list = [1, 0, 13, 0, 0, 0, 5]
my_list.append(0)
my_list.append(0)
my_list.append(0)
my_list.append(0)
print(my_list)
my_list.pop(1)
print(my_list)
my_list.pop(2)
print(my_list)
my_list.pop(2)
print(my_list)
my_list.pop(2)
print(my_list)


second_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
second_list.insert(-1, 0)
print(second_list)
second_list.insert(-2, 0)
print(second_list)
second_list.insert(-3, 0)
print(second_list)
second_list.insert(-4, 0)
print(second_list)
second_list.insert(-5, 0)
print(second_list)
second_list.insert(-6, 0)
print(second_list) # [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0, 0, 0, 0, 0, 0, 0]
del second_list[1]
print(second_list)
del second_list[3]
print(second_list)
del second_list[4]
del second_list[5]
print(second_list)
del second_list[6]
print(second_list)
del second_list[6]
print(second_list) #[9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

my_list = [0]
del my_list[0]
print(my_list)
my_list.append(0)
print(my_list)
