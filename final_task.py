import sqlite3
import math
import sys

r = 6371 # Earth radius in km

def calc_distance(coordinate1, coordinate2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(coordinate1[0])
    lon1 = math.radians(coordinate1[1])
    lat2 = math.radians(coordinate2[0])
    lon2 = math.radians(coordinate2[1])
    
    # Calculate the difference in latitude and longitude
    dif_lat = lat2 - lat1
    dif_lon = lon2 - lon1
    
    # Calculate the arc on the surface of the Earth using the haversine formula
    a = math.sin(dif_lat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dif_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Calculate the distance
    dist = r * c
    return dist

def get_coordinates(city, cursor):
    # Try to take coordinates from the database
    try:
        cursor.execute("""select latitude, longitude 
                        from city 
                        where city = ?""", (city,))
        result = cursor.fetchone()
        if result:
            return result
        else:
            # If coordinates not found, input manualy
            print(f"City of {city} not found.")
            while True:
                try:
                    latitude = float(input(f"Input the latitude for {city}: "))
                    longitude = float(input(f"Input the longitude for {city}: "))
                    
                    # Error handling for invalid inputs
                    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
                        cursor.execute("""insert into city (city, latitude, longitude) 
                                            values (?, ?, ?)""", 
                                            (city, latitude, longitude))
                        return (latitude, longitude)
                    else:
                        print("Invalid input, try again. Latitude must be between -90 and 90 and longitude between -180 and 180.")
                except ValueError:
                    print("Invalid input, please enter a valid number.")
    # Error handling for database errors
    except sqlite3.Error as e:
        print(f"Database error: {e}")

# Establish connection to db
with sqlite3.connect("city_db.db") as connection:
    cursor = connection.cursor()
    # Create table if not exists
    cursor.execute("""create table if not exists city (
                        city_id integer primary key autoincrement,
                        city text, 
                        latitude float, 
                        longitude float)""")

    # Main loop to handle user input
    while True: 
        city1 = input("Input the first city or type 0 to exit: ")
        if city1 == "0":
            print("Ok, bye!")
            break
        # Ensuring two different cities for comparison without exiting program.
        while True:
            city2 = input("Input the second city or type 0 to exit: ")
            if city2 == "0":
                print("Ok, bye!")
                sys.exit()
            
            elif city2 == city1:
                print("You have to enter some other city")
                continue
            else:
                break

        # Calculate coordinates from the database or user input for distance calculation.
        coord1 = get_coordinates(city1, cursor)
        coord2 = get_coordinates(city2, cursor)

        # Calculate the distance and print it.
        distance = round(calc_distance(coord1, coord2), 2)
        print(f"The distance between {city1} and {city2} is {distance} kilometers.")
