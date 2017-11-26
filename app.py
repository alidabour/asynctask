from sanic import Sanic
from sanic.response import json
from signal import signal,SIGINT
from multiprocessing import Event
import uvloop
import asyncio

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "Sanic"})

asyncio.set_event_loop(uvloop.new_event_loop())
server = app.create_server(host="0.0.0.0",port=8000,debug = False)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(server)
signal(SIGINT,lambda s,f: loop.stop())
try:
	loop.run_forever()
except:
	loop.stop()
# if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000, debug = False)