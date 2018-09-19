import sqlite3


SAVE_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class HaveniteDatabaseManager(object):

    def __init__(self, *args, **kwargs):
        self.connection = sqlite3.connect(database='havenite.sqlite3')

        self.connection.row_factory = sqlite3.Row

        self.c = self.connection.cursor()

        self.c.execute("""PRAGMA foreign_keys = ON;""")

    def insert_into_table(self, table, columns, data):
        if not isinstance(columns, (list, tuple, set)):
            if isinstance(columns, str):
                columns = [columns]
            else:
                raise NotImplementedError("Columns must be a list, tuple, or set.")

        if not isinstance(data, (list, tuple)):
            if isinstance(data, str):
                data = [data]
            else:
                raise NotImplementedError("Columns must be a list or tuple.")

        if len(columns) != len(data):
            raise NotImplementedError("The number of columns entered does not match the number of "
                                      "data entries entered.")

        query = 'INSERT INTO {table} ({columns}) VALUES ({params});'. \
            format(table=table.upper(), columns=', '.join(columns).upper(),
                   params=', '.join(['?' for column in columns]))

        try:
            with self.connection:
                self.c.execute(query, data)
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as err:
            instance = ''
            for i, column in enumerate(columns):
                attrib = '{0}={1}'.format(column, data[i])

                if instance:
                    instance = ', '.join([instance, attrib])
                else:
                    instance = attrib

            print 'Error saving data to the {table} table ({instance}). Error: {error}'.\
                format(table=table, instance=instance, error=err)

    def setup_database(self):
        try:
            with self.connection:
                self.c.execute("""
                CREATE TABLE RACE (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME CHAR(50) NOT NULL UNIQUE
                );""")
        except sqlite3.OperationalError as err:
            print 'Error creating "RACE" table: {0}'.format(err)

        try:
            with self.connection:
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
        except sqlite3.OperationalError as err:
            print 'Error creating "CHARACTER" table: {0}'.format(err)

        try:
            with self.connection:
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
        except sqlite3.OperationalError as err:
            print 'Error creating "ITEMTYPE" table: {0}'.format(err)

        try:
            with self.connection:
                self.c.execute("""
                CREATE TABLE ITEM (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME CHAR(50) NOT NULL,
                    ITEMTYPE INTEGER,
                    FOREIGN KEY (ITEMTYPE) REFERENCES ITEMTYPE(ID) ON DELETE CASCADE
                );""")
        except sqlite3.OperationalError as err:
            print 'Error creating "ITEM" table: {0}'.format(err)

        try:
            with self.connection:
                self.c.execute("""
                CREATE TABLE INVENTORY (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    INVENTORYLIMIT INTEGER NOT NULL,
                    CHARACTER INTEGER,
                    FOREIGN KEY (CHARACTER) REFERENCES CHARACTER(ID) ON DELETE CASCADE
                );""")
        except sqlite3.OperationalError as err:
            print 'Error creating "INVENTORY" table: {0}'.format(err)

        try:
            with self.connection:
                self.c.execute("""
                CREATE TABLE INVENTORYITEM (
                    INVENTORY INTEGER,
                    ITEM INTEGER,
                    FOREIGN KEY (INVENTORY) REFERENCES INVENTORY(ID) ON DELETE CASCADE,
                    FOREIGN KEY (ITEM) REFERENCES ITEM(ID) ON DELETE CASCADE
                );""")
        except sqlite3.OperationalError as err:
            print 'Error creating "INVENTORYITEM" table: {0}'.format(err)

    def reset_tables(self):
        error_dropping_tables = False

        try:
            with self.connection:
                self.c.execute("""DROP TABLE INVENTORYITEM;""")
        except sqlite3.OperationalError as err:
            error_dropping_tables = True
            print 'Error dropping "INVENTORYITEM" table: {0}'.format(err)

        try:
            with self.connection:
                self.c.execute("""DROP TABLE INVENTORY;""")
        except sqlite3.OperationalError as err:
            error_dropping_tables = True
            print 'Error dropping "INVENTORY" table: {0}'.format(err)

        try:
            with self.connection:
                self.c.execute("""DROP TABLE ITEM;""")
        except sqlite3.OperationalError as err:
            error_dropping_tables = True
            print 'Error dropping "ITEM" table: {0}'.format(err)

        try:
            with self.connection:
                self.c.execute("""DROP TABLE ITEMTYPE;""")
        except sqlite3.OperationalError as err:
            error_dropping_tables = True
            print 'Error dropping "ITEMTYPE" table: {0}'.format(err)

        try:
            with self.connection:
                self.c.execute("""DROP TABLE CHARACTER;""")
        except sqlite3.OperationalError as err:
            error_dropping_tables = True
            print 'Error dropping "CHARACTER" table: {0}'.format(err)

        try:
            with self.connection:
                self.c.execute("""DROP TABLE RACE;""")
        except sqlite3.OperationalError as err:
            error_dropping_tables = True
            print 'Error dropping "RACE" table: {0}'.format(err)

        if not error_dropping_tables:
            self.setup_database()
        else:
            print 'Since there was an error dropping the tables, the database was not reset properly.'
