import psycopg2

try:
    psycopg2.connect()
    connection = psycopg2.connect(database="testi", user="user", password="salasana", host="localhost", port="port")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO testitaulu (etunimi, sukunimi) VALUES ('Jakke, Jäynä')")
    connection.commit()
except Exception as e:
    raise e
finally:
    if connection:
        cursor.close()
        connection.close()

try:
    connectionString = "dbname=testi user=user password=salasana host=localhost port=5432"
    connection2 = psycopg2.connect("dbname=test user=user password=salasana host=localhost port=5432")
    cursor2 = connection2.cursor()
    cursor2.execute("INSERT INTO testitaulu (etunimi, sukunimi) VALUES ('Jonne', Janttari')")
    connection2.commit()
except Exception as e:
    print(str(e))
finally:
    if connection2:
        cursor2.close()
        connection2.close()
