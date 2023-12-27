# -*- coding: utf-8 -*-
"""
Пример 1 - Дефинициjа класе за чвор бинарног стабла.
"""
"""
class Node:
    def __init__(self, data, parent=None):
        self.data=data
        self.parent=parent
        self.left=None
        self.right=None
"""

"""
Пример 2 - Inorder пролазак кроз стабло
"""
"""
def inorder(root, array):
     
    # Base case
    if not root:
        return
     
    inorder(root.left, array)
    array.append(root)
    inorder(root.right, array)
"""

"""
# Тест стабло:    
root = Node('A')
root.left = Node('B', root)
root.right = Node('C', root)
root.left.left = Node('D', root.left)
root.left.right = Node('E', root.left)
root.left.left.left = Node('F', root.left.left)
"""

"""
# Тест за Inorder обилазак стабла:
array = []
inorder(root, array)

#print(array[0].data, array[1].data, array[2].data, array[3].data, array[4].data, array[5].data)
"""


"""
Пример 3 - Операциjе над бинарним стаблом претраживања.
"""
# Нова дефиниција класе за чвор бинарног стабла:
class AnotherNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None
        
        
# Тест стабло:
another_root = AnotherNode(17)
another_root.left = AnotherNode(7, another_root)
another_root.right = AnotherNode(23, another_root)
another_root.left.left = AnotherNode(4, another_root.left)
another_root.left.right = AnotherNode(12, another_root.left)
another_root.right.left = AnotherNode(19, another_root.right)
another_root.left.left.left = AnotherNode(1, another_root.left.left)

# Претраживање:
def search(root, k):
	if root.key==k:
		return root
	elif k < root.key:
		if root.left is None:
			return None
		else:
			return search(root.left, k)
	else:
		if root.right is None:
			return None
		else:
			return search(root.right, k)

# Минимум:
def min(root):
	# idemo levo sve dok mozemo
	current=root
	while current.left is not None:
		current=current.left
	return current

# Максимум:
def max(root):
	# idemo desno sve dok mozemo
	current=root
	while current.right is not None:
		current=current.right
	return current

# Наследник:
def naslednik(node):
	#case 1: Ima desno dete, trazi se minimum na njemu
	if node.right is not None:
		return min(node.right)
		
	#case 2: Nema desno dete, moramo da idemo gore sve dok ne krenemo desno(dodjemo do levog deteta)
	# idemo gore sve dok je on desno dete(njegov roditelj je manji od njega)
	# ili dok nema roditelja, tada nemamo naslednika
	# i vracamo roditelja, u prvom slucaju, vratice key, u drugom None
	current=node
	while current.parent is not None and current is current.parent.right:
		current=current.parent
	return current.parrent

# Претходник:
def prethodnik(node):
	#case 1: Ima levo dete, trazi se maksimum na njemu
	if node.left is not None:
		return max(node.left)
		
	#case 2: Nema levo dete, moramo da idemo gore sve dok ne krenemo levo(dodjemo do desnog deteta)
	# idemo gore sve dok je on levo dete(njegov roditelj je veci od njega)
	# ili dok nema roditelja, tada nemamo prethodnika
	# i vracamo roditelja, u prvom slucaju, vratice key, u drugom None
	current=node
	while current.parent is not None and current is current.parent.left:
		current=current.parent
	return current.parrent

# Додавање чвора:
def insert(root, node):
	# Isto kao search, samo umesto return stavljamo node
	if root.key == node.key:
		return root
	elif node.key < root.key:
		if root.left is None:
			root.left=node
			node.parent=root
		else:
			return insert(root.left, node)
	else:
		if root.right is None:
			root.right=node
			node.parent=root	
		else:
			return insert(root.right, node)

# Брисање чвора:
def delete(node):
	#case 1 nema dece, odgovarajuci left ili right parenta pokazuje na null
	if node.left is None and node.right is None:
		if node is node.parent.left:
			node.parent.left=None
		if node is node.parent.right:
			node.parent.right=None
		return node
		
	#case 2 ima jedno dete, menjamo pokazivace kako bi obrisali cvor
	elif node.left is None:
		if node is node.parent.left:
			node.parent.left=node.right
			node.parent.left.parent=node.parent
		if node is node.parent.right:
			node.parent.right=node.right
			node.parent.right.parent=node.parent
		return node
	elif node.right is None:
		if node is node.parent.left:
			node.parent.left=node.left
			node.parent.left.parent=node.parent
		if node is node.parent.right:
			node.parent.right=node.left
			node.parent.right.parent=node.parent
		return node
		
	#case 3 ima oba deteta, trazimo naslednika i menjamo keyeve cvoru i nasledniku i brisemo naslednika
	else:
		s=naslednik(node)
		s.key, node.key=node.key, s.key
		return delete(s)

               
# Тест за претраживање:
"""        
print(search(another_root, 4))
print(search(another_root, 4).key)

print(search(another_root, 13))
"""

# Тест за минимум:
"""
print(min(another_root))
print(min(another_root).key)
"""

# Тест за максимум:
"""
print(max(another_root))
print(max(another_root).key)
"""

# Тест за наследника:
"""
print(naslednik(another_root).key)
print(naslednik(another_root.left).key)
"""

# Тест за претходника:
"""
print(prethodnik(another_root).key)  
print(prethodnik(another_root.left).key)  
"""

# Тест за додавање чвора:
"""
new_node = AnotherNode(13)
insert(another_root, new_node)

print(another_root.left.right.right)
print(another_root.left.right.right.key)
"""

# Тест за брисање чвора:
"""
# Први случај: чвор је лист стабла
delete(another_root.left.left.left)
print(another_root.left.left.left)
"""
 
"""   
# Други случај: чвор има једног потомка
delete(another_root.right)
print(another_root.right)
print(another_root.right.key)
"""

"""
# Трећи случај: чвор има оба потомка
delete(another_root.left)
print(another_root.left)
print(another_root.left.key)
"""



"""
Пример 4 - Добијање балансираног бинарног стабла претраживања из небалансираног 
бинарног стабла претраживања.
"""
# Дефиниција чвора бинарног стабла
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


def inorder(root,nodes):
	
	# Основни случај
	if not root:
		return
	
	inorder(root.left,nodes)
	nodes.append(root)
	inorder(root.right,nodes)

# Из сортираног низа добијамо балансирано бинарно стабло претраживања
def buildTreeUtil(nodes,start,end):
	
	# Основни случај
	if start>end:
		return None

	# Узимамо средњи елемент да буде root
	mid=(start+end)//2
	node=nodes[mid]

	# користећи се индексима рекуризвно позивамо функцију да бисмо добили 
    # балансирано стабло
	node.left=buildTreeUtil(nodes,start,mid-1)
	node.right=buildTreeUtil(nodes,mid+1,end)
	
	return node

# Функција која као аргуемнт прима корен небалансираног стабла, и позива пређашње 
# функције како бисмо добили балансирано стабло
def buildTree(root):
	
	# Store nodes of given BST in sorted order
	nodes=[]
	inorder(root,nodes)

	# Constructs BST from nodes[]
	n=len(nodes)
	return buildTreeUtil(nodes,0,n-1)

def preOrder(root):
	if not root:
		return
	print("{} ".format(root.data),end="")
	preOrder(root.left)
	preOrder(root.right)


# Конструкција бинарног стабла
#		      10
#		     /
#		    8
#	       /
#	      7
#	     /
#	    6
#	   /
#     5

root = Node(10)
root.left = Node(8) 
root.left.left = Node(7) 
root.left.left.left = Node(6)   
root.left.left.left.left = Node(5)
  
print("Preorder небалансираног стабла је:")
preOrder(root)

# 'балансирамо' стабло
root = buildTree(root)

print("\nPreorder балансираног стабла је:")
preOrder(root)
        