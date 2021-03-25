from flask import Flask
from database.database import Database
from configuration import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

# Application flask, représente le serveur
app = Flask(__name__, template_folder = "templates")

# Accès à la base de données
database = Database(
    host = DATABASE_HOST,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD,
    database_name = DATABASE_NAME
)