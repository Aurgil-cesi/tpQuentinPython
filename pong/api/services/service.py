class Service:
    db = None

    def __init__(self, modelClass):
        if(Service.db == None):
            raise ValueError()
        self.db = Service.db
        self.modelClass = modelClass
        (self.connection, self.cursor) = self.db.connect()
