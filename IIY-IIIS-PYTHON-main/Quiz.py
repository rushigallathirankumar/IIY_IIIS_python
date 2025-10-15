class Quiz:
    def display(self):
      print("welcome to the Quiz")
class Subject(Quiz):
    def Show(self):
      print("subject:python")
a = Quiz()
s = Subject()
s.display()
s.Show()
a.display()
