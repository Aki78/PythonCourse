#1

class Publication:
  def __init__(self, name):
      self.name = name

class Book(Publication):
    def __init__(self, name, author, page_n):
        self.author = author
        self.page_n = page_n
        super().__init__(name)
    def print_information(self):
        print("name:", self.name, "author:", self.author, "page number:", self.page_n)


class Magazine(Publication):
    def __init__(self,name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print("name:", self.name, "chief_editor:", self.chief_editor)



b = Book("Campartment No. 6", "Rosa Liksom", 192)
m = Magazine("Donald Duck", "Aki Hyppa")

b.print_information()
m.print_information()

# 2 -----> Go To Exercise 9
