from sanic import Sanic
from sanic.response import text
import asyncio
import asyncpg
import os
import urllib.parse


app = Sanic()
urllib.parse .uses_netloc.append("postgres")
url = urllib.parse.urlparse("ss")

@app.route("/adserver")
async def test(request):
	conn = await connectDB()
	await insert_query(conn,str(request.args))
	await conn.close()
	return text("OK",status=200)

async def connectDB():
	# conn = await asyncpg.connect('postgres://aglziifkvghija:e88c7cf121436073c5f21b1d658e1b0d2250d697a281b23ad129564d8fa39226@ec2-174-129-193-169.compute-1.amazonaws.com:5432/dbda36k41dj2f2',password='e88c7cf121436073c5f21b1d658e1b0d2250d697a281b23ad129564d8fa39226')
	conn = await asyncpg.connect(database=url.path[1:],
		user=url.username,
		password=url.password)
	return conn

async def insert_query(conn,query):
	await conn.execute('''
		INSERT INTO logquery(query) VALUES($1)
		''', str(query))


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug = False)