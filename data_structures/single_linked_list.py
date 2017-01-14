#!/usr/bin/env python
# coding=utf-8


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(Node):
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node
        self.size += 1

    def length(self):
        return self.size

    def search(self, data):
        p = self.head
        while p.next:
            if p.data == data:
                return True
            p = p.next
        return False

    def remove(self, data):
        if self.head.data == data:
            print "Removing head node.."
            self.head = self.head.next
            self.size -= 1
            return True

        p = self.head
        q = self.head.next
        while q:
            if q.data == data:
                print "Deleting the node {}".format(q.data)
                p.next = q.next
                self.size -= 1
                return True
            p = q
            q = q.next
        print "Node not found."
        return False

    def print_list(self):
        p = self.head
        while p:
            print p.data
            p = p.next


if __name__ == '__main__':
    a = SingleLinkedList()
    a.add(1)
    a.add(2)
    a.add(3)
    a.add(4)
    # Print the list
    a.print_list()
    # Length of the list.
    a.length()
    # search node in list
    print(a.search(2))
    # remove node from list
    a.remove(3)
    # print list again.
    a.print_list()
