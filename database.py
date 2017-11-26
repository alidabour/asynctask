import asyncio
import asyncpg
import datetime

async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect('postgres://aglziifkvghija:e88c7cf121436073c5f21b1d658e1b0d2250d697a281b23ad129564d8fa39226@ec2-174-129-193-169.compute-1.amazonaws.com:5432/dbda36k41dj2f2',password='e88c7cf121436073c5f21b1d658e1b0d2250d697a281b23ad129564d8fa39226')
    # Execute a statement to create a new table.
    await conn.execute('''
        CREATE TABLE logquery(
            id serial PRIMARY KEY,
            query text
        )
    ''')
    # Close the connection.
    await conn.close()


asyncio.get_event_loop().run_until_complete(main())
