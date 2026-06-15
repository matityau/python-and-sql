from db import *

def create_students_table():
    conn = get_connection()
    cusor = conn.cursor()
    sql=""" CREATE TABLE IF NOT EXSIST students VALUES(id INT PRIMERY KEY AUTO INCREMENT,
                                                name VARCHAR(100) NOT NULL,
                                                age INT NOT NULL,
                                                course VARCHAR(100) NOT NULL,
                                                email VARCHAR(100) UNIQUE,
                                                status  VARCHAR(20) DEFAULT 'active')"""
    cusor.execute(sql)
    conn.commit()
    cusor.close()
    conn.close()

def add_student(data:dict):
    conn = get_connection()
    cusor = conn.cursor()
    sql = "INSERT INTO students (name,age,course,email,status) VALUES (name=%s,age=%s,course=%s,email=%s,status=%s)" 
    values = (data["name"],data["age"],data["course"],data["email"],data["status"])
    cusor.execute(sql,(values))
    conn.commit()
    row = cusor.lastrowid
    cusor.close()
    conn.close()
    return row 

def all_students():
    conn = get_connection()
    cusor = conn.cursor()
    sql = "SELECT * FROM student" 
    cusor.execute(sql)
    rows = cusor.fetchall()
    cusor.close()
    conn.close()
    return rows

def get_student_by_id(student_id:int):
    conn = get_connection()
    cusor = conn.cursor()
    sql = "SELECT * FROM student WHERE id=%s" 
    cusor.execute(sql,(student_id,))
    row = cusor.fetchone()
    cusor.close()
    conn.close()
    return row

def update_student_name(student_id:int,new_name:str):
    conn = get_connection()
    cusor = conn.cursor()
    sql = "UPDATE students SET name=%s WHERE id=%s" 
    
    cusor.execute(sql,(new_name,student_id))
    conn.commit()
    row = cusor.rowcount
    cusor.close()
    conn.close()
    return row > 0

def delete_student(student_id:int):
    conn = get_connection()
    cusor = conn.cursor()
    sql = "DELETE FROM students WHERE id=%s" 
    
    cusor.execute(sql,(student_id,))
    conn.commit()
    row = cusor.rowcount
    cusor.close()
    conn.close()
    return row > 0

def count_students():
    conn = get_connection()
    cusor = conn.cursor(dictionary=True
                        )
    sql = "SELECT COUNT(*) FROM student" 
    cusor.execute(sql)
    row = cusor.fetchone()
    cusor.close()
    conn.close()
    return row