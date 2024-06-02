immutable_var=666,'Alex',333.333,True
print(immutable_var)
# immutable_var[1]=200 ошибка так как кортеж не поддерживает обращение по элементам
mutable_list=[777,'Ded',15.1,False]
mutable_list[1]=False
mutable_list[2]=15
mutable_list[0]='gaga'
print(mutable_list)