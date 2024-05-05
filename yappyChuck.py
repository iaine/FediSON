'''
yappyChuck - yet another python pyChuck
File to stop and start service
'''

import os
import subprocess

from pythonosc import udp_client

class Server():

    def __init__(self, port_number) -> None:
        self.port = port_number
        self.process = None

    def start(self, command_string):
        try:
            self.process = subprocess.Popen(["`which chuck` {}".format(command_string)], shell=True, \
                                        stderr=subprocess.PIPE, stdout= subprocess.PIPE)
            if not self.process.pid:
                raise Exception('No server')
            print(self.process.pid)
        except Exception as e:
            print("Server Error {}".format(e))

    def stop(self):
        pid =  self.process.pid
        self.process.terminate()

        #let's catch any zombies
        try:
            os.kill(pid, 0)
            self.process.kill()
            print("Forced kill")
        except OSError as e:
            print ("Terminated gracefully")

class Client():

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def send(self, channel, message):
        '''
           Function to send the message
        '''
        try:
            client = udp_client.SimpleUDPClient(self.host, self.port)
            client.send_message("/{}".format(channel), message)
        except Exception as e:
            print("Client Exception {}".format(e))