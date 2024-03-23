'''
Prototype for the ChucK work. 

Simple creation of a ChucK file from a template and then run it. 
'''
import os
import subprocess

fh = open('template.ck', 'r')
template = fh.read()
fh.close()

names = []

port = 5678

blocks = []

base_dir = os.getcwd()

def create_agent(name, port, blocks):
    server = template.format(name, port, blocks)
    with open(base_dir + "/agents/" + name + ".ck", 'w') as f:
        f.write(server)
    f.closed()
    
def create_agents(names, port, blocks):
    for name in names:
        create_agent(name, port, blocks)
        

def run_agents(agents=[]):
    '''
        Run each agent 
        @param Agents - a defines list of agents that can be run
    '''
    if len(agents) ==0:
        for name in os.listdir("agents"):
            try:
                agent = subprocess.run(["`which chuck` {}.ck".format(name)], shell=True, \
                                       stderr=subprocess.PIPE, stdout= subprocess.PIPE)
            except Exception as e:
                print(e)
    else:
        for name in agents:
                try:
                    agent = subprocess.Popen(["`which chuck` {}.ck".format(name)], shell=True,\
                                            stderr=subprocess.PIPE, stdout= subprocess.PIPE)
                    agent.pid
                except subprocess.SubprocessError as se:
                    print(se)
                except Exception as e:
                    print(e)