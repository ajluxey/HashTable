class HashMap:
    def __init__(self):
        self._elements = [[]]
        self._count = 0
        self._size = 1
        self._max_load_k = 2

    @property
    def count(self):
        return self._count

    @property
    def lists_count(self):
        return len(self._elements)

    @property
    def load_factor(self):
        return self._load_factor()

    @property
    def max_load_k(self):
        return self._max_load_k

    @max_load_k.setter
    def max_load_k(self, k):
        self._max_load_k = k

    def delete(self, key):
        index = self._index(key)
        if index == -1:
            return
        self._delete(index, key)

    def delete_all(self):
        self._count = 0
        self._elements = [[]]
        self._size = 1

    def __getitem__(self, key):
        index = self._index(key)
        if index == -1:
            return
        el_index = self._search(key, index)
        if el_index == -1:
            return
        else:
            return self._elements[index][el_index]

    def __setitem__(self, key, value):
        index = self._index(key)
        if index == -1:
            return
        self._delete(index, key)
        self._elements[index].append((key, value))
        self._count += 1
        if self._load_factor() > self._max_load_k:
            self._rehash()

    def _delete(self, index, key):
        element_index = self._search(key, index)
        if element_index != -1:
            self._elements[index].pop(element_index)
            self._count -= 1
        return

    def _index(self, key):
        try:
            return abs(hash(key)) % self._size
        except (TypeError, ZeroDivisionError):
            return -1

    def _load_factor(self):
        try:
            return self._count/self._size
        except ZeroDivisionError:
            return 0

    def _search(self, key, index):
        lst = self._elements[index]
        for i in range(len(lst)):
            if key == lst[i][0]:
                return i
        return -1

    def _rehash(self):
        new_size = self._size*2 + 1
        elements = self._elements
        self.delete_all()
        self._size = new_size
        for i in range(new_size-1):
            self._elements.append([])
        for lst in elements:
            for pare in lst:
                self[pare[0]] = pare[1]
        return


if __name__ == '__main__':
    d = HashMap()
    d['a'] = 5
    print(d['a'])
