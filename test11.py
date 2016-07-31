class Work:
    def __init__(self, work_id):
        self.work_id = work_id
    def do(self):
        print 'doing work id' + str(self.work_id)
work_list = [Work(1),Work(2), Work(3), Work(4), Work(5), Work(6), Work(7), Work(8), Work(9), Work(10)]
import threading
class Do(threading.Thread):
    def __init__(self, work):
        threading.Thread.__init__(self)
        self.work = work
    def run(self):
        self.work.do()
for work in work_list:
    d = Do(work)
    d.start()

