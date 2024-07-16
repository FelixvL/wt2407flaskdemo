import mysql.connector


def optellen(nummer1, nummer2):
    print("getal 1 =", nummer1)
    print("getal 2 =", nummer2)
    print("uitkomst = ", nummer1 + nummer2)
    return "uitkomst ="+str(nummer1 + nummer2)

def volgendefunctie():
    mydb = mysql.connector.connect(
    host="localhost",  #port erbij indien mac
    user="root",
    password="root",
    database="abc"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM schip")

    myresult = mycursor.fetchall()

    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data
