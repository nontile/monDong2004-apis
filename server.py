import os
import config
from flask import Flask
from flask_restful import Api
from project_repo.resource import ProjectRepo

app = Flask(__name__)

mode = os.environ.get('MODE', 'local')
if mode == 'dev':
    app.config.from_object(config.DevelopmentConfig)
elif mode == 'local':
    app.config.from_object(config.LocalConfig)
elif mode == 'prd':
    app.config.from_object(config.ProductionConfig)
else:
    raise ValueError('Invalid environment name')
print(mode)


api = Api(app)
api.add_resource(ProjectRepo, '/p1')

from flask_restful import Resource
class Test(Resource):
    def get(self, _id):
        return {"test": _id}


api.add_resource(Test, '/<string:_id>')

if __name__ == '__main__':
    from init_db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=8080)
