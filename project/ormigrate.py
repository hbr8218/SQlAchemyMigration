# from flask import Flask
# from flask_mongoalchemy import MongoAlchemy

# app = Flask(__name__)

# app.config['MONGOALCHEMY_DATABASE']='test'
# # app.config['MONGOALCHEMY_CONNECTION_STRING'] = "mongodb://hbr8218:mysqL2016@cluster0-shard-00-00-ygyqk.mongodb.net:27017,cluster0-shard-00-01-ygyqk.mongodb.net:27017,cluster0-shard-00-02-ygyqk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
# app.config['MONGOALCHEMY_CONNECTION_STRING']='mongodb+srv://hbr8218:mysqL2016@cluster0-ygyqk.mongodb.net/test?retryWrites=true&w=majority'

# db = MongoAlchemy(app)

# class Example(db.Document):
#     name = db.StringField
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myselfHassanbarraza8218@gmail.com'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysqL2016@localhost/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)