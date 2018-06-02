from micron.abs.person_repository import (
    AbsPersonRepository
)


class MemPersonRepository(AbsPersonRepository):

    def __init__(self):
        self.persons = []

    def get_all(self):
        return self.persons

    def get(self, personal_id: str) -> dict or None:
        for person in self.persons:
            print(person)
            if person["id"] == personal_id:
                return person
        return None

    def create(self, person_state: dict) -> bool:
        self.persons.append(person_state)
        return True
