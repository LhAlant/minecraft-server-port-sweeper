from mcstatus import JavaServer
import threading

class Sweeper:
    def __init__(self, ip, bottomPort, numberOfPorts, numberOfThreads, filePath):
        self.ip = ip
        self.port = bottomPort
        self.range = numberOfPorts
        self.top_port = self.port + self.range
        self.numberOfThreads = numberOfThreads
        self.threads = []

        self.file_path = filePath

    def check_port(self):
        while self.port < self.top_port:
            port_to_check = self.port
            self.port += 1

            server = JavaServer(self.ip, port_to_check)
            try:
                status = server.status()
                with open(self.file_path, 'a') as file:
                    file.write("{}:{}\n".format(self.ip, port_to_check))

            except:
                #Just passing the error because that means there's no server on that specific port
                pass

    def start(self):

        #Creates an empty file to avoid confusion if no servers were found
        with open(self.file_path, "a") as file:
            pass

        for i in range(self.numberOfThreads):
            t = threading.Thread(target=self.check_port)
            self.threads.append(t)

        for i in range(self.numberOfThreads):
            self.threads[i].start()

        for i in range(self.numberOfThreads):
            self.threads[i].join()
