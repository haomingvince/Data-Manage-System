import pymysql


def addUser(username, password):
    # connect to mysql db
    database = pymysql.connect("localhost", "root", "19970920", "sys")

    # create a cursor()
    cursor = database.cursor()
    comm1 = 'insert into user (username,password) values ("{}","{}")'.format(username, password)
    cursor.execute(comm1)
    database.commit()
    database.close()


def deleUser(username, password):
    # connect to mysql db
    database = pymysql.connect("localhost", "root", "19970920", "sys")

    # create a cursor()
    cursor = database.cursor()
    comm2 = 'delete from user where username = "{}" and password = "{}"'.format(username, password)
    cursor.execute(comm2)
    database.commit()
    database.close()


def ifExist(username):
    # connect to mysql db
    database = pymysql.connect("localhost", "root", "19970920", "sys")

    # create a cursor()
    cursor = database.cursor()
    comm3 = 'select * from user where username = "{}"'.format(username)
    cursor.execute(comm3)
    result = cursor.fetchall()
    database.close()
    if len(result) == 0:
        return False
    else:
        return True


def chkPwd(username, password):
    # connect to mysql db
    database = pymysql.connect("localhost", "root", "19970920", "sys")

    # create a cursor()
    cursor = database.cursor()
    comm4 = 'select * from user where username = "{}" and password = "{}"'.format(username, password)
    cursor.execute(comm4)
    result = cursor.fetchall()
    database.close()
    if len(result) == 0:
        return False
    else:
        return True


def updateUserPwd(username, origpwd, newpwd):
    # connect to mysql db
    database = pymysql.connect("localhost", "root", "19970920", "sys")

    # create a cursor()
    cursor = database.cursor()
    comm5 = 'UPDATE user set password="{}" where username="{}" and password = "{}"'.format(newpwd, username, origpwd)
    cursor.execute(comm5)
    result = cursor.fetchall()
    database.commit()
    database.close()
    if len(result) == 0:
        return False
    else:
        return True

