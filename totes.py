pri_vowels = {'AA1': 0, 'AE1': 1, 'AH1': 2, 'AO1': 3, 'AW1': 4, 'AY1': 5, 'EH1': 6, 'ER1': 7, 'EY1': 8, 'IH1': 9, 'IY1': 10, 'OW1': 11, 'OY1': 12, 'UH1': 13, 'UW1': 14}

vowels = {'AA0': 0, 'AA2': 1, 'AE0': 2, 'AE2': 3, 'AH0': 4, 'AH2': 5, 'AO0': 6, 'AO2': 7, 'AW0': 8, 'AW2': 9, 'AY0': 10, 'AY2': 11, 'EH0': 12, 'EH2': 13, 'ER0': 14, 'ER2': 15, 'EY0': 16, 'EY2': 17, 'IH0': 18, 'IH2': 19, 'IY0': 20, 'IY2': 21, 'OW0': 22, 'OW2': 23, 'OY0': 24, 'OY2': 25, 'UH0': 26, 'UH2': 27, 'UW0': 28, 'UW2': 29}

consonants = {'B': 0, 'CH': 1, 'D': 2, 'DH': 3, 'F': 4, 'G': 5, 'HH': 6, 'JH': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'NG': 12, 'P': 13, 'R': 14, 'S': 15, 'SH': 16, 'T': 17, 'TH': 18, 'V': 19, 'W': 20, 'Y': 21, 'Z': 22, 'ZH': 23}

def abbrev(inp):
  inp = inp.split(' ')
  output = ''


  for word in inp:
 	abbrev = lookup(word)
 	output = output + word + ' '

  output = output.strip()
  output = output + '.'
  print output


def lookup(token):
  cmu = open('cmudict.txt', 'r')

  abbrev = ''
  
  for line in cmu:
  	if token in line:
  	  line = line.split()
  	  if token == line[0]:
  	  	print line
  	  	for phone in line:
  	  		if '1' in phone:

  	  			ndx = line.index(phone)
  	  			abbrev = line[0:ndx+1]

  	  			newline = line[ndx+1:]
  	  			print newline

  	  			for sound in newline:
  	  				

  	  			print abbrev
  cmu.close()
  return token

'''
  	  if token == line[0]:
  	  	print line
  	  	for phone in line:
  	  		if '1' in phone:
  	  			print phone
  	  	return token
  	  	
  	  for phone in line: 
	    if '1' in phone:
	      print line
	      print phone

'''


    
   
def main():
	# Initialize
	stop = False
	token_counter = 0

	while (stop == False):
		# Get input token from user
		inp = raw_input("Enter sentence to abbrev: ");
		# TODO: Check that phone is w/i list
		abbrev(inp)

		# Continue or break out of loop
		cont = raw_input("\nEnter X to exit, or any key to continue: ")
		if (cont == 'X'):
			stop = True
		else: 
			token_counter = token_counter + 1
			continue
	print("Done!")
main()
