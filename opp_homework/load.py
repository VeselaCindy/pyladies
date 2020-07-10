class Load:
    def __init__(self, path):
        self.path = path
        self.data = None

    def load(self):
        file = open(self.path)
        self.data = file.read()
        file.close()

    def show(self):
        pass
