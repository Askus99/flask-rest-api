from models.DrugModel import DrugModel
from flask import jsonify, request, json

class DrugController:
    @staticmethod
    def index():
        drug_id = request.args.get('id')
        if drug_id:
            try:
                data = DrugModel().find(drug_id)
            except Exception as err:
                print(err)
                return DrugController().format_return('failed', err, 400)
            return DrugController().format_return('OK', data, 200)
        try:
            data = DrugModel().all()
        except Exception as err:
            print(err)
            return DrugController().format_return('failed', err, 400)
        return DrugController().format_return('OK', data, 200)
    
    @staticmethod
    def store():
        data = json.loads(request.data)
        try:
            result = DrugModel().store(data)
        except Exception as err:
            print(err)
            return DrugController().format_return('failed', str(err), 400)
        return DrugController().format_return('created', result, 201)
        

    @staticmethod
    def update(drug_id):
        data = json.loads(request.data)
        try:
            result = DrugModel().update(drug_id, data)
        except Exception as err:
            print(err)
            return DrugController().format_return('failed', str(err), 400)
        return DrugController().format_return('OK', result, 200)

    @staticmethod
    def delete(drug_id):
        try:
            result = DrugModel().delete(drug_id)
        except Exception as err:
            print(err)
            return DrugController().format_return('failed', str(err), 400)
        return DrugController().format_return('OK', result, 200)

    @staticmethod
    def format_return(status, data, status_code):
        return jsonify({
            'status_code': f'{status_code}',
            'status': status,
            'data': data
            }), status_code
