from flask import Blueprint
from controller.DrugController import DrugController

app_drug_item = Blueprint('app_drug_item', __name__)
app_drug_item.add_url_rule('/', view_func=DrugController.index, methods=['GET'])
app_drug_item.add_url_rule('/store', view_func=DrugController.store, methods=['POST'])
app_drug_item.add_url_rule('/update/<drug_id>', view_func=DrugController.update, methods=['POST'])
app_drug_item.add_url_rule('/delete/<drug_id>', view_func=DrugController.delete, methods=['DELETE'])