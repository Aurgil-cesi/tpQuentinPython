class Service:
    models = None

    def __init__(self, modelname, repository):
        self.modelsClasses = Service.models
        self.modelClass = self.modelsClasses[modelname]
        self.repository = repository
