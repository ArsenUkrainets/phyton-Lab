class Books():
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    #def __del__(self):
     #   print("Book:", self.name, "- was deleted")


class Junior(Books):
    def __init__(self, name, author, year, mark):
        super().__init__(name, author, year)
        self.mark = mark

    def jun_print(self):
        print("Junior Book:", self.name, "\t", self.year, "\nby", self.author)
        print("Readers mark:", self.mark)


class Senior(Junior):
    def __init__(self, name, author, year, mark, page):
        super().__init__(name, author, year, mark)
        self.page = page

    def sen_print(self):
        print("Senior Book:", self.name, " pages:", self.page, "\t", self.year, "\nby", self.author)
        print("Readers mark:", self.mark)


def inp(name, author, year):
    name = input("Book's name:")
    author = input("Author:")
    year = int(input("Year:"))
    objct = Senior(name, author, year, 0, 0)
    return objct


def create():
    name = "none"
    author = "none"
    year = 0
    choose = int(input("Choose type of book:\n1-Junior 2-Senior\n"))
    if choose == 1:
        objct = inp(name, author, year)
        objct.mark = int(input("Reader's mark:"))
        print("Element book, junior book was created")
        objct.jun_print()
    if choose == 2:
        objct = inp(name, author, year)
        objct.mark = int(input("Reader's mark:"))
        objct.page = int(input("Pages:"))
        print("Element book, junior, senior book was created")
        objct.sen_print()
    return objct

#def edit(objct):
   # objct.

y = 1
while y == 1:
    se = create()
    y = int(input("Create new book? 1-yes 2-no:"))

