from agent import createAgent
import os

def test_file_creation():
    name = "test"
    port = 4557
    blocks = []
    fh = open('server_template.ck', 'r')
    template = fh.read()
    fh.close()   
    createAgent(port).create_agent(template, name,blocks)
    assert(os.path.exists(os.getcwd() + '/agents/' + name + '.ck'))
    with open(os.getcwd() + '/agents/' + name + '.ck', 'r') as fh:
        data = fh.read()
    assert("int port <= " + port in data)
    assert("string name <= " + name in data)
    os.remove(os.getcwd() + '/agents/' + name + '.ck')

def test_two_file_creation():
    name = ["test", "baz"]
    port = 4557
    blocks = []
    fh = open('server_template.ck', 'r')
    template = fh.read()
    fh.close()   
    createAgent(port).create_agent(template, name,blocks)
    assert(os.path.exists(os.getcwd() + '/agents/test.ck'))
    assert(os.path.exists(os.getcwd() + '/agents/baz.ck'))
    os.remove(os.getcwd() + '/agents/test.ck')
    os.remove(os.getcwd() + '/agents/baz.ck')

def test_create_command():
    cmd = createAgent().run_command(['foo', 'bar', 'baz'])
    assert(cmd == " foo.ck bar.ck baz.ck")
    assert(cmd != " foo.ck bar.ck baz.ck moe.ck")