#Creating a list
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#verifying the list
print(my_list)
# inserting value in the list
my_list.insert(1,15)
#extending my_list with another  called my_list2: [50,60,70]
my_list2= [50,60,70]
my_list.extend(my_list2)

#verifying the updated list
print(my_list)
#removing t((he last emement from my_list
my_list.pop()

#sorting in ascending order
sorted_list= sorted(my_list)
print(sorted_list)

#Findind the index of the value 30
index_of_30= my_list.index(30)
print(index_of_30)
