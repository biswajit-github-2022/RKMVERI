 # 2 b.


class Library:
    def __init__(self,title,pub_details,pub_date):
        self.title=title
        self.pub_details=pub_details
        self.pub_date=pub_date
    def check_out(self):
        return self.title,self.pub_details,self.pub_date

class Book(Library):
    def __init__(self,author,genre):
        self.author=author
        self.genre=genre
    def check_out(self):
        # super().chech_out()
        return self.genre
    

b=Book('a','b')
print(b.check_out())
    
