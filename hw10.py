from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):

    def __init__(self, phone):
         self.value = phone

    def say():
        pass
    
class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, rec):
        #print(f"{name.value} : {rec}")
        #self.data.append(f"{name.value} : {rec}")
        self.data[name.value] = rec
        return f"Add success {name.value}"
    
    def list_record(self):
        result = "Notebook: \n"
        if len(self) > 0:
            for i in self:
                phones_values = '; '.join(str(p.value) for p in ab.data[i].phones) if ab.data[i].phones else ''    
                #print(i)
                #print(self.data[i].get_phones())
                result += i + ": " + phones_values + "\n"
        else:
            result += "is blank"
        return result
    
class Record:
    def __init__(self, name, phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.add_phone(phone)
    
    def add_phone(self, phone:Phone):
        self.phones.append(phone)
        
    def get_phones(self):
        #phones_values = []
        #print(name.value)
        phones_values = '; '.join(str(p.value) for p in ab.data[name.value].phones) if ab.data[name.value].phones else ''    
        #for phone in self.phones:
            #phones_values.append(phone.value)
        return phones_values

    def edit_phone(phone):
        ...
        
    def delete_phone(name):
        ...
            


if __name__ == "__main__":

    ab = AddressBook()
    print(ab.list_record())
    name = Name("Bill")
    phone = Phone("12345")
    rec = Record(name, phone)
    print(ab.add_record(rec))
    phone = Phone("54321")
    rec.add_phone(phone)
    #print(f"rec phones values Bill: {ab.data[name.value].get_phones()}")
    print(ab.list_record())
    
    name = Name("Jill")
    phone = Phone("45")
    rec_jill = Record(name, phone)
    print(ab.add_record(rec_jill))
    phone = Phone("21")
    rec_jill.add_phone(phone)
    print(ab.list_record())

    #print(ab.list_record())
    #print(f"name.value: {name.value}")
    #print(f"rec phones values Jill: {ab.data[name.value].get_phones()}")


    # print(ab.add_record(rec))

    # print(f"abdata phones for {name.value}: {ab.data.get(name.value).get_phones()}")


    #print(rec.list_record)
    
    #ab.add_record(rec)
    
    # ab.add_record(Record(Name("Janet")))

    # for rec in ab.values():
    #     assert isinstance(rec, Record)

    # print(ab.list_record())   
    # phone2 = Phone("56784")
    # print(ab)
        
    # rec = ab["Jill"]
    # print(rec)
    
    # rec.add_phone(phone2)
    # print(rec)
    
    # rec.change_phone(Phone("56784"), Phone("99345"))
    
    # print(ab)
