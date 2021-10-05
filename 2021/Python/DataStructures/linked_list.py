class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.data = new_data

	def set_next(self, new_next):
		self.next = new_next


class UnorderedLinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next


if __name__=='__main__':
	linked_list = UnorderedLinkedList()

	linked_list.head = Node(1)
	second = Node(2)
	third = Node(3)

	linked_list.head.next = second
	second.next = third

	linked_list.print_list()
