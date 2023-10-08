import psycopg2

database = "testdataset"
user = "postgres"
password = "123"
host = "localhost"
port = "5432"

#creating table

create_table_query = """
CREATE TABLE IF NOT EXISTS studentrecord(
    id SERIAL PRIMARY KEY,
    rollno INT,
    name VARCHAR(30),
    marks INT
 
);

"""

insert_data_query = """
INSERT INTO studentrecord(rollno,name,marks)
VALUES(%s,%s,%s)
"""

data_to_insert = (1, "Tushti",95)
try:
    connection = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cursor = connection.cursor()
    cursor.execute(create_table_query)
    cursor.execute(insert_data_query, data_to_insert)

    connection.commit()
    print("Table created and data inserted successfully.")

#display or Read  record
    select_query = "SELECT * FROM studentrecord where rollno=1;"
    cursor.execute(select_query)

    result = cursor.fetchall()
    for i in result:
        print("id", i[0])
        print("rollno", i[1])
        print("name",  i[2])
        print("marks", i[3])
        print("-----")

#update record from table
    cursor.execute("update studentrecord SET name='Oishi' WHERE rollno=2")
    connection.commit()
    print("Record is updated")


#delete record
    cursor.execute("delete from studentrecord WHERE rollno=1")
    connection.commit()
    print("Record is deleted")

except(Exception, psycopg2.Error) as error:
    connection.rollback()
    print("Error while connecting to PostgreSQL:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
