class Resource:
    server = None

    def __init__(self, service):
        if(Resource.server == None):
            raise ValueError()
        self.server = Resource.server
        self.service = service
        self.modelClass = self.service.modelClass