class Quiz:
    def display_quiz(self):
      print("welcome to the Quiz")
class Subject(Quiz):
    def Show_subject(self):
      print("subject:python")
class Exam(Quiz):
    def display_exam(self):
      print("exam failed")
a = Quiz()
s = Subject()
e = Exam()
a.display_quiz()    
s.display_quiz()     
s.show_subject()      
e.display_exam()      
e.display_quiz() 
