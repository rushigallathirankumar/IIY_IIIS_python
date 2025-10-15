class course:
     def display_course(self):
        print("course:programming")
class module1(course):
     def show_module1(self):
        print("module:object")
class module2(course):
     def show_module2(self):
        print("module:orienteed")
m1=module1()
m2=module2()
m1.display_course()
m1.show_module1()
m2.display_course()
m2.show_module2()