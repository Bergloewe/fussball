#!/usr/bin/env python
# coding: utf-8





import sqlite3


# In[2]:


def reset_spiele(liga):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE {liga}'.format(liga=liga))
    sql_command = 'CREATE TABLE {liga} (game_id INTEGER PRIMARY KEY, team1 VARCHAR(30) NOT NULL, tore_heim VARCHAR(1), tore_aus VARCHAR(1), team2 VARCHAR(30) NOT NULL , date VARCHAR(30) NOT NULL)'.format(liga=liga)
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print( 'table ', liga, ' has been reset')


# In[3]:


def insert_bundesliga(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO bundesliga (team1, tore_heim, tore_aus, team2, date) VALUES (?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('stored in bundesliga')


# In[4]:


def insert_liga2(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO liga2 (team1, tore_heim, tore_aus, team2, date) VALUES (?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('stored in liga2')


# In[5]:


def insert_liga3(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO liga3 (team1, tore_heim, tore_aus, team2, date) VALUES (?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('stored in liga3')


# In[6]:


def read_spiele(liga):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM {liga}'.format(liga=liga))
    tb = cursor.fetchall()
    connection.close()
    return tb


# In[7]:


def len_spiele(liga):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('SELECT count(*) FROM {liga}'.format(liga=liga))
    print(cursor.fetchall()[0][0])
    connection.close()

