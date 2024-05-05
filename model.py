'''
Temporal sonification using modelling
'''
import sys
from agent import createAgent
from yappyChuck import Server, Client

data = sys.argv[1]

if not data:
    print("Usage :  python3 feditime.py <data>")
    sys.exit(0)

port = 5005
cA = createAgent(port, 'server_template.ck')

server = "server_template.ck"

try:
    with open(data, 'r') as fh:
        data = fh.readlines()

    cA.create_agents(data)

    cmd = cA.run_agents()
    #cA.run_command(cmd)

    #server = Server(port)
    #server.start(cmd)

    client = Client(port)
    client.send("a")

    #server.stop()

except Exception as e:
    print(e.with_traceback)