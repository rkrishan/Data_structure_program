class Node:

	def __init__(self,data):
		self.data = data
		self.next = None


class Linklist:

	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head

		while(temp):
			print(temp.data)
			temp = temp.next

	def insert_data(self,data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return
		last = self.head
		
		while(last.next):
			last = last.next

		last.next = new_node	

	def deleteNodeKey(self,key):

		# store head node
		temp = self.head

		if (temp.data==key):
			self.head = temp.next
			temp = None
			return 

		while(temp is not None):
			if temp.data ==key:
				break
			prev = temp
			temp = temp.next

		if (temp == None):
			return 

		prev.next = temp.next	
				


		


if __name__=='__main__':
	llist = Linklist()
	llist.head = Node(1)
	second = Node(2)
	third =  Node(3)

	llist.head.next = second;
	second.next = third;

	llist.insert_data(5)
	llist.printList()

	print("List after deleteNodeKey")

	llist.deleteNodeKey(5)
	llist.printList()




