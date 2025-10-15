class Course:
    def display_course(self):
      print("Course: python programming")
class Module(Course):
    def show_module(self): 
      print("Module: object-oriented programming")
class Topic(Module):
    def show_topic(self):
      print("Topic:Inheritance in python")
t = Topic()
t.display_course()
t.show_module()
t.show_topic()
m=Module()
m.display_course()
m.show_module()
c=Course()
c.display_course()
c.show_module()
c.show_topic()
