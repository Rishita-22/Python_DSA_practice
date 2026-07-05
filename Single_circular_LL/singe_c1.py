class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class SL:
	head = None  # static-like variable (same for all methods)

	@staticmethod
	def create():
		c = 0
		ch = 'y'
		ptr = None

		while ch == 'y':
			c += 1
			data = int(input(f"Enter node{c} data: "))
			cur = Node(data)

			if SL.head is None:
				SL.head = cur
				cur.next = SL.head   # first node points to itself
			else:
				ptr.next = cur
				cur.next = SL.head   # last node points to head

			ptr = cur
			ch = input("To create new node press y; ")

	@staticmethod
	def disp():
		print("Elements are:")

		if SL.head is None:
			print("List is empty")
			return

		ptr = SL.head
		while True:
			print(ptr.data)
			ptr = ptr.next
			if ptr == SL.head:
				break


# main equivalent
if __name__ == "__main__":
	SL.create()
	SL.disp()
