def str_compare(str1,str2):
    if str2 == "learn":
        a=3
        return a
    elif str1 == str2:
        b=1
        return b
    elif str1 != str2  and  len(str1)>len(str2):
        c=2
        return c


def main():
    string1 = str(input("Введите строку 1:"))
    string2 = str(input("Введите строку 2:"))
    print("Результат сравнения= {}".format(str_compare(string1,string2)))

if __name__ == '__main__':
    main()
