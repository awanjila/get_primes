#A function to generate prime numbers from 0 to n with asymptotic analysis
def getPrimeNumbers():

	for num in range(0, n):  #checks the num from 0 to a number n
		if num>1:
			for i in range(2, num): #This second loop, gets all the numbers in range o to n that divides with numbers
				if (num%i)==0:
					break
			else: 
				print(num)

		
	
