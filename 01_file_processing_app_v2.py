from os import name
import pypyodbc
import config
import mysql.connector
import db_connection as dbConn
class TextFile:
    def name(self):
    with open('text.txt', 'r') as f:
        for i in range(1, 10):
            f.write("\r\n" % i * i)
            f.write("\r\n" % i * i)
            f.write("\r\n" % i * i)
            f.write("\r\n" % i)
    f.close()
def FileAsk():
    if name == input() + '.txt':
        return name()
    else:
        return ValueError
def FileCheck():
    with open('text.txt') as f:
        datafile = f.readlines()
    found = False
    numbers = datafile
    for line in datafile:
        if '0,1,2,3,4,5,6,7,9' in line:
            return True
    return False
def SwitchLane():
    inp = open('text.txt','r')
    out = open('text.txt', 'w')
    prev = inp.readline()
    for line in inp:
        if line.endswith (input()):
        prev = line
        if line.endswith(input()):
            out.write(line)
            out.write(prev)
        else:
            out.write(prev)
        prev = line
        out.write(prev)
        out.close()
    inp.close()
def SwitchNu():
    with open("text.txt.", 'r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == input():
                lines[i] = line.replace(input())
        file.seek(0)
        file.writelines(lines)
    file.close()
def NewValid():
   for TextFile in file('text.txt'):
        if SwitchNu()is True:
            print('Valid')
        else:
            print('Not Valid! \n FIle content is not changed!')

mydb = mysql.connector.connect(
    host = 'localhost',
    user = "dogco",
    passwd = "" ,
    database = 'text_fpa'
)
mycursor = mydb.cursor(TextFile)
mycursor.execute("CREATE TABLE text_fpa(id INT AUTO-INCREMENT PRIMARY KEY, line_idex VARCHAR(225), data VARCHAR(225))"

class Read():
    def func_ReadData(self):
        connection = dbConn.getConnection()
        cursor = connection.cursor
        cursor.execute('Select * from text_fpa')
        for row in cursor:
            print('row %ds=r' % (row,))


class Update:
    def func_UpdateData(self):
        connection = dbConn.getConnection()
        id = input('')

        try:
            sql = "Select * From text_fpa Where Id = ?"
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t line_index\t\t\t line_number_index')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('Enter New Data To indexes in text file ')
            name = input('line_index = ')
            age = input('line_number_index = ')
            query = "Update Employee Set line_index = ?, line_number_index =? Where Id =?"
            cursor.execute(query, [line_index, line_number_index, id])
            connection.commit()
            print('Data Updated Successfully')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()


class Delete:
    def func_DeleteData(self):
        connection = dbConn.getConnection()
        id = input('')
        try:
            sql = "Select * From text_fpa Where Id = ?"
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t line_index\t\t\t line_number_index')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('Enter New Data To indexes in text file ')
            confirm = input('Are you sure to delete this record (Y/N)?')
            if confirm == 'Y':
                deleteQuery = "Delete From text_fpa Where Id = ?"
                cursor.execute(deleteQuery, [id])
                connection.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()