class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, value):
        n = ListNode(value)
        n.setNext(self.head)
        self.head = n

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num_1_as_string = ''
        num_2_as_string = ''
        num_1_size = 0
        num_2_size = 0

        while l1 is not None:
            num_1_as_string += str(l1.val)
            num_1_size += 1
            l1 = l1.next
        while l2 is not None:
            num_2_as_string += str(l2.val)
            num_2_size += 1
            l2 = l2.next

        num_1_as_string = num_1_as_string[::-1]
        num_2_as_string = num_2_as_string[::-1]

        summ = int(num_1_as_string) + int(num_2_as_string)
        summ = str(summ)

        head = None
        for digit in summ:
            new_node = ListNode(int(digit))
            new_node.next = head
            head = new_node

        return head


if __name__ == "__main__":
    # linked list implementation tests
    l = LinkedList()
    l.add(31)
    l.add(77)
    l.add(17)
    l.add(93)
    l.add(26)
    l.add(54)

    print(l.size())  # 6

    print(l.search(999))  # False
    print(l.search(17))  # True

    l.remove(17)
    print(l.search(17))  # False
    l.remove(31)
    print(l.search(31))  # False
    l.remove(54)
    print(l.search(54))  # False

    # solution test
    l1 = LinkedList()  # (2 -> 4 -> 3)
    l1.add(3)
    l1.add(4)
    l1.add(2)

    l2 = LinkedList()  # (5 -> 6 -> 4)
    l2.add(4)
    l2.add(6)
    l2.add(5)

    s = Solution()
    sum = s.addTwoNumbers(l1.head, l2.head)
    sumlist = []
    while sum:
        sumlist.append(sum.val)
        sum = sum.next
    print(sumlist)  # [7, 0, 8]

    l1 = LinkedList()  # [1, 8]
    l1.add(8)
    l1.add(1)

    l2 = LinkedList()  # [0]
    l2.add(0)

    sum = s.addTwoNumbers(l1.head, l2.head)
    sumlist = []
    while sum:
        sumlist.append(sum.val)
        sum = sum.next
    print(sumlist)  # [1, 8]
