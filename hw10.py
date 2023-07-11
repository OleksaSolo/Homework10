from collections import UserList

class AddressBook(UserList):
    def __init__(self):
        self.data = {}

    def add_record(self, rec):
        #print(f"{name.value} : {rec}")
        #self.data.append(f"{name.value} : {rec}")
        self.data[name.value] = rec
        return f"Add success {rec}"
    
class Record:
    def __init__(self, name, *phone):
        self.name = name
        #self.phone = (i for i in range(len(phone)))
        #self.phones.append(i for i in range(len(phone)))
        self.phones = []
        self.phones.append(phone)
        print(f"phones list: {self.phones}")

        
    def get_phones(self):
        return self.phones

    def add_phone(phone):
        ...

    def edit_phone(phone):
        ...
        
    def delete_phone(name):
        ...
            

class Field:
    ...

class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone

if __name__ == "__main__":

    ab = AddressBook()
    name = Name("Bill")
    phone1 = Phone("12345")
    phone2 = Phone("54321")
    rec = Record(name, phone1, phone2)

    print(f"rec.phones: {rec.get_phones()}")

    print(ab.add_record(rec))
    
    name = Name("Jill")
    phone1 = Phone("45")
    phone2 = Phone("21")
    rec = Record(name, phone1, phone2)

    print(f"rec.phones: {rec.get_phones()}")

    print(ab.add_record(rec))

    print(f"abdata for {name.value}: {ab.data.get(name.value).phones}")


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
