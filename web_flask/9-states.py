from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/states')
def states():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.route('/states/<id>')
def states_id(id):
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states_404.html')
    else:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('8-states.html', state=state, cities=cities)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
