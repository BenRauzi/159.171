from Q6 import PhoneBook

book = PhoneBook("book.txt")
book.readPhoneBook()
book.getPhoneNumber("Bert")
print(book)
print(book.dict)