from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from server import app
db = SQLAlchemy(app)
ma = Marshmallow(app)