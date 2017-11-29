from sanic import Sanic
from sanic.response import text
import asyncio
import asyncpg
import os
import urllib.parse


app = Sanic()
urllib.parse.uses_netloc.append("postgres")
url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

@app.route("/adserver")
async def test(request):
	# Connect to database
	conn = await connectDB()
	# Insert request args 
	await insert_query(conn,str(request.args))
	# Close database connection
	await conn.close()
	# Return "OK" HTTP 200 
	return text("OK",status=200)

async def connectDB():
	"""Connect to postgresql database using 
	asyncpg and data from urlib"""
	conn = await asyncpg.connect(database=url.path[1:],
		user=url.username,
		password=url.password,
		host=url.hostname,
		port=url.port)
	return conn

async def insert_query(conn,query):
	"""Insert request args into 
	logquery table """
	await conn.execute('''
		INSERT INTO logquery(query) VALUES($1)
		''', str(query))


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug = False)