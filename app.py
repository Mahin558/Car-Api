from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('bmws.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET'])
def home():
    query = request.args.get('query', '')
    results = []
    if query:
        conn = get_db()
        results = conn.execute('''
            SELECT * FROM bmws
            WHERE LOWER(model) LIKE ?
            OR LOWER(engine_code) LIKE ?
            OR LOWER(generation) LIKE ?
        ''', (f'%{query.lower()}%', f'%{query.lower()}%', f'%{query.lower()}%')).fetchall()
        results = [dict(row) for row in results]
        conn.close()
    return render_template('index.html', results=results, query=query)

@app.route('/bmws', methods=['GET'])
def get_bmws():
    conn = get_db()
    cars = conn.execute('SELECT * FROM bmws').fetchall()
    conn.close()
    return jsonify([dict(car) for car in cars])

if __name__ == '__main__':
    app.run(debug=True)