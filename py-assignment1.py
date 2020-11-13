#declare variable to store the user input 
num_of_courses=int(input("How many courses did you finish?")) 
# empty list declared to be used later to contain the coures marks 
course_marks=[]
course_number=1
#creat while loop based on the number we will get from num_of_courses 
#using append method to add to the list 
while (course_number<=num_of_courses):
    course_marks.append(int(input(f"Enter your mark for course {course_number} : ")))
# printing the items of course_mark
    course_number+=1
    for item in course_marks:
        print(item)  

    total=0
    for mark in course_marks:
        total = total + mark
# printing the total marks
        print(f"Your total marks for {num_of_courses} courses is {total}")        
# finding the average by dividing the total by the length of the list using round built in function
#  to return the nearest integer 
average = round(total/num_of_courses,2)
# print the average 
print(f"Your average for your {num_of_courses} courses is {average}")
# if statment to get the grades 
if average >=90 and average<=100:
    print ("Your grade is A")
elif average >=80 and average<=89:
    print ("Your grade is B")
elif average >=70 and average<=79:
    print ("Your grade is C")
elif average >=60 and average<=69:
    print ("Your grade is D")
elif average<=59:
    print ("Your grade is F")
