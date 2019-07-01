#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3


# In[ ]:


def set_spiele(liga):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = 'CREATE TABLE {liga} (game_id INTEGER PRIMARY KEY, team1_id INTEGER NOT NULL, tore_heim INTEGER, tore_aus INTEGER, team2_id INTEGER NOT NULL, date DATETIME )'.format(liga=liga)
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print( 'table ', liga, ' has been set')

def reset_spiele(liga):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE {liga}'.format(liga=liga))
    sql_command = 'CREATE TABLE {liga} (game_id INTEGER PRIMARY KEY, team1_id INTEGER NOT NULL, tore_heim INTEGER, tore_aus INTEGER, team2_id INTEGER NOT NULL, date DATETIME )'.format(liga=liga)
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print( 'table ', liga, ' has been reset')

def read_spiele(liga):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM {liga}'.format(liga=liga))
    row = cursor.fetchall()
    connection.close()
    return row
   
def select_spiel_id(team1_id, date):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "SELECT game_id FROM bundesliga WHERE team1_id= (?) AND date= (?)"
    cursor.execute(sql_command, [team1_id, date])
    spiel_id = cursor.fetchone()
    connection.close()
    return spiel_id    


# In[ ]:


def insert_bundesliga(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO bundesliga (team1_id, tore_heim, tore_aus, team2_id, date) VALUES (?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('stored in bundesliga')

def insert_liga2(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO liga2 (team1_id, tore_heim, tore_aus, team2_id, date) VALUES (?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('stored in liga2')

def insert_liga3(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO liga3 (team1_id, tore_heim, tore_aus, team2_id, date) VALUES (?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('stored in liga3')


# In[ ]:


def set_quote():
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = 'CREATE TABLE quote (id INTEGER PRIMARY KEY, date DATETIME, spiel_id INTEGER NOT NULL, quote_sieg INTEGER, quote_un INTEGER, quote_lost INTEGER)'
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print( 'table quote has been set')

def drop_quote():
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE quote')
    connection.commit()
    connection.close()
    print( 'drop table quote')

def insert_quote(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO quote (date, spiel_id, quote_sieg, quote_un, quote_lost) VALUES (?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('stored in quote')


# In[ ]:


def set_teams():
    connection = sqlite3.connect("teams.db")
    cursor = connection.cursor()
    sql_command = 'CREATE TABLE teams (team_id INTEGER PRIMARY KEY, name VARCHAR(30) NOT NULL, link VARCHAR(60) NOT NULL UNIQUE)'
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print('Create teams tbl')

def drop_teams():
    connection = sqlite3.connect("teams.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE teams')
    connection.commit()
    connection.close()
    print( 'drop table teams')
    
def insert_teams(values):
    connection = sqlite3.connect("teams.db")
    cursor = connection.cursor()    
    sql_command = "INSERT INTO teams (name, link) VALUES (?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('insert teams')
    
def read_teams():
    connection = sqlite3.connect("teams.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM teams')
    row = cursor.fetchall()
    connection.close()
    return row

def read_team_link():
    connection = sqlite3.connect("teams.db")
    cursor = connection.cursor()
    cursor.execute('SELECT link FROM teams')
    row = cursor.fetchall()
    connection.close()
    return row

def select_team_id(link):
    connection = sqlite3.connect("teams.db")
    cursor = connection.cursor()
    sql_command = "SELECT team_id FROM teams WHERE link LIKE (?)"
    cursor.execute(sql_command, link)
    team_id = cursor.fetchone()
    connection.close()
    return team_id

def try_select_team_id(name):
    connection = sqlite3.connect("teams.db")
    cursor = connection.cursor()
    sql_command = "SELECT team_id FROM teams WHERE name LIKE (?)"
    cursor.execute(sql_command, name)
    team_id = cursor.fetchone()
    connection.close()
    return team_id

