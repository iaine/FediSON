'''
Prototype for the ChucK work. 

Simple creation of a ChucK file from a template and then run it. 
'''
import os
import signal
import subprocess
from string import Template
from glob import glob

from agentException import agentException

class createAgent:

    def __init__(self, port_num, name) -> None:
        fh = open(name, 'r')
        self.template = Template(fh.read())
        fh.close()
        self.port = port_num
        self.base_dir = os.getcwd()
        self.agent = None


    def create_agent(self, name, blocks):
        server = self.template.safe_substitute({"name":name, "port":self.port, 
                                        "blocks": ','.join([ b.replace('\n','') for b in blocks.split(';')])
                                        })
        with open(self.base_dir + "/agents/" + name + ".ck", 'w') as f:
            f.write(server)

        
    def create_agents(self, dataset):
        for d in dataset:
            data = d.split(',')
            name = data[0]
            blocks = data[1]
            self.create_agent(name, blocks)

    def run_command(self, command_string):
        try:
            print ("`which chuck` {}".format(command_string))
            self.agent = subprocess.Popen(["`which chuck` {}".format(command_string)], shell=True, \
                                        stderr=subprocess.PIPE, stdout= subprocess.PIPE)
        except Exception as e:
            raise agentException(e)

    def run_agents(self, agents=[]):
        '''
            Run each agent. 
            If not set, run all agents
            @param agents - a defines list of agents that can be run
        '''
        command = ""
        if len(agents) == 0:
            for name in glob("agents/*.ck"):
                command +=  name + " "
        else:
            for name in agents:
                command +=  name + " "

        return command
                    
    
    def stop_agents(self):

        self.agent.kill()
        self.agent.wait()
