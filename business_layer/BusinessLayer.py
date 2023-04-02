from persistence_layer.PersistenceLayer import PersistenceLayer


class BusinessLayer:
    def __init__(self):
        self.persistence = PersistenceLayer('localhost', 'root', 'algonquin', 'potatoes')

    def populate(self, file_path):
        return self.persistence.populate_from_csv(file_path)

    def create(self, data):
        return self.persistence.create(data)

    def read(self, data):
        return self.persistence.read(data)

    def update(self, data,updated_data):
        return self.persistence.update(data, updated_data)

    def delete(self, data):
        return self.persistence.delete(data)

    def read_all(self):
        return self.persistence.read_all()

