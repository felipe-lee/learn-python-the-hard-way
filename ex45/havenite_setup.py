import sqlite3

connection = sqlite3.connect(database='havenite.sqlite3')
c = connection.cursor()

c.execute("""
CREATE TABLE Race (
    RaceID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name char(50) NOT NULL
)""")

c.execute("""
CREATE TABLE Character (
    CharacterID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    LastName char(50) NOT NULL,
    FirstName char(50) NOT NULL,
    SaveName char(50) NOT NULL,
    SaveDate datetime DEFAULT GETDATE(),
    Race INTEGER FOREIGN KEY REFERENCES Race(RaceID),
    Health INTEGER NOT NULL,
    Stamina INTEGER NOT NULL,
    Strength INTEGER NOT NULL,
    Defense INTEGER NOT NULL,
    Agility INTEGER NOT NULL,
    Endurance INTEGER NOT NULL,
    Charisma INTEGER NOT NULL,
    Luck INTEGER NOT NULL,
    CONSTRAINT uc_CharacterSaveState UNIQUE (FirstName, LastName, SaveName)
)""")

c.execute("""
CREATE TABLE ItemType (
    ItemTypeID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Type char(50) NOT NULL,
    Damage INTEGER,
    Defense INTEGER,
    Healing INTEGER,
    StaminaRegeneration INTEGER,
    Durability INTEGER NOT NULL,
    Description char(100)
)""")

c.execute("""
CREATE TABLE Item (
    ItemID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name char(50) NOT NULL,
    ItemType INTEGER FOREIGN KEY REFERENCES ItemType(ItemTypeID)
)""")

c.execute("""
CREATE TABLE Inventory (
    InventoryID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    inventoryLimit INTEGER NOT NULL,
    Character INTEGER FOREIGN KEY REFERENCES Character(CharacterID)
)""")

c.execute("""
CREATE TABLE InventoryItem (
    Inventory INTEGER FOREIGN KEY REFERENCES Inventory(InventoryID),
    Item INTEGER FOREIGN KEY REFERENCES Item(ItemID)
)""")
