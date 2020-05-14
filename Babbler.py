from collections import defaultdict
from random import choices
from collections import Counter



def distribution():
		result = defaultdict(int)
		for i in range(26):
			result[chr(i + ord('a'))] = 0.0001

		return result



class Babbler:

	

	def __init__(self,n,title):
		self.title = title
		self.n = n
		self.counts = defaultdict(distribution)

		with open(self.title,encoding='utf-8') as file:
    			text = file.read().lower().replace('\n', ' ')			
	
		
		a = self.n
		b = a

		while(a < len(text)):
			self.counts[text[a-b:a]][text[a]] += 1
			a+=1
	

	def babble(self,letter,total):
		
		a=self.n
		b=a	
		while(len(letter) < total):

			#print(letter[-b:])
			#print(self.counts[letter[-b:]])
			letter += choices(list(self.counts[letter[-b:]].keys()),weights = list(self.counts[letter[-b:]].values()))[0]
			a+=b

		return letter 

		


b = Babbler(6, 'moby.txt')
#print(b.title)
print(len(b.counts))
while(1):
	tempstr = input("enter: ")
	print(b.babble(tempstr, 300))
	#b = Babbler(1, 'moby.txt')
	#print(b.babble('call me ishmael. some years ago', 200))  #Produce 200 characters


	
