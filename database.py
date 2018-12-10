#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#CONNECTION
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='', password='',
                              host='',
                              database='')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    print('\n Conectado ao banco de dados.')

#CREATING CURSOR
    cursor = cnx.cursor()

#INSERT
#  insert_query = ("INSERT INTO teste "
#               "(usuario, senha, email) "
#               "VALUES (%s, %s, %s)")

#  insert_data = ('UserTeste', '123456', 'teste@teste.com.br')

#  cursor.execute(insert_query, insert_data)

#  cnx.commit()

#  cursor.close()
#  cnx.close()

#UPDATE
#    query = ("UPDATE mailings SET statusatual = 'Testing' WHERE statusatual = 'Testando'")
#
#    cursor.execute(query)
#
#    cnx.commit()

#DELETE
#    query = ("DELETE FROM mailings WHERE statusatual = 'Erro'")
#
#    cursor.execute(query)
#
#    cnx.commit()

#SELECT
    query = ("SELECT nome, statusatual FROM mailings")

    cursor.execute(query)

    for (nome, statusatual) in cursor:
        print("{}, {} ".format(
            nome, statusatual))

    cursor.close()
    cnx.close()

input('Press ENTER to exit')
