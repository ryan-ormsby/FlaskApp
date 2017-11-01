import os
import sqlite3

db_filename = 'addrisk.db'
schema_filename = 'addrisk_schema.sql'

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print 'Creating schema'
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print 'Inserting initial data'

        conn.execute("""
        insert into reviews (nickname, review)
        values ('AlexR', 'Wow cool flask app')
        """)

        #conn.execute("""
        #insert into reviews (nickname, review)
        #values (JordanL', 'amazing')
        #""")

        #conn.execute("""
        #insert into reviews (nickname, review)
        #values (JamieD', 'this sucks')
        #""")

    else:
        print 'Database exists, assume schema does, too.'
