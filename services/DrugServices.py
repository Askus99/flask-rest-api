from connection import read, write
from services.interfaces.Item import Item
from uuid import uuid4

class DrugServices(Item):
    def __init__(self):
        pass
    
    def all(self):
        return read(self.jsondata)
    
    def store(self, obj):
        existing = read(self.jsondata)
        
        obj["id"] = str(uuid4())
        obj["deleted"] = False
        obj["subitem"] = self.subitem
        existing.append(obj)
        write(self.jsondata, existing)
        return obj

    def find(self, id):
        data = read(self.jsondata)
        for i in data:
            if i["id"] == id:
                return i
        return None
    
    def update(self, id, obj):
        data = read(self.jsondata)
        for i in data:
            if i["id"] == id:
                i["name"] = obj["name"]
                i["price"] = obj["price"]
                break
        write(self.jsondata, data)
        return obj
    
    def delete(self, id):
        data = read(self.jsondata)
        for i in data:
            if i["id"] == id:
                i["deleted"] = True
                break
        write(self.jsondata, data)
        return id


