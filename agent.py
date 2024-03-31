'''
Prototype for the ChucK work. 

Simple creation of a ChucK file from a template and then run it. 
'''
import os
import signal
import subprocess
from string import Template

from agentException import agentException

class createAgent:

    def __init__(self, port_num) -> None:
        fh = open('server_template.ck', 'r')
        template = fh.read()
        fh.close()
        self.port = port_num
        self.base_dir = os.getcwd()
        self.agent = None


    def create_agent(self, template, name, blocks):
        server = template.safe_substitute({"name":name, "port":self.port, 
                                        "blocks":blocks})
        with open(self.base_dir + "/agents/" + name + ".ck", 'w') as f:
            f.write(server)
        f.closed()
        
    def create_agents(self, template, dataset):
        for name in dataset:
            name = dataset[0]
            blocks = dataset[1]
            self.create_agent(template, name, self.port, blocks)

    def run_command(self, command_string):
        try:
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
            for name in os.listdir("agents"):
                command +=  name + ".ck "
        else:
            for name in agents:
                command +=  name + ".ck "

        return command
                    
    
    def stop_agents(self):

        self.agent.kill()
        self.agent.wait()
