import sqlite3

conn = sqlite3.connect('bmws.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bmws (
        id INTEGER PRIMARY KEY,
        model TEXT NOT NULL,
        generation TEXT NOT NULL,
        years TEXT NOT NULL,
        engine_code TEXT NOT NULL,
        engine_type TEXT NOT NULL
    )
''')

cursor.executemany('''
    INSERT OR IGNORE INTO bmws VALUES (?, ?, ?, ?, ?, ?)
''', [
    (1, "E30 M3", "E30", "1986-1991", "S14B23", "2.3L inline-4"),
    (2, "E36 M3", "E36", "1992-1999", "S50B30", "3.0L inline-6"),
    (3, "E46 M3", "E46", "2000-2006", "S54B32", "3.2L inline-6"),
    (4, "E90 M3", "E90/E92/E93", "2007-2013", "S65B40", "4.0L V8"),
    (5, "F80 M3", "F80", "2014-2018", "S55B30", "3.0L twin-turbo inline-6"),
    (6, "G80 M3", "G80", "2021-present", "S58B30", "3.0L twin-turbo inline-6"),
    (7, "335i", "E90/E92/E93", "2006-2013", "N54B30", "3.0L twin-turbo inline-6"),
    (8, "135i", "E82/E88", "2007-2013", "N55B30", "3.0L turbo inline-6"),
    (9, "M140i", "F20/F21", "2016-2019", "B58B30", "3.0L turbo inline-6"),
    (10, "330d", "E46", "1999-2005", "M57D30", "3.0L diesel inline-6"),
    (11, "320d", "E90", "2005-2013", "N47D20", "2.0L diesel inline-4"),
    (12, "330i", "G20", "2019-present", "B48B20", "2.0L turbo inline-4")
])

conn.commit()
conn.close()
print("Database created successfully!")
