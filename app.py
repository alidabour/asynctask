from sanic import Sanic
from sanic.response import json
from signal import signal,SIGINT
from multiprocessing import Event
import uvloop
import asyncio
import asyncpg


app = Sanic()

@app.route("/adserver")
async def test(request):
	# conn = await asyncpg.connect('postgres://aglziifkvghija:e88c7cf121436073c5f21b1d658e1b0d2250d697a281b23ad129564d8fa39226@ec2-174-129-193-169.compute-1.amazonaws.com:5432/dbda36k41dj2f2',password='e88c7cf121436073c5f21b1d658e1b0d2250d697a281b23ad129564d8fa39226')
	# await conn.execute('''
	# 	INSERT INTO logquery(query) VALUES($1)
	# 	''', str(request.args))
	# await conn.close()
	return json({"hello": request.args})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug = False)