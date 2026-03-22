student_info=[["Ashmita",23],['Kristina',12],["Sushila",27],["Maya",45]]
print (student_info[1][1])
mark_list=[100,98,95,99,80]
subject_list=['math','AI','Java','o-math','os']
# for i in range(len(subject_list)):
#     print(subject_list[i],":",mark_list)
total=sum(mark_list)
print (total)
average=total/len(mark_list)
print(average)
highest=max(mark_list)
print(highest)
lowest=min(mark_list)
print(lowest)
subject_list[1]="python"
print(subject_list)
mark_list[2]=89
subject_list[2]="English"
print("Marks obtained in",subject_list[2],"is",mark_list[2])
print("Marks obtained in",subject_list[-2],"is",mark_list[-2])
print("Marks obtained in",subject_list[-2],"is",mark_list[-2] ,"and ",subject_list[-1],"is",mark_list[-1])
print("Marks obtained in",subject_list[0:3] ,"is",mark_list[0:3])
index1=mark_list.index(highest)
print (subject_list[index1])
index2=mark_list.index(lowest)
print (subject_list[index2])
Num=0
for i in range(len(mark_list)):
    if mark_list[i]==80:
        Num+=1
print ("The number of students with 80 marks",Num)
