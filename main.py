from flask import Flask, render_template
import json
import os

if not os.path.exists('cities.json'):
    with open('cities.json', 'w') as file:
        json.dump({}, file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/stats/<int:city_id>/<city_name>')
def stats(city_id, city_name):
    with open('cities.json', 'r+') as file:
        data = json.load(file)
        if str(city_id) not in data:
            data[str(city_id)] = {
                'name': city_name,
                'search_count': 1
            }
        else:
            data[str(city_id)]['search_count'] += 1
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()
    return 'Stats updated successfully'

@app.route('/get-stats')
def get_stats():
    with open('cities.json', 'r') as file:
        data = json.load(file)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug=True)
