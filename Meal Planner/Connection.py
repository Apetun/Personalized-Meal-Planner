import oracledb

conn = None
try:
    # create a connection object
    conn = oracledb.connect(
    user="jeffin",
    password="jancy123",
    dsn="localhost/xe")
    dataInsertionTuples = [
        (1, 'John', 'Doe', 'password123', 1),
        (2, 'Alice', 'Johnson', 'securepwd', 3)
    ]


    # get a cursor object from the connection
    cur = conn.cursor()

    # do something with the database
    sqlTxt = 'INSERT INTO user_account\
                (userid,fname,lname,password,al_id)\
                VALUES (:1, :2, :3,:4,:5)'
    # execute the sql to perform data extraction
    cur.executemany(sqlTxt, dataInsertionTuples)

    rowCount = cur.rowcount
    print("number of inserted rows =", rowCount)

    # commit the changes
    conn.commit()
except Exception as err:
    print('Error while connecting to the db')
    print(err)
finally:
    if(conn):
        # close the cursor object to avoid memory leaks
        cur.close()

        # close the connection object also
        conn.close()
print("execution complete!")