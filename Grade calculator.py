def inputmark():
    print('Enter student ID: ')
    id=int(input())
    print('Enter exam score: ')
    exam=int(input())
    print('Enter all test score: ')
    mark1=int(input())
    mark2=int(input())
    mark3=int(input())
    mark4=int(input())  
    mark5=int(input())
    mark6=int(input())
    mark7=int(input())
    sum =(mark1+mark2+mark3+mark4+mark5+mark6+mark7)
    avg = sum/7
    print('Test average is: '+str(avg))
    print('Final mark is: ',compute_mark(avg,exam))
    print('Letter grade is: ',getgrade(compute_mark(avg,exam)))
    print_Remark(getgrade(compute_mark(avg,exam)))
    return avg
def compute_mark(avg,exam):
    final_mark=0.4*avg+0.6*exam
    return final_mark
def getgrade(final_mark):
    if 90<=final_mark<=100:
        grade='A'
    elif 80<=final_mark<=89:
        grade='B'
    elif 70<=final_mark<=79:
        grade='C'
    elif 60<=final_mark<=69:
        grade='D'    
    else:
        grade='F'
    return grade    
def print_Remark(grade):
    if grade=='A':
        print('Remark : Excellent')
    elif grade=='B':
        print('Remark : Very good')
    elif grade=='C':
        print('Remark : Good')
    elif grade=='D':
        print('Remark : Satisfactory')
    elif grade=='F':
        print('Remark: Poor')
inputmark()        