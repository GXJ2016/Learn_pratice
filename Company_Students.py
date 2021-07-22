
class Student():
    def __init__(self, name,golar:int, will_array):
        self.student_name = name
        self.golar = golar
        self.will = will_array
        self.last = None
        pass

    def copyone(self,student):
        self.student_name = student.student_name
        self.golar = student.golar
        self.will = student.will
        self.last = student.last
        return 
        pass
    pass

class Company():
    def __init__(self, company_name, all_offer_num):
        self.company_name = company_name
        self.allcnt = all_offer_num
        self.restcnt = self.allcnt
        self.get_offer_students = []
        
    def pick_student(self, student_will_company):
        if self.restcnt > 0:
            self.get_offer_students.append()
            self.restcnt = self.restcnt -1
        pass
        pass


def process_company_pick(arg_student_will_company, company_list_all):
    for company_item in company_list_all:
        if company_item.company_name == arg_student_will_company:
            company_item.pick_student(arg_student_will_company)
            pass
        pass
    pass


def core_prcess(ordered_student_list_all):
    for student_item in ordered_student_list_all:
        for student_will in student_item.will:
            process_company_pick(student_will)
            pass
    pass

def order_golar(student_list_all):
    ordered_student_list=[]    
    tmpgolar = student_list_all[0].golar
    for i,student_item_i in enumerate(student_list_all):
        tmpgolar = student_list_all[i].golar
        tmpstudent = Student(None,0,None)
        tmpstudent.copyone(student_list_all[i])
        print ("I",i,student_item_i.student_name)
        print("++++++")

        topindex=i
        
        print("start",i,tmpgolar)
        for j,student_item_j in enumerate(student_list_all[i:]):
            print("J",j,student_item_j.student_name,student_item_j.golar, tmpgolar)
            if tmpgolar < student_item_j.golar:
                print("changed!! ",tmpgolar,student_item_j.golar)
                tmpgolar = student_item_j.golar
                topindex=j+i
                

        print("top",topindex)
        tmpstudent2 = Student(None,0,None)
        tmpstudent2.copyone(student_list_all[i])
        student_list_all[i].copyone(student_list_all[topindex])
        
        tmpstudent.copyone(student_list_all[topindex])
        
        student_list_all[topindex].copyone(tmpstudent2)
                        
        print("show<<<<<")
        for ixp in student_list_all:
            print(ixp.student_name, ixp.golar)
        print("show>>>>>>")  

        print("===============================",tmpstudent.student_name)    
        ordered_student_list.append(tmpstudent)
        
    return ordered_student_list
    pass
    




def Init_Ctx():
    studentlist=[Student("1",89,[1,2,4]),
                 Student("2",95,[1,2,3]),
                 Student("3",90,[2,4]),
                 Student("4",70,[2,3]),
                 Student("5",69,[1,4])
                 ]
    
    companylist=[
        Company(1,3),
        Company(2,4),
        Company(3,2),
        Company(4,1)        
        ]
    orderlist = order_golar(studentlist)
    return orderlist
    pass



def entry():
    orderlist = Init_Ctx()
    
    print(orderlist)
    for ix in orderlist:
        print(ix.student_name)
        pass
    pass


if __name__=="__main__":
    entry()
    print("prg end")
    pass

