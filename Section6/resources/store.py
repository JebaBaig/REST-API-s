from Flask_RESTful import Resource
from models.store import StoreModel

class Store(Resource):
    
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        
        return {'message': 'Store not found'}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f'A store with name {name} already exists'}
        
        store = StoreModel(name)
        
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store'}, 500
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store: