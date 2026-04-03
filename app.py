from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

bmws = [
    {"id": 1, "model": "E30 M3", "generation": "E30", "years": "1986-1991", "engine_code": "S14B23", "engine_type": "2.3L inline-4"},
    {"id": 2, "model": "E36 M3", "generation": "E36", "years": "1992-1999", "engine_code": "S50B30", "engine_type": "3.0L inline-6"},
    {"id": 3, "model": "E46 M3", "generation": "E46", "years": "2000-2006", "engine_code": "S54B32", "engine_type": "3.2L inline-6"},
    {"id": 4, "model": "E90 M3", "generation": "E90/E92/E93", "years": "2007-2013", "engine_code": "S65B40", "engine_type": "4.0L V8"},
    {"id": 5, "model": "F80 M3", "generation": "F80", "years": "2014-2018", "engine_code": "S55B30", "engine_type": "3.0L twin-turbo inline-6"},
    {"id": 6, "model": "G80 M3", "generation": "G80", "years": "2021-present", "engine_code": "S58B30", "engine_type": "3.0L twin-turbo inline-6"},
    {"id": 7, "model": "335i", "generation": "E90/E92/E93", "years": "2006-2013", "engine_code": "N54B30", "engine_type": "3.0L twin-turbo inline-6"},
    {"id": 8, "model": "135i", "generation": "E82/E88", "years": "2007-2013", "engine_code": "N55B30", "engine_type": "3.0L turbo inline-6"},
    {"id": 9, "model": "M140i", "generation": "F20/F21", "years": "2016-2019", "engine_code": "B58B30", "engine_type": "3.0L turbo inline-6"},
    {"id": 10, "model": "330d", "generation": "E46", "years": "1999-2005", "engine_code": "M57D30", "engine_type": "3.0L diesel inline-6"},
    {"id": 11, "model": "320d", "generation": "E90", "years": "2005-2013", "engine_code": "N47D20", "engine_type": "2.0L diesel inline-4"},
    {"id": 12, "model": "330i", "generation": "G20", "years": "2019-present", "engine_code": "B48B20", "engine_type": "2.0L turbo inline-4"}
]

@app.route('/', methods=['GET'])
def home():
    query = request.args.get('query', '')
    results = []

    if query:
        results = [
            car for car in bmws
            if query.lower() in car['model'].lower()
            or query.lower() in car['engine_code'].lower()
            or query.lower() in car['generation'].lower()
        ]

    return render_template('index.html', results=results, query=query)

@app.route('/bmws', methods=['GET'])
def get_bmws():
    return jsonify(bmws)

if __name__ == '__main__':
    app.run(debug=True)