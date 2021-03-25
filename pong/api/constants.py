from flask import Flask
from database.database import Database

# Application flask, représente le serveur
app = Flask(__name__, template_folder = "templates")

# Accès à la base de données
database = Database()