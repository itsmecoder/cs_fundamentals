#!/usr/bin/env python
# coding=utf-8


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

    def has_next(self):
        return bool(self.next_node)


class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 1

    def __str__(self):
        p = self.head
        while p:
            print p.get_data(),
            p = p.get_next()
        return ''

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        p = self.head
        while p.get_next():
            p = p.get_next()
        p.set_next(node)
        self.size += 1

    def length(self):
        return self.size

    def search(self, data):
        p = self.head
        while p.get_next():
            if p.get_data() == data:
                return True
            p = p.get_next()
        return False

    def print_list(self):
        p = self.head
        while p:
            print p.data
            p = p.get_next()

    def remove(self, data):
        if self.head.get_data() == data:
            self.head.set_next(self.head.get_next())
            print "Deleted data from list {}".format(data)
            return True

        p = self.head
        q = self.head.get_next()
        while q:
            if q.get_data() == data:
                p.set_next(q.get_next())
                print "Deleted data from the list {}".format(data)
                return True
        print "Maybe the data you're trying to delete is not in the list."
        return False

    def insert_at_pos(self, data, pos):
        node = Node(data)
        if pos < 0 or pos > self.size + 1:
            # In an ideal world, this should throw ValueError.
            print "Cannot insert beyod the length of the list."

        if pos == 0:
            return self.insert_at_head(data)

        if pos == self.size:
            return self.insert_at_end(data)

        p = self.head
        q = self.head.get_next()
        for i in range(1, self.size):
            if i == pos:
                p.set_next(node)
                node.set_next(q)
                self.size += 1
                print "Node inserted at position {}".format(pos)
                return
            p = q
            q = q.get_next()
        return

    def insert_at_head(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def insert_at_end(self, data):
        node = Node(data)
        p = self.head
        while p.get_next():
            p = p.get_next()
        p.set_next(node)
        self.size += 1


if __name__ == '__main__':
    a = SingleLinkedList()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    # Print the list
    print a
    # Length of the list.
    print "Length of the list is {}".format(a.length())
    # search node in list
    print a.search(2)
    a.remove(2)
    print a
    a.insert_at_head('a')
    print a
    a.insert_at_end('b')
    print a
    a.insert_at_pos('z', 4)
    print a
