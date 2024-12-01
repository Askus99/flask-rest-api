from abc import ABC, abstractmethod
class Item(ABC):
    @abstractmethod
    def all():
        pass
    @abstractmethod
    def store(item_obj):
        pass
    @abstractmethod
    def find(item_id):
        pass
    @abstractmethod
    def update(item_id, item_ob):
        pass
    @abstractmethod
    def delete(item_id):
        pass
    