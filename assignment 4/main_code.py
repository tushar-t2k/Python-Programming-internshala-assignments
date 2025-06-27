# Internshala Python Programming  Assignment 4
class Book:
    copies_sold=0
    def __init__(self,title,author,publisher,price,royalty):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price
        self._royalty = royalty
        Book.copies_sold=Book.copies_sold+1
    

    def get_title(self):
        return self._title
    def set_title(self, title):
        self._title = title
    def get_author(self):
        return self._author
    def set_author(self, author):
        self._author = author
    def get_publisher(self):
        return self._publisher
    def set_publisher(self, publisher):
        self._publisher = publisher
    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price
    def get_royalty(self):
        return self._royalty
    def set_royalty(self, royalty):
        self._royalty = royalty
    title=property(get_title,set_title)
    author=property(get_author,set_author)
    publisher=property(get_publisher,set_publisher)
    price=property(get_price,set_price)
    royalty=property(get_royalty,set_royalty)

    def royalty(self,copies_sold):
        if copies_sold <= 500:
            return self._price * 0.10 * copies_sold
        elif copies_sold <= 1500:
            return (self._price * 0.10 * 500) + (self._price * 0.125 * (copies_sold - 500))
        else:
            return (self._price * 0.10 * 500) + (self._price * 0.125 * 1000) + (self._price * 0.15 * (copies_sold - 1500))
    
        
class Ebook(Book):
    def __init__(self, title, author, publisher, price, royalty, format):
        super().__init__(title, author, publisher, price, royalty)
        self._format = format
        
        

    def get_format(self):
        return self._format
    def set_format(self, format):
        self._format = format
    format=property(get_format,set_format)

    def royalty(self, copies_sold):
        base_royalty = super().royalty(copies_sold)
        gst = base_royalty * 0.12
        return base_royalty - gst

#for checking purpose:-
a=Book("Python","Tushar Tailor","T2K.Publisher",1000,1500000)
print(a.royalty(1000))
b=Ebook("Python","Tushar Tailor","T2K.Publisher",1000,1500000,"pdf")
print(b.royalty(1000))