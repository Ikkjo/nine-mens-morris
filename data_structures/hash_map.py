import random


class HashMap(object):
    """
    Klasa modeluje heš mapu
    """
    def __init__(self, capacity=8):
        """
        Konstruktor

        Argumenti:
        - `capacity`: inicijalni broj mesta u lookup nizu
        - `prime`: prost broj neophodan heš funkciji
        """
        self._data = [None] * capacity
        self._capacity = capacity
        self._size = 0
        self._prime = 109345121
        self._keys = set()

        # konstante heširanja
        self._a = 1 + random.randrange(self._prime-1)
        self._b = random.randrange(self._prime)

    def _hash(self, key):
        """
        Heš funkcija

        Izračunavanje heš koda vrši se po formuli (ax + b) mod p.

        Argument:
        - `x`: vrednost čiji se kod računa
        """
        hashed_value = (hash(key)*self._a + self._b) % self._prime
        compressed = hashed_value % self._capacity
        return compressed

    def __getitem__(self, key):

        if key not in self._keys:
            raise KeyError("No such key in Hash Map!")


        index = self._hash(key)
        if self._data[index][0] == key:
            return self._data[index][1]

        else:

            while self._data[index] is not None:
                index = (index + 1) % self._capacity

    def __setitem__(self, key, value):
        index = self._hash(key)

        if key in self._keys:
            self._data[index] = (key, value)

        else:
            if self._data[index] is None:
                self._data[index] = (key, value)
            else:
                counter = 0
                while self._data[index] is not None or counter == self._capacity:
                    index = (index + 1) % self._capacity
                    counter += 1

                if counter == self._capacity:
                    raise IndexError("Maximum capacity reached!")

                self._data[index] = (key, value)

            if key not in self._keys:
                self._size += 1

            self._keys.add(key)

    def keys(self):
        keys = []
        for index in range(self._capacity):
            if self._data[index] is not None:
                keys.append(self._data[index][0])

        return keys

    def values(self):
        values = []
        for index in range(self._capacity):
            if self._data[index] is not None:
                values.append(self._data[index][0])

        return values

    def items(self):
        items = []

        for item in self._data:
            if item is not None:
                items.append(item)

        return items

    # def __del__(self, key):
    #     if key not in self._keys:
    #         raise KeyError("No such key in Hash Map!")
    #
    #     index = self._hash(key)
    #     while self._data[index][0] != key:
    #         index = (index + 1) % self._capacity
    #
    #     self._data[index][1] = None


if __name__ == '__main__':
    map = HashMap()
    map["board_state"] = 2
    map["mode"] = 3
    map["player_color"] = "W"
    map["board_state"] = 566
    map["table_cloth"] = "WEEEWOOO"
    keyz = map.keys()
    itemz = map.items()
    "TEST"
