from src.adapters.flask import FlaskApp
from src.adapters.mongo import MongoReportRepository

storage = MongoReportRepository()
flaskapp = FlaskApp(storage)
app = flaskapp.app

if __name__ == "__main__":
    flaskapp.run()
