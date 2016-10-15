# -*- coding: utf-8 -*-

class PrioQueueError(ValueError):
    pass


class PrioQue:
    def __init__(self, elist=[]):
        self.elems = list(elist)
        self.elems.sort()

    def is_empty(self):
        return self.elems == []

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self.elems[len(self.elems)-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self.elems.pop()

    def enqueue(self, e):
        i = len(self.elems) - 1
        while i >= 0:
            if self.elems[i] <= e:
                i -= 1
            else:
                break
        self.elems.insert(i+1, e)


# 基于堆结构的优先队列

class PrioQueue:
    def __init__(self, elist = []):
        self.elems = list(elist)
        if elist != []:
            self.buildheap()

    def is_empty(self):
        return self.elems == []

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('in top')
        return self.elems[0]

    def enqueue(self, e):
        self.elems.append(None)
        self.siftup(e, len(self.elems)-1)

    def siftup(self, e, last):
        elems, i, j = self.elems, last, (last-1)//2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)//2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('in pop')
            elems = self.elems
            e0 = elems[0]
            e = elems.pop()
            if len(elems) > 0:
                self.siftdown(e, 0, len(elems))
            return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self.elems, begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j] #三者中最小，上移
            i, j = j, j*2+1 #找左子结点
        elems[i] = e

    def buildheap(self):
        end = len(self.elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self.elems[i], i, end)


# 堆排序

def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin*2+1
        while j < end:
            if j+1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j+1
        elems[i] = e

    end = len(elems)
    for i in range(end//2, -1, -1):
        siftdown(elems, elems[i], i, end)
    for i in range((end-1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)


# 海关模拟程序

from random import randint, random
from queue_class import SQueue, QueueUnderflow

car_arrive_interval = (1, 2)
car_check_time = (3, 5)

class Simulation:
    def __init__(self, duration):
        self._eventq = PrioQueue()
        self._time = 0
        self._duration = duration

    def run(self):
        while not self._eventq.is_empty():
            event = self._eventq.dequeue()
            self._time = event.time()
            if self._time > self._duration:
                break
            event.run()

    def add_event(self, event):
        self._eventq.enqueue(event)

    def cur_time(self):
        return self._time


class Customs:
    def __init__(self, gate_num, duration):
        self.simulation = Simulation(duration)
        self.waitline = SQueue()
        self.duration = duration
        self.gates = [0]*gate_num
        self.total_wait_time = 0
        self.total_used_time = 0
        self.car_num = 0

    def wait_time_acc(self, n):
        self.total_wait_time += n

    def total_time_acc(self, n):
        self.total_used_time += n

    def car_count_1(self):
        self.car_num += 1

    def add_event(self, event):
        self.simulation.add_event(event)

    def cur_time(self):
        return self.simulation.cur_time()

    def enqueue(self, car):
        self.waitline.enqueue(car)

    def has_queued_car(self):
        return not self.waitline.is_empty()

    def next_car(self):
        return self.waitline.dequeue()

    def find_gate(self):
        for i in range(len(self.gates)):
            if self.gates[i] == 0:
                self.gates[i] = 1
                return i
        return None

    def free_gate(self, i):
        if self.gates[i] == 1:
            self.gate[i] = 0
        else:
            raise ValueError('Clear gate error.')

    def simulate(self):
        Arrive(0, self)
        self.simulation.run()
        self.statistics()

    def statistics(self):
        print("Simulate" + str(self.duration) + "minutes, for"
              + str(len(self.gates)) + "gates")
        print(self.car_num, "cars pass the customs")
        print("Avarage waiting time:",
              self.total_wait_time / self.car_num)
        print("Avarage passing time:",
              self.total_used_time / self.car_num)
        i = 0
        while not self.waitline.is_empty():
            self.waitline.dequeue()
            i += 1
        print(i, "cars are in waiting line.")


class Car:
    def __init__(self, arrive_time):
        self.time = arrive_time

    def arrive_time(self):
        return self.time


class Event:
    def __init__(self, event_time, customs):
        self.ctime = event_time
        self.customs = customs

    def __lt__(self, other_event):
        return self.ctime < other_event.ctime

    def __le__(self, other_event):
        return self.ctime <= other_event.ctime

    def time(self):
        return self.ctime

    def run(self, time, event_name):
        pass


def event_log(time, name):
    print("Event:" + name + ",happens at" + str(time))


class Arrive(Event):
    def __init__(self, arrive_time, customs):
        Event.__init__(self, arrive_time, customs)
        self.customs.add_event(self)

    def run(self):
        time, customs = self.ctime, self.customs
        event_log(time, "car arrive")
        Arrive(time + randint(*car_arrive_interval))
        car = Car(time)
        i = customs.find_gate()
        if i is not None:
            event_log(time, "car check")
            Leave(time + randint(*car_check_time), i, car, customs)
        else:
            customs.enqueue(car)


class Leave(Event):
    def __init__(self, leave_time, gate_num, car, customs):
        Event.__init__(self, leave_time, customs)
        self.car = car
        self.gate_num = gate_num
        self.customs.add_event(self)

    def run(self):
        time, customs = self.ctime, self.customs
        event_log(time, "car  leave")
        customs.free_count_1()
        customs.total_time_acc(time - self.car.arrive_time())
        if customs.has_queued_car():
            car = customs.next_car()
            i = customs.find_gate()
            event_log(time, "car check")
            customs.wait_time_acc(time, car.arrive_time())
            Leave(time + randint(*car_check_time), i, car, customs)
#
# if __name__ == '__main__':
#     cus = Customs(2, 480)
#     cus.simulate()