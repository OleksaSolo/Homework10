from collections import UserList

class AddressBook(UserList):
    def __init__(self):
        self.data = []

    def add_record(self, rec):
        # self.data[] = rec
        return f"Add success {rec}"
    
class Record:

    def __init__(self, name, *phone):
        self.name = name
        self.phone = (i for i in range(len(phone)))

    def add(rec):
        return AddressBook.add_record(rec)

    def edit(*args):
        name = Name(args[0])
        phone = Phone(args[1])
        new_phone = Phone(args[2])

        # if CONTACTS.get(name) != None:
        #     CONTACTS.pop(name)
        #     CONTACTS[name] = phone
        #     #print(CONTACTS)
        #     return f"Update success {name} {phone}"
        # else:
        #     return f"Notebook have not {name}"
        
    def delete(name):
        ...

class Field:
    ...

class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.list = phone

if __name__ == "__main__":

    ab = AddressBook()
    # print(ab)
    name = Name("Bill")
    #phone1 = Phone("12345")
    #phone2 = Phone("54321")
    #rec = Record(name, phone1, phone2)

    print(name.value)
    # print(rec.list_record)
    
    #ab.add_record(rec)
    
    # ab.add_record(Record(Name("Jill")))
    
    # for rec in ab.values():
    #     assert isinstance(rec, Record)
    
    # phone2 = Phone("56784")
    # print(ab)
        
    # rec = ab["Jill"]
    # print(rec)
    
    # rec.add_phone(phone2)
    # print(rec)
    
    # rec.change_phone(Phone("56784"), Phone("99345"))
    
    # print(ab)
