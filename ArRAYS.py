class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def print(self):
        if self.head is None:
            print("ist is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def print_back(self):
        itr = self.head
        # while itr.next:
        #     itr = itr.next

        if self.head is None:
            print("list is empty")
            return

        llstr = ''

        while itr.next:
            itr = itr.next

        while itr.next:
            llstr += str(itr.data) + '<--'
            itr = itr.prev

        print(llstr)

    def insertatend(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def countOfValues(self):
        count = 1
        itr = self.head
        while itr.next:
            count +=1
            itr = itr.next

        print(count)

    def insetValues(self, data_list):
        self.head  = None
        for data in data_list:
            self.insertatend(data)

        print(data_list)

    def remove(self,index):
        if index < 0 | index >= self.countOfValues():
            raise Exception("invalid index error")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insetAt(self, index, data):
        if index < 0 | index >= self.countOfValues():
            raise Exception("invalid index error")
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count  == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertatend(20)
    ll.insertatend(1)
    ll.insertatend(123)
    ll.insert_at_begining(21112)
    ll.insert_at_begining(9990)
    ll.insertatend(2321212)
    ll.insert_after_value(20,7888)
    ll.print()
    ll.print()
    ll.countOfValues()
    ll.remove(1)
    ll.print()
    ll.insetValues(['g','p','o'])
    ll.remove(1)
    ll.print()
    ll.countOfValues()
    ll.insetAt(1,'r')
    ll.print()
    ll.insert_after_value('g','k')
    ll.print()
    ll.insert_after_value(20,8999)
    ll.print()
    ll.insert_at_end(22222)
    ll.print()
    ll.print_back()

