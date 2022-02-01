import os


class Machine:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip
    
    def ping(self):
      os.system(f"ping {self.ip}")
