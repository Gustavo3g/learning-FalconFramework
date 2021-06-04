import json,falcon

class ObjRequestClass:

    def on_get(self,req,resp):

        content = {
            'name': 'Guts',
            'age': 31,
            'contry': 'Denmark'
        }
        resp.body = json.dumps(content)

api = falcon.API()
api.add_route('/test', ObjRequestClass())
