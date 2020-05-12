class QueueError(Exception):
    """Base class for errors elated to Stack class"""
    pass


class EmptyQueueException(QueueError):
    """:raises Empty stack exception"""

class Qu(object):

    def __init__(self):
        self._queue = []
        self._length = 0

    def __len__(self):
        return self._length

    def __str__(self):
        return str(self._queue)

    def is_empty(self):
        return self._length == 0

    def enqueue(self, item):
        """
        Puts item in
        :param item: Item that goes in the end of the queue
        """
        self._queue.insert(0, item)
        self._length += 1

    def dequeue(self):

        if self.__len__() == 0:
            raise EmptyQueueException

        first = self._queue[-1]

        self._queue.pop()

        self._length -= 1

        return first
    
    def first(self):
        if self._length == 0:
            raise EmptyQueueException

        return self._queue[-1]



# if __name__ == '__main__':
#     q = Queue()
#     q.enqueue(1)
#     q.enqueue(2)
#     q.enqueue("#@")
#     q.enqueue("#$%^YHVF")
#
#     first_in_q = q.dequeue()
#     second_in_q = q.dequeue()
#     third_in_q = q.dequeue()
#     print("First:", first_in_q)
#     print(q)


