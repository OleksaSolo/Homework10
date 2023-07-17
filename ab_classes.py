from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return str(self)
        
    def __eq__(self, other):
        return self.value == other.value

class Name(Field):
    ...
    

class Phone(Field):
    ...


class Record:
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
    
    def add_phone(self, phone: Phone = None):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f"phone {phone} add to contact {self.name}"
        return f"{phone} present in phones of contact {self.name}"
    
    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[idx] = new_phone
                return f"old phone {old_phone} change to {new_phone}"
        return f"{old_phone} not present in phones of contact {self.name}"
    
    def del_phone(self, phone: Phone = None):
        i = 0
        result = ""
        for p in self.phones:
            if phone == p:
                self.phones.pop(i)
                result = f"{phone} delete from phones of contact {self.name}"
            i += 1
        if result == "":
            result = f"contact {self.name} have not phone {phone}"
        return result

    def __str__(self) -> str:
        #return f"{self.name}: {', '.join(str(p) for p in self.phones)}"
        result = f"{self.name}: {', '.join(str(p) for p in self.phones) if self.phones else ''}"
        return result
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())