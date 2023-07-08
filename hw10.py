from collections import UserList

class AddressBook(UserList):
    ...
def add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, phone)
    return ab.add_rec(rec)
    
class Record:
    #current_id = 1
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    # def __init__(self):
    #     self.record = []

    def list_record(self):
        return self.record

class Field:
    ...

class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

if __name__ == "__main__":
    
    ab = AddressBook()
    print(ab)
    name = Name("Bill")
    phone1 = Phone("12345")
    rec = Record(name, phone1)
    print(rec.name)
    print(rec.list_record)
    
    # ab.add_record(rec)
    
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