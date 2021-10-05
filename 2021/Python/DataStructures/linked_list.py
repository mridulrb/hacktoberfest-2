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

	def is_empty(self):
		"""Check if UnorderedLinkedList is empty"""
		return self.head is None

	def add(self, new_data):
		"""Add a node with new_data to the list"""
		new_node = Node(new_data)
		new_node.set_next(self.head)
		self.head = new_node

	def get_size(self):
		"""Get the size of the list"""
		curr = self.head
		count = 0
		while curr is not None:
			count += 1
			curr = curr.get_next()
		return count

	def exists(self, new_data):
		"""Check if a node with new_data exists"""
		curr = self.head
		while curr is not None:
			if curr.get_data() == new_data:
				return True
		return False

	def remove(self, new_data):  # WIP
		"""
		Remove node with new_data in the list.
		Assume that node exists.
		"""
		prev = None
		curr = self.head
		while curr is not None:
			if curr.get_data() == new_data:
				prev.set_next(curr.get_next())
			else:
				# Inchworming
				prev = curr
				curr = curr.get_next()

	def print_list(self):
		"""Print all nodes in the list in new lines"""
		curr = self.head
		while curr:
			print(curr.data)
			curr = curr.next


if __name__ == '__main__':
	linked_list = UnorderedLinkedList()

	linked_list.head = Node(1)
	second_node = Node(2)
	linked_list.head.set_next(second_node)
	third_node = Node(3)
	second_node.set_next(third_node)

	linked_list.print_list()
