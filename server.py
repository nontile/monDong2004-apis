import os
import config
from flask import Flask
from flask_restful import Api
from project_repo.resource import ProjectRepo
from samp_repo import Sample2Resource, SampleResource

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


api = Api(app)
api.add_resource(ProjectRepo, '/project')
api.add_resource(SampleResource, '/')
api.add_resource(Sample2Resource, '/user')

if __name__ == '__main__':
    from init_db import db
    db.init_app(app)
    print(mode)
    app.run(debug=True, host='0.0.0.0', port=8080)
