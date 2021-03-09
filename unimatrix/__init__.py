
class MatrixPort():
    port_type = "Unknown"
    def __init__(self, matrix, id, **kwargs):
        self.matrix = matrix
        self.id = id
        self.attibs = kwargs

    def __repr__(self):
        return f"<{self.port_type} port {self.id}>"

    def __getitem__(self, key):
        return self.attribs.get(key, None)

class MatrixInput(MatrixPort):
    port_type = "Input"

class MatrixOutput(MatrixPort):
    port_type = "Output"


class Unimatrix():
    def __init__(self, **kwargs):
        self.settings = kwargs
        self.sources = {}
        self.destinations = {}
        self.routes = {}

    def __getitem__(self, key):
        pass

