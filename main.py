# 1
print("1) 1 dan 10 gacha sonlar ro'yxati:")
numbers_list = []
for i in range(1, 11):
    numbers_list.append(i)
print(numbers_list)


# 2
print("\n2) Ism harflari ro'yxati:")
name = input("Ismingizni kiriting: ")
letters_list = []
for harf in name:
    letters_list.append(harf)
print(letters_list)


# 3
print("\n3) Raqam qo'shish:")
user_number = int(input("Bir son kiriting: "))
numbers_list.append(user_number)
print(numbers_list)


# 4
print("\n4) Ikki ro'yxatni birlashtirish:")
new_list = numbers_list + letters_list
print(new_list)


# 5
print("\n5) Bo'sh ro'yxatni kengaytirish:")
empty_list = []

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False]

empty_list.extend(list1)
empty_list.extend(list2)
empty_list.extend(list3)

print(empty_list)
