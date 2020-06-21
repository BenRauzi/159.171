class Queue():
	def __init__(self, queue=[]):
		self.items = queue

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def size(self):
		return len(self.items)

	def dequeue(self):
		return self.items.pop()

	def __str__(self):
		return str(self.items)
