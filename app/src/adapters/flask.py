from flask import Flask, request, jsonify

from ..usecase.app import App
from ..domain.report import Report
from ..repository.repository import ReportRepository

APP = Flask(__name__)


class FlaskApp(App):
    storage: ReportRepository

    def __init__(self, storage: ReportRepository):
        self.storage = storage
        self.app = APP

        @self.app.route("/problems", methods=["POST"])
        def add_report():
            body = request.get_json(force=True)
            headers = dict(request.headers)
            return jsonify(self.save_report(headers=headers, body=body))

        @self.app.route("/find", methods=["POST"])
        def find_report_by_kv():
            data = request.get_json(force=True)
            dicts_list = self.find_reports_by_kv(data)
            if len(dicts_list) == 0:
                return [], 404
            else:
                return dicts_list

        @self.app.route("/find2", methods=["GET"])
        def find_report_by_hash():
            hash_value = request.args.get("h")
            if hash_value is None:
                return "Error: no input from user", 400
            elif not _is_digit(hash_value):
                return "Error: non-integer value for hash", 400
            else:
                dicts_list = self.find_reports_by_hash(int(hash_value))
                if len(dicts_list) == 0:
                    return [], 404
                else:
                    return dicts_list

    def run(self, host: str = "0.0.0.0", debug: bool = False):
        self.app.run(host=host, debug=debug)


def _is_digit(n: str) -> bool:
    """Check if string is translatable to integer."""
    try:
        int(n)
        return True
    except ValueError:
        return False
