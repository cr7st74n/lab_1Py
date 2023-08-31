"""Cristian Gonzalez, 8/30/2023.This program will create a Author Class that have name, and books
with this inputs, we will create a output with all the author's books"""

class Author:
    def __init__(self, name, ):
        self.name = name
        self.books = []
        self.no_duplicate = {}

    def publish(self, title):
        for book in self.no_duplicate:
            if(title == book):
                print("this title is already used")
            else:
                print("Title added")
        self.books.append(title)
        self.no_duplicate = list(set(self.books))

    def __str__(self):
        titles = ", ".join(self.no_duplicate) or "There is no books published"
        return f' {self.name} Books : {titles}'


def main():
    Arthur_Conan = Author("Arthur Conan")

    Arthur_Conan.publish("The Adventures of Sherlock Holmes")
    Arthur_Conan.publish("The Hound of the Baskervilles")
    Arthur_Conan.publish("The Hound of the Baskervilles")
    Arthur_Conan.publish("The Adventures of Sherlock Holmes")
    
    

    print(Arthur_Conan)

main()