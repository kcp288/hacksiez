# hacksiez
Created at Stupid Hackathon 2016
Live at https://dumb-it-down.herokuapp.com/

### About
Node.js, [python-shell](https://github.com/extrabacon/python-shell) module for backend
[cmudict](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)  for pronunciation
[Hover.css](http://ianlunn.github.io/Hover/) button effect
Thanks to Lauren Spradlin and Taylor Jones for their work on phonological and  morphological construction of "totes"  abbreviations. Read more about abbreviation research [here](http://opencuny.org/laurenspradlin/files/2016/01/Totes-LSA-Spradlin-Jones-2016-pdf.pdf).

### Basic rules for 'Totes' constructions
A 'totes' is a term for abbreviations (abbrevs?) that have proliferated from twitter into speech. Originally triggered by the abbreviation of 'totally,' 'totes' constructions can now be constructed without any preceding contraction. What was once 'totes adorbs' can now just be 'adorbs.' Intriguing!
How to built a 'totes' *using 'obviously'*
 1. Locate primary stress in the word *- OB.vi.uhs.li*
 2. Maximize coda of stressed syllable *- OBV.iushli*
 3. Delete everything after the coda *- OBV*
 4. Optional suffix *- OBVS or perhaps OBVSIEZ

### Algorithm
In **totes.py**
For each word in input:
* Check if stop word. If yes, ignore--we don't abbreviate stop words.
* Look up word in cmu pronunciation dictionary.
  * If not found, just return the word. We won't abbreviate it.
* Use cmu dict stress coding to identify stressed syllable
* Build abbreviation, including stressed syllable and all consonants that follow
* Generate coda, adding 'z' or 's' to ending consonants
* Convert from phones to spelling by using the original spelling concatenated with the cmu dict phonetic spelling for the coda
* Return all in string!

### TODO
* Integrate 'ziez' optional amplification
* Bug fix: diphthongs, common spelling errors
