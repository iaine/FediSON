import agent
import os

def test_file_creation():
    name = "test"
    port = 4557
    blocks = []
    agent.create_agent(name, port, blocks)
    assert(os.path.exists(os.getcwd() + '/agents/' + name + '.ck'))