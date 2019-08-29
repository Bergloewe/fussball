#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3


# In[ ]:


def set_games():
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = 'CREATE TABLE games (game_id INTEGER PRIMARY KEY, team1_id INTEGER NOT NULL, tore_heim INTEGER, tore_aus INTEGER, team2_id INTEGER NOT NULL, date DATETIME, liga VARCHAR(20))'
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print( 'Create games tbl')

def drop_games():
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE games')
    connection.commit()
    connection.close()
    print( 'drop table games')
    
def insert_games(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO games (team1_id, tore_heim, tore_aus, team2_id, date, liga) VALUES (?,?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('insert games')

def read_games():
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM games')
    row = cursor.fetchall()
    connection.close()
    return row
   
def select_game_id(team1_id, date):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "SELECT game_id FROM games WHERE team1_id= (?) AND date= (?)"
    cursor.execute(sql_command, [team1_id, date])
    spiel_id = cursor.fetchone()
    connection.close()
    return spiel_id    


# In[ ]:


def set_quotes():
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = 'CREATE TABLE quotes (id INTEGER PRIMARY KEY, date DATETIME, game_id INTEGER NOT NULL, quote_sieg INTEGER, quote_un INTEGER, quote_lost INTEGER)'
    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print( 'Create quotes tbl')

def drop_quotes():
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE quotes')
    connection.commit()
    connection.close()
    print( 'drop table quotes')

def insert_quotes(values):
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    sql_command = "INSERT INTO quotes (date, game_id, quote_sieg, quote_un, quote_lost) VALUES (?,?,?,?,?)"
    cursor.executemany(sql_command, values)
    connection.commit()
    connection.close()
    print('insert quotes')
    
def read_quotes():
    connection = sqlite3.connect("spiele.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM quotes')
    row = cursor.fetchall()
    connection.close()
    return row


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

