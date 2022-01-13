swap1 = 3
swap2 = 4
print(swap1, swap2)
swap1, swap2 = swap2, swap1
print(swap1, swap2)
s1 = 'Hellowersdfxcvxcvxcvxcv ! \n' # используя апострофы
s2 = "hola \n" # используя кавычки
s3 = '''\n Привет!
        Хорошего дня!''' # используя тройные "апострофы" или тройные кавычки
print(s1, s2, s3)
print(s1[2::2])
print(s2[::-1])
