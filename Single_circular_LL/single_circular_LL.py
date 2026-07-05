class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class SL:
	head = None #static-like variable (same for all methods)

	@staticmethod
	def create():
		c = 0
		ch = 'y'
		ptr = None

		while ch == 'y':
			c += 1
			data = int(input(f"Enter node{c} data: "))
			cur = Node(data)
			cur.next = cur
			if SL.head is None:
				SL.head = cur 
			else:
				ptr.next = cur
				cur.next = SL.head

			ptr = cur 
			ch = input("To create new node press y; ")

	@staticmethod
	def disp():
		print("Elements are:")

		if SL.head is None:
			print("List is empty")

		ptr = SL.head
		while ptr.next is not SL.head:
			print(ptr.data)
			ptr = ptr.next
		print(ptr.data)

#main equivalent 
if __name__=="__main__":
	SL.create()
	SL.disp()