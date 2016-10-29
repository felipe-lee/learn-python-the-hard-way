import sqlite3


class HaveniteDatabaseManager(object):

    def __init__(self, *args, **kwargs):
        connection = sqlite3.connect(database='havenite.sqlite3')
        self.c = connection.cursor()

        self.c.execute("""PRAGMA foreign_keys = ON;""")

    def add_race(self):
        self.c.execute("""
        INSERT INTO RACE(NAME)
        VALUES (
        );""")

    def setup_database(self):
        self.c.execute("""
        CREATE TABLE RACE (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME CHAR(50) NOT NULL
        );""")

        self.c.execute("""
        CREATE TABLE CHARACTER (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LASTNAME CHAR(50) NOT NULL,
            FIRSTNAME CHAR(50) NOT NULL,
            SAVENAME CHAR(50) NOT NULL,
            SAVEDATE DATETIME DEFAULT (DATETIME('now', 'localtime')),
            RACE INTEGER,
            HEALTH INTEGER NOT NULL,
            STAMINA INTEGER NOT NULL,
            STRENGTH INTEGER NOT NULL,
            DEFENSE INTEGER NOT NULL,
            AGILITY INTEGER NOT NULL,
            ENDURANCE INTEGER NOT NULL,
            CHARISMA INTEGER NOT NULL,
            LUCK INTEGER NOT NULL,
            FOREIGN KEY (RACE) REFERENCES RACE(ID) ON DELETE CASCADE,
            CONSTRAINT CHARACTERSAVESTATE UNIQUE (FIRSTNAME, LASTNAME, SAVENAME)
        );""")

        self.c.execute("""
        CREATE TABLE ITEMTYPE (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TYPE CHAR(50) NOT NULL,
            DAMAGE INTEGER,
            DEFENSE INTEGER,
            HEALTHREGEN INTEGER,
            STAMINAREGEN INTEGER,
            DURABILITY INTEGER NOT NULL,
            DESCRIPTION CHAR(100)
        );""")

        self.c.execute("""
        CREATE TABLE ITEM (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME CHAR(50) NOT NULL,
            ITEMTYPE INTEGER,
            FOREIGN KEY (ITEMTYPE) REFERENCES ITEMTYPE(ID) ON DELETE CASCADE
        );""")

        self.c.execute("""
        CREATE TABLE INVENTORY (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            INVENTORYLIMIT INTEGER NOT NULL,
            CHARACTER INTEGER,
            FOREIGN KEY (CHARACTER) REFERENCES CHARACTER(ID) ON DELETE CASCADE
        );""")

        self.c.execute("""
        CREATE TABLE INVENTORYITEM (
            INVENTORY INTEGER,
            ITEM INTEGER,
            FOREIGN KEY (INVENTORY) REFERENCES INVENTORY(ID) ON DELETE CASCADE,
            FOREIGN KEY (ITEM) REFERENCES ITEM(ID) ON DELETE CASCADE
        );""")

    def reset_tables(self):
        self.c.execute("""DROP TABLE RACE""")
        self.c.execute("""DROP TABLE CHARACTER""")
        self.c.execute("""DROP TABLE ITEMTYPE""")
        self.c.execute("""DROP TABLE ITEM""")
        self.c.execute("""DROP TABLE INVENTORY""")
        self.c.execute("""DROP TABLE INVENTORYITEM""")

        self.setup_database()
