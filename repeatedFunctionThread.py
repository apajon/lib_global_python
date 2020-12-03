from threading import Thread

class repeatedFunctionThread:
    def __init__(self,function, *args, **kwargs):
        self._running = False
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.thread = Thread(target = self.run, args =(self.function, ))

    def start(self):
        self._running = True
        self.thread.start()

    def terminate(self):
        self._running = False

    def join(self):
        self.thread.join()

    def stop(self):
        self.terminate()
        self.join()

    def run(self, function):
        while self._running:
            self.function(*self.args, **self.kwargs)
