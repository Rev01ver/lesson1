def str_compare(str1,str2):
    if str2 == "learn":
        return 3
    elif str1 == str2:
        return 1
    elif str1 != str2  and  len(str1)>len(str2):
        return 2

def main():
    string1 = str(input("Введите строку 1:"))
    string2 = str(input("Введите строку 2:"))
    print("Результат сравнения= {}".format(str_compare(string1,string2)))

if __name__ == '__main__':
    main()
