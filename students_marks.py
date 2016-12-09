marks = [{"school_class":"4a","scores":[3,4,4,5,2]},
         {"school_class":"4b","scores":[5,3,4,2,3]},
         {"school_class":"4c","scores":[3,5,4,5,3]}
        ]

#считаем средний балл по школе
sum_school = len_school = 0
for mark in marks:
     sum_school += sum(mark.get("scores"))
     len_school += len(mark.get("scores"))
print("Средний балл по всей школе равен - {}".format(round(sum_school/len_school,1)))

#считаем средний балл по каждому классу
for mark in marks:
    sum_class = len_class = 0
    sum_class += sum(mark.get("scores"))
    len_class += len(mark.get("scores"))
    print("Средний балл по {} классу равен - {}".format(mark.get("school_class"),round(sum_class/len_class,1)))