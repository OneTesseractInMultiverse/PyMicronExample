from micron.abs.person_repository import (
    AbsPersonRepository
)


class Person(object):

    def __init__(self, personal_id=None, name=None, last_name=None, age=None, repo: AbsPersonRepository=None):
        self.personal_id = personal_id
        self.name = name
        self.last_name = last_name
        self.age = age
        self.repo = repo

    @property
    def full_name(self):
        return "{} {}".format(self.name, self.last_name)

    @property
    def as_dictionary(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "id": self.personal_id,
            "age": self.full_name
        }

    def parse(self, state: dict):

        if "id" in state:
            self.personal_id = state["id"]
        if "name" in state:
            self.name = state["name"]
        if "last_name" in state:
            self.last_name = state["last_name"]
        if "age" in state:
            self.age = state["age"]

    def load(self):
        if self.personal_id is not None:
            state = self.repo.get(self.personal_id)
            if state is not None:
                self.parse(state)
                return True
        return False

    def save(self) -> bool:
        return self.repo.create(person_state=self.as_dictionary)

