from flask import Flask, render_template, request, json
import sqlite3 as sql
from database.database import Database

app = Flask(__name__, template_folder = "templates")
database = Database()

@app.route("/players", methods=["POST", "GET"])
@app.route("/players/<id>", methods=["GET"])
def players(id=None):

    (connection, cursor) = database.connect()

    if request.method == "GET" and id == None:

        print("test")
        query = f"select id, username from player"
        cursor.execute(query)
        rows = cursor.fetchall()

        players = list(map(lambda row: {
            "id": row[0],
            "username": row[1]
        }, rows))

        return app.response_class(
            response = json.dumps(players),
            status = 200,
            mimetype = "application/json"
        )

    elif request.method == "GET" and id != None:

        query = f"select id, username from player where id = '{id}'"
        cursor.execute(query)
        row = cursor.fetchone()

        if(row):
            player = {
                "id": row[0],
                "username": row[1],
            }

            return app.response_class(
                response = json.dumps(player),
                status = 200,
                mimetype = "application/json"
            )
        else:
            return app.response_class(
                status = 404
            )

    elif request.method == "POST":
        player = request.get_json()

        username = player["username"]
        query = f"insert into player (username) values ('{username}')"
        cursor.execute(query)

        connection.commit()
    
        return app.response_class(
            response = json.dumps(player),
            status = 201,
            mimetype = "application/json"
        )

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)