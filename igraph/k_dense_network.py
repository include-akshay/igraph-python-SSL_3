class Classname:
	
	def __init__(self,vertices) :
		self.vertices=vertices
		self.graph=[[0 for x in range(vertices+1)] for y in range(vertices+1)]
		self.degree=[]
		self.degree=[0 for i in range(vertices+1)]
		self.store=[]
		self.store=[0 for i in range(vertices+1)]
		self.result=[]
		
	def addEdge(self,u,v):
		self.graph[u][v]=1
		self.graph[v][u]=1
		self.degree[u]+=1
		self.degree[v]+=1

	def create_result(self,n) :
 
		sub_list=[]
		for i in range(1, n) :
			sub_list.append(self.store[i])
		self.result.append(sub_list)

	def is_clique(self,b) :
 
		# Run a loop for all the set of edges
		# for the select vertex
		for i in range(1, b) :
			for j in range(i + 1, b) :
	
				# If any edge is missing
				if (self.graph[self.store[i]][self.store[j]] == 0) :
					return False
		
		return True

	def findCliques(self,i, l, s) :
 
		# Check if any vertices from i+1 can be inserted
		for j in range( i + 1, self.vertices -(s - l) + 1) :
	
			
			if (self.degree[j] >= s - 1) :
	
				# Add the vertex to store
				self.store[l] = j
	
				if (self.is_clique(l + 1)) :
					if (l < s) :
	
						# Recursion to add vertices
						self.findCliques(j, l + 1, s)
	
					# Size is met
					else :
						self.create_result(l + 1)
		
	def calling_function(self,i,l,s):
		self.findCliques(i,l,s)
		return self.result

