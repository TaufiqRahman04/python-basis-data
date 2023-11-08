import psycopg2
from psycopg2.extras import DictCursor


db_params = {
    "dbname" : "polban1",
    "host":"localhost", 
    "port": "5432",
    "user":"postgres",
    "password":"taufiq",
}

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor(cursor_factory=DictCursor)

    cursor.execute("SELECT nim,nama FROM mahasiswa")
    
    data = cursor.fetchall()

    for row in data:
        print(dict(row)['nama'])

except (Exception, psycopg2.Error) as error:
    print("error while connecting to PostgreSQL database",error)

finally:
    if connection :
        cursor.close()
        connection.close()
        print("PostgreSQL connection is close")