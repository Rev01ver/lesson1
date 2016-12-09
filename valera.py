def find_person(n,p):
    while p:
        if p.pop()== n:
            good = "Валера нашелся"
            break
    return good

def main():
    people = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    print(find_person("Валера",people))

if __name__ == '__main__':
    main()

