# import the sqlite3 library to work with SQLite databases in Python
import sqlite3

# connect and open the database file database.db, the database will be created when it does not exists
conn = sqlite3.connect('database.db')
print("Opened database successfully")

# create a new table card with two columns:
# the first column cardid is the primary key and autoincrement
# the second column contains the card title
conn.execute('DROP TABLE IF EXISTS card')
conn.execute('CREATE TABLE card (cardid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT)')
print("Table card created successfully")

# insert four rows in the newly created table
conn.execute("INSERT INTO card (title) VALUES ('Happy birthday | Viking filter')")
conn.execute("INSERT INTO card (title) VALUES ('All the luck in the universe | Space filter')")
conn.execute("INSERT INTO card (title) VALUES ('Congratulations with your new dog | Dog animation')")
conn.execute("INSERT INTO card (title) VALUES ('Drivers license | Car animation')")
conn.execute("INSERT INTO card (title) VALUES ('Happy birthday | Cake animation')")
conn.execute("INSERT INTO card (title) VALUES ('Have a marvel-ous day | Thor video')")
conn.execute("INSERT INTO card (title) VALUES ('Footbal MPV award | Football field animation')")
conn.execute("INSERT INTO card (title) VALUES ('Happy Halloween! | Zombies')")
print("Cards inserted successfully")

# create a second table wish with four columns:
# the first column wishid is the primary key and autoincrement
# the second column contains the sender of the wishes
# the third column contains the message from the sender
# the fourth column contains the id of the card
conn.execute('DROP TABLE IF EXISTS wish')
conn.execute('CREATE TABLE wish (wishid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, sender TEXT, message TEXT, cardid INTEGER)')
# there are no wishes already sent, so the table stays empty
conn.execute("INSERT INTO card (title) VALUES ('Happy Halloween! | Zombies')")

# commit all changes to the database, otherwise they will be lost
conn.commit()

# close the connection
conn.close()
