
import random



N = 20
k = 0.1
agents = [0]*N
c=[]
for j in range(N):
	c.append(random.randint(1,100))

for u in range(20000):
	for index in range(0,len(agents)):
		if index == 0:
			if agents[index + 1] ==1 or agents[index + (N-1)] == 1:
				c[index] = c[index] + k*c[index]
			else:
				c[index] = c[index]+1
		elif index == N-1:
			if agents[index - 1] ==1 or agents[0] == 1:
				c[index] = c[index] + k*c[index]
			else:
				c[index] = c[index]+1
		elif index > 0 & index<N-1:
			if agents[index - 1] == 1 or agents[index+1] == 1:
				c[index] = c[index] + k*c[index]
			else:
				c[index] = c[index]+1
	for n in range(0,len(agents)):
		if c[n]>=100:
			agents[n]=1
			c[n]=0
		else:
			agents[n] = 0
	print(agents)



			