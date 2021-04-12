import pygame
import math
import sys


class node():

	def __init__(self,name,par=None,ch=[]):
		self.name=name
		self.par = par
		self.ch = []
		if ch is not None:
			for c in ch:
				self.addch(c)
		#self.fix = 0

	def addch(self,nodeob):
		self.ch.append(nodeob)
		nodeob.par = self

	def __str__(self):
		return self.name

	def tb(self,n,a):
		
		while n.name != self.name:
			i,j = n.name[0],n.name[1]
			a[i][j] = 2
			n = n.par
		return a




width = 500
blue = (0,0,255)
black = (0,0,0)
col = (150,200,205)
white = (255,255,255)
end = 0
n = int(input("Input the number of rows"))
sq = int(width/n)
a = []
q = {}

def drgrid(n):
	for i in range(n):
		for j in range(n):
				q[(i,j)]=0
				#print(i,j)
				pygame.draw.rect(screen,white, (j*sq, i*sq,sq,sq),width=0)
	for j in range(n):
		q[(i,j)]=0
		pygame.draw.rect(screen,col, (j*sq, n*sq,sq,sq),width=0)

def chgrid(s):
	j = s[0]//sq
	i = s[1]//sq
	#print(i,j)
	if i<n and j<n:
		if q.get((i,j),-1)==0:
			pygame.draw.rect(screen,black, (j*sq, i*sq,sq,sq),width=0)
			q[(i,j)]=1
		elif q.get((i,j),-1)==1:
			pygame.draw.rect(screen,white, (j*sq, i*sq,sq,sq),width=0)
			q[(i,j)]=0
	elif i==n and j<n:
		global a
		a = makemaze()
		start = findstart(a)
		root = node(start)
		w = findnext(a,root)
		a = root.tb(end,a)
		pmaze(a)
		final(a)
		pass

def pmaze(a):
	for i in range(len(a)):
		for j in range(len(a[i])):
			print(a[i][j],end="")
		print()

def makemaze():
	global a
	global q
	global n
	a = []
	for i in range(n):
		b = []
		for j in range(n):
			if q[(i,j)] == 0:
				b.append(0)
			elif q[(i,j)]==1:
				b.append(1)
		a.append(b)
	return a

def findstart(a):
	for j in range(len(a[0])):
		if a[0][j] == 0:
			a[0][j]=2
			s = (0,j)
			return s
			break

def findnext(a,nod):
	i = nod.name[0]
	j = nod.name[1]
	if i == len(a)-1:
		global end
		end =nod
		return 2
	else :
		count=0
		if j!=0:
			if a[i][j-1]==0:
				if nod.par==None:
					k = node((i,j-1))
					nod.addch(k)
					f1 = findnext(a,k)
					a[i][j-1]=f1
					count+=1
				elif nod.par.name[0]!=i or nod.par.name[1]!=j-1:
					k = node((i,j-1))
					nod.addch(k)
					f1 = findnext(a,k)
					a[i][j-1]=f1
					count+=1
		if i!=len(a)-1:
			if a[i+1][j]==0:
				if nod.par==None:
					k = node((i+1,j))
					nod.addch(k)
					f2 = findnext(a,k)
					a[i+1][j]=f2
					count+=1
				elif nod.par.name[0]!=i+1 or nod.par.name[1]!=j:
					k = node((i+1,j))
					nod.addch(k)
					f2 = findnext(a,k)
					a[i+1][j]=f2
					count+=1
		if j!=len(a[0])-1:
			if a[i][j+1]==0:
				if nod.par==None:
					k = node((i,j+1))
					nod.addch(k)
					f3 = findnext(a,k)
					a[i][j+1]=f3
					count+=1
				elif nod.par.name[0]!=i or nod.par.name[1]!=j+1:
					k = node((i,j+1))
					nod.addch(k)
					f3 = findnext(a,k)
					a[i][j+1]=f3
					count+=1
		if i!=0:
			if a[i-1][j]==0:
				if nod.par==None:
					k = node((i-1,j))
					nod.addch(k)
					f4 = findnext(a,k)
					a[i-1][j]=f4
					count+=1
				elif nod.par.name[0]!=i-1 or nod.par.name[1]!=j:
					k = node((i-1,j))
					nod.addch(k)
					f4 = findnext(a,k)
					a[i-1][j]=f4
					count+=1
		
		if count==0:
			return 0
		else:
			return 0

def final(a):
	for i in range(len(a)):
		for j in range(len(a[i])):
			if a[i][j]==0:
				pygame.draw.rect(screen,white, (j*sq, i*sq,sq,sq),width=0)
			elif a[i][j]==1:
				pygame.draw.rect(screen,black, (j*sq, i*sq,sq,sq),width=0)
			elif a[i][j]==2:
				pygame.draw.rect(screen,blue, (j*sq, i*sq,sq,sq),width=0)
	print("Success")

pygame.init() 
screen = pygame.display.set_mode((width,width+sq))
drgrid(n)
pygame.display.update()

run = True

while run:

	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			s = pygame.mouse.get_pos()
			#print(s)
			chgrid(s)
			


