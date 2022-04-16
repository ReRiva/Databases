import pymysql as sql


# Database manipulation functions


#Setting a variable for the connection with the database
conn_db = None

#Connecting to the databse, and passing the parameters for the connection.
def mysql_connect():
    global conn_db
    conn_db = sql.connect(host="localhost", user="root", password="root", db="employees", cursorclass=sql.cursors.DictCursor)

#Writting the querry to get the information about the employees and departments(Menu Option 1)
def get_employee_department_info():
    if(not conn_db):
        mysql_connect()
    query = "select e.name, d.name from employee e inner join dept d on e.did = d.did order by d.name, e.name;"
    #Creating a cursor, to execute the querry, setting the cursor proprieties to get all the information.
    with conn_db:
        cursor = conn_db.cursor()
        cursor.execute(query)
        query_result = cursor.fetchall()
        return query_result
