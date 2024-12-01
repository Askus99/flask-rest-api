from services.DrugServices import DrugServices

class DrugModel(DrugServices):
    def __init__(self):
        self.jsondata = './tmp/data.json'