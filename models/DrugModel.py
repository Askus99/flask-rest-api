from services.DrugServices import DrugServices

class DrugModel(DrugServices):
    def __init__(self):
        self.jsondata = './tmp/data.json'
        self.subitem = 'Drug'

    def fillable(self, data):
        required_keys = {"name", "price"}
        missing_keys = [key for key in required_keys if key not in data]

        if not missing_keys:
            pass
        else:
            raise KeyError(f"Missing keys: {', '.join(missing_keys)}")

