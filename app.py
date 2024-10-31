# Rooms service microservice
from flask import Flask, jsonify, request
import sqlite3

#Allows for updating availability, check availability and showcase list of all rooms

app = Flask(__name__)

#Update availability
@app.route('/room/availability', methods=["PUT"])
def update_room_availability():

    #Extract room number from request body
    data = request.json
    room_number = data.get("room_number")

    # Update the database
    with sqlite3.connect("/app/data/rooms.db") as conn:
        cur = conn.cursor()
        cur.execute("UPDATE rooms SET availability = NOT availability WHERE room_number = ?",(room_number,))
        if cur.rowcount == 0:
            return "Unable to update availability", 400
        conn.commit()

        # Check the result
        cur.execute("SELECT room_number, availability FROM rooms WHERE room_number = ?",(room_number,))
        result = cur.fetchone()

        # Return the result 
        if result is None:
            return "We were unable to find the room and therefore couldnt update the status", 400
        else:
            return f'(Room number:{room_number} availability is now set to {result[1]})', 200
    
#Check availability
@app.route('/room/availability', methods=["GET"])
def check_availability():

    #Extract room number from arguments &?
    room_number = request.args.get("room_number")

    #Query the database
    with sqlite3.connect('/app/data/rooms.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT availability FROM rooms WHERE room_number = ?", (room_number,))
        result = cur.fetchone()

    if result is None:
        return "We were unable to find the room!", 400
    else:
        return jsonify(result[0]), 200

#List of all rooms
@app.route('/rooms', methods=["GET"])
def get_all_rooms():

    with sqlite3.connect('/app/data/rooms.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms")
        result = cur.fetchall()
        if not result:
            return "We were unable to find any rooms!", 400
        else: 
            # OBS CHECK THE RETURN FORMAT
            return result, 200
        
#Get room type
@app.route('/room/type/<int:room_number>',methods=["GET"])
def get_room_type(room_number):
    with sqlite3.connect("/app/data/rooms.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT room_type FROM rooms WHERE room_number = ?",(room_number,))
        result = cur.fetchone()
        if result is None:
            return "Couldnt find the room", 400
        else:
            return result[0], 200

        
#Update cleaning
@app.route("/room/cleaning", methods=["PUT"])
def update_cleaning():
    data = request.json

    room_number = data.get("room_number")
    with sqlite3.connect("/app/data/rooms.db") as conn:
        cur = conn.cursor()
        cur.execute("UPDATE rooms SET cleaned_status = NOT cleaned_status WHERE room_number = ?", (room_number,))
        if cur.rowcount == 0:
            return "Couldnt update cleaning status",400
        conn.commit()

        cur.execute("SELECT room_number, cleaned_status FROM rooms WHERE room_number = ?", (room_number,))
        result = cur.fetchone()

        return f'(Room number:{room_number} cleaned status is now set to {result[1]})', 200
    

#Send all data
@app.route('/rooms/data', methods=["GET"])
def get_rooms_data():
    with sqlite3.connect('/app/data/rooms.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms")
        data = cur.fetchall()

        #Check the response
        if not data:
            #response is empty
            return "There was an error trying to retrieve all the data!", 400
        return data, 200


        


app.run(debug=True, host="0.0.0.0")