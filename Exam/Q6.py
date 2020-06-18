"""
    Loads Names and Numbers from a Phonebook file into a usable format. 
    Allows for easy lookup of numbers
    Phonebook should be in the format of:

    Name1 Number1
    Name2, Number2
"""

#Question says to call file Q6... Pretty sure it's meant to be Q10 but oh well
class PhoneBook():
    """
        Phonebook Class. Loads phonebook into memory and allows name lookup.
        Initalise with file directory/relative file directory
    """
    def __init__(self, filep): #Method documentation makes sense in __init__()
        """
            Sets up the Phonebook
            Inputs:
            0 - File Directory/Relative File Directory/File Name (Phonebook File)
        """
        self.filep = filep
        self.dict = {}
    def __str__(self):
        return f"Phone book for {self.filep}"
    def readPhoneBook(self):
        """
            Reads the Phonebook file and loads into a dictionary (self.dict) for later use. Duplicate names will be overwritten
            Outputs:
            200 - "Phone Book Read" (Ok - Success)
            400 - "Could not read phone book" (Bad Request - Error Occured. File is not found or is in an invalid format)

            self.filep must be set through the initialiser first
        """
        try:

            file = open(self.filep, "r")

            for i in file.readlines():
                name, number = i.split()
                self.dict[name] = number

            file.close()

            print("Phone book read")
        except: #Give general error if ANY error occurs, e.g. FileNotFoundError, IndexError
            print("Could not read phone book")
    def getPhoneNumber(self, contact_name):
        """
            Returns the phone number based on name as a case-sensitive input
            Input:
            contact_name: string
            
            Outputs:
            200 - Phone Number of Name (case-sensitive)
            400 - 'Could not find phone number' (Bad Request, name is not in the dict or readPhoneBook has not yet succeeded)
        """
        try:
            print(self.dict[contact_name])
        except KeyError:
            print('Could not find phone number')

#Code to test (from another file)
#from Q6 import PhoneBook

##book = PhoneBook("book.txt")
#print(book)
#book.readPhoneBook()
#book.getPhoneNumber("Carla")