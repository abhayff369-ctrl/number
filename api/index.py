from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

CSV_FILE = "data.csv"

def search_number(number):
    results = []

    with open(CSV_FILE, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["mobile"] == number:
                results.append(row)

    return results

@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "Mobile Search API Running"
    })

@app.route("/search")
def search():
    number = request.args.get("number")

    if not number:
        return jsonify({
            "success": False,
            "message": "Number parameter required"
        })

    results = search_number(number)

    if results:
        return jsonify({
            "success": True,
            "total": len(results),
            "results": results
        })

    return jsonify({
        "success": False,
        "message": "No data found"
    })

if __name__ == "__main__":
    app.run()
