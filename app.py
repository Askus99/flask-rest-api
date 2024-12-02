from flask import Flask
from routes.DrugRoutes import app_drug_item

app = Flask(__name__)

app.register_blueprint(app_drug_item, url_prefix='/item/drugs')

if __name__ == '__main__':
    app.run(debug=True)