from micron import (
    app
)
from flask import (
    jsonify,
    request,
    url_for
)

persons = [
    {
        "id": 117240449,
        "name": "Josue",
        "last_name": "Gabuardi",
        "age": 19
    },
    {
        "id": 114170498,
        "name": "Pedro",
        "last_name": "Guzman",
        "age": 28
    }
]


@app.route('/api/v1/person', methods=['GET'])
def get_persons():
    return jsonify(persons)


@app.route('/api/v1/person/<uid>', methods=['GET'])
def get_person_by_id(uid):

    for person in persons:
        if str(person['id']) == uid:
            return jsonify(person)
    return jsonify({
        "message": "The requested person was not found"
    }), 404
