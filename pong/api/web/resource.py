class Resource:
    db = None
    server = None

    def __init__(self):
        if(Resource.db == None or Resource.server == None):
            raise ValueError()
        self.db = Resource.db
        self.server = Resource.server
