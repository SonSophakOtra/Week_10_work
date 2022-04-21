'''
2022247_sonsophakotra
2022170_Sokornnika
20222188_DosVathanakBotra
'''





from turtle import update
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="cat_db",
    port="3306"
)


cursor = mydb.cursor()


def register_cat(cat_info):

    sql = "INSERT INTO cats (name, gender, breed, dob, description) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, cat_info)
    mydb.commit()

    print("Registration completed!\n")



def get_cats():

    sql = "SELECT * from cats"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result




def get_cat(id):
    sql = f"SELECT * FROM cats WHERE id={id}"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def update_cat(cat_info):
    id, name, gender, breed, dob, description = cat_info
    sql = f"UPDATE cats SET name='{name}', gender='{gender}', breed='{breed}', dob='{dob}', description='{description}' WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()

    print("Update completed!\n")


def remove_cat(id):
    sql = f"DELETE FROM cats WHERE id={id}"
    cursor.execute(sql)
    mydb.commit()
    print("Remove completed!\n")

