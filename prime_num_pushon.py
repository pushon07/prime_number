__author__ = 'ASM Pushon'

"""
Use:  In the pyhton shell or command line, write the command given below:
		python prime_num_pushon.py min_val max_val
Example: python prime_num_pushon.py 1900 2000

This is a small code in Python for finding the Prime numbers within any given range of integers.
Here I saved all the prime numbers (from 2 to maximum-value-of-the-range ) in a list first.
Later, all the prime numbers within the given range is saved in a separate list (prime_list_within_range).
Because to make this code work faster I used a trick to find the prime numbers. That is, instead of 
dividing each number by all the integers between 1 and that number-itself inclusive, I divided each number
by only the prime numbers smaller than it. If the number is divided by any smaller prime numbers,
then its not a prime number. Interestingly, when the first number 2 was divided by the elements
of the initial empty prime_list, it passed the condition to be a prime number. :)
Now, since I used the list of prime numbers to find other prime numbers, I had to make that list from
the beginning (from 2) regardless of the given range. Therefore, I had to use two lists here.

Thanks for reading the lengthy details!
"""
import sys

def print_prime_numbers(lower_num, upper_num):

	prime_list = []			#initial empty list of the prime numbers from 2 to upper_num
	for x in xrange(2, upper_num + 1):	#loop for iterating and storing the prime numbers
		isPrime = True
		for i in prime_list:	#This the trick! Think about it
			if x%i == 0:		#if number is divided by any prime number then its not a prime number
				isPrime = False
				break				#so no need to continue anymore and close/break the loop

		if isPrime == True:		
			prime_list.append(x)	#store all the prime numbers (from 2 to upper_num) in the list

	prime_list_within_range = []	#list of prime numbers within the given range
	for n in prime_list:			#from the list of all prime numbers
		if n in xrange(lower_num, upper_num + 1):
			prime_list_within_range.append(n)	#store all the prime numbers (from lower_num to upper_num) in the list

	number_prime_num = len(prime_list_within_range)		#variable for number of prime numbers within the range
	if number_prime_num == 0:
		print "Sorry, no Prime Number between %d and %d inclusive. Try with a different range." \
		%(lower_num, upper_num)

	elif number_prime_num == 1:
		print "Only a single Prime Number between %d and %d inclusive. It is %r." \
		%(lower_num, upper_num, prime_list_within_range[0])

	else:
		print "Total %d Prime Numbers between %d and %d inclusive. They are:\n%r" \
		%(number_prime_num, lower_num, upper_num, prime_list_within_range)


if __name__ == '__main__':
	#print_prime_numbers(69900, 70000)	#to run this code directly in sublime text,IPython Notebook, etc.
	try:
		#converts upper and lower values (including floats) of the range into integers and stores them
		lower_num, upper_num = int(float(sys.argv[1])), int(float(sys.argv[2]))
		if lower_num > upper_num:		#in case the range is not valid
			lower_num, upper_num = upper_num, lower_num
		
		print_prime_numbers(lower_num, upper_num)

	except ValueError: print "Please try with a valid range of two integers."
