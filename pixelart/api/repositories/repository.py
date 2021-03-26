class Repository:
    db = None
    
    def __init__(self):
        if(Repository.db == None):
            raise ValueError()
        self.db = Repository.db
        (self.connection, self.cursor) = self.db.connect()