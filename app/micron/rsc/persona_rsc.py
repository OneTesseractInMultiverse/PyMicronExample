from micron import (
    app,
    person_repo
)
from flask import (
    jsonify,
    request,
    url_for
)
from micron.models.person import (
    Person
)


@app.route('/api/v1/person', methods=['GET'])
def get_persons():
    return jsonify(person_repo.get_all())


@app.route('/api/v1/person/<uid>', methods=['GET'])
def get_person_by_id(uid):
    person = Person(personal_id=uid, repo=person_repo)
    if person.load():
        return jsonify(person.as_dictionary)
    return jsonify({
        "msg": "Person not found"
    }), 404


@app.route('/api/v1/person', methods=["POST"])
def create_person():
    if not request.is_json:
        return jsonify({
            "msg": "Sorry, this API only accepts JSON"
        }), 400

    state = request.get_json()
    person = Person(repo=person_repo)
    person.parse(state)
    if person.save():
        return jsonify({
            "msg": "Person created successfully"
        }), 201
    return jsonify({
        "msg": "Could not create person"
    }), 500

