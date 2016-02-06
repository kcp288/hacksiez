pri_vowels = {'AA1': 0, 'AE1': 1, 'AH1': 2, 'AO1': 3, 'AW1': 4, 'AY1': 5, 'EH1': 6, 'ER1': 7, 'EY1': 8, 'IH1': 9, 'IY1': 10, 'OW1': 11, 'OY1': 12, 'UH1': 13, 'UW1': 14}

vowels = {'AA0': 0, 'AA2': 1, 'AE0': 2, 'AE2': 3, 'AH0': 4, 'AH2': 5, 'AO0': 6, 'AO2': 7, 'AW0': 8, 'AW2': 9, 'AY0': 10, 'AY2': 11, 'EH0': 12, 'EH2': 13, 'ER0': 14, 'ER2': 15, 'EY0': 16, 'EY2': 17, 'IH0': 18, 'IH2': 19, 'IY0': 20, 'IY2': 21, 'OW0': 22, 'OW2': 23, 'OY0': 24, 'OY2': 25, 'UH0': 26, 'UH2': 27, 'UW0': 28, 'UW2': 29}

consonants = {'B': 0, 'CH': 1, 'D': 2, 'DH': 3, 'F': 4, 'G': 5, 'HH': 6, 'JH': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'NG': 12, 'P': 13, 'R': 14, 'S': 15, 'SH': 16, 'T': 17, 'TH': 18, 'V': 19, 'W': 20, 'Y': 21, 'Z': 22, 'ZH': 23}

v_cons = {'D': 2, 'DH': 3, 'G': 5, 'JH': 7, 'M': 10, 'N': 11, 'NG': 12, 'R': 14, 'V': 19, 'W': 20, 'Y': 21}

nv_cons = {'B': 0, 'F': 4, 'G': 5, 'K': 8, 'P': 13, 'T': 17, 'TH': 18, 'Y': 21}

written_consonants = {'B': 0, 'C': 1, 'D': 2, 'F': 4, 'G': 5, 'H': 6, 'J': 7, 'K': 8, 'L': 9, 'M': 10, 'N': 11, 'P': 13, 'Q': 3, 'R': 14, 'S': 15, 'T': 17, 'V': 19, 'W': 20, 'Y': 21, 'Z': 22, 'X': 23}


def abbrev(inp):
  # To uppercase, split into words
  inp = inp.upper()
  inp = inp.split(' ')

  output = []

  # For each word, call lookup
  for word in inp:
 	abbrev = lookup(word)

 	print word
 	print abbrev

  #print output

def lookup(token):
  cmu = open('cmudict.txt', 'r')

  abbrev = ''
  coda = ''
  
  for line in cmu:
  	if token in line:
  	  line = line.split()
  	  if token == line[0]:
  	  	abbrev = findstressed(line, token)


  if len(abbrev)==0:
	print token + " not found"
	return
  
  cmu.close()
  return abbrev

# Get spelling up to stressed syllable
# Cut off all consonants after it

def spelling(token, ctr, r):

	vowelcount = 0
	word = list(token)
	print word
	for letter in word:
		if letter in written_consonants:
			continue
		else:
			vowelcount = vowelcount + 1
			if vowelcount == ctr:
				ndx = word.index(letter)
				break

	# Account for rhotic vowel
	if r:
		return  word[0:ndx+2]

	return  word[0:ndx+1]


def findstressed(line, token):
	abbrev = ''
	numvowels = 0
	stressedlocation = 0

	for phone in line:
		if phone in pri_vowels:
			stressed = True

			# Locate stressed syllable
			ndx = line.index(phone)

			abbrev = line[1:ndx+1]
			newline = line[ndx+1:]

			# No need to pad the coda
			if len(newline) < 1:
				return abbrev

			# Else if it is truncated
			for sound in newline:
				if sound in vowels:
					break
				if sound in consonants:
					ndx = newline.index(sound)

			coda = newline[0:ndx+1]
			coda2 = generatecoda(abbrev)

			newspelling = ''.join([str(x) for x in coda]) + ''.join([str(x) for x in coda2])

			abbrev = abbrev + coda + coda2

			numvowels = numvowels + 1
			stressedlocation = numvowels
			
		elif phone in vowels:
			numvowels = numvowels + 1

	rhotic = False
	for i in abbrev:
		if i == 'ER1':
			rhotic = True

	firstpart = spelling(token, stressedlocation, rhotic)

	firstpart = ''.join([str(x) for x in firstpart])
	print "New Spelling: ", firstpart+newspelling


	if ndx == 0:
		abbrev = line

	return abbrev

def generatecoda(abbrev):
	if len(abbrev) == 0:
		print "not found"
		return 

	end = abbrev[len(abbrev)-1]
	coda = []

	if end in v_cons:
		coda = ['Z']
	if end in nv_cons:
		coda = ['S']

	return coda
  
   
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
