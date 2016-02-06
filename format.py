def format(inp):
  ctr = 0
  output = ''
  for i in inp:
   out = '\'' + i + '\': ' + str(ctr) + ', '
   ctr = ctr + 1
   output = output + out
  print output

def format2(inp):
  inp = inp.split(' ')
  output = '[ '
  for i in inp:
    out = '\'' + i + '\','
    output = output + out
  output = output + ']'
  print output

def format3(inp):
  pri = []
  other = []
  for i in inp:
    if i.count('1') == 1:
      pri.append(i)
    elif i.count('2') == 1:
      other.append(i)
    elif i.count('0') == 1:
      other.append(i)
    else: continue
  print pri
  print other
  return pri, other
def main():
  inp = ['B', 'CH', 'D', 'DH', 'F', 'G', 'HH', 'JH', 'K', 'L', 'M', 'N', 'NG', 'P', 'R', 'S', 'SH', 'T', 'TH', 'V', 'W', 'Y', 'Z', 'ZH']
  inp2 = 'AA AA0 AA1 AA2 AE AE0 AE1 AE2 AH AH0 AH1 AH2 AO AO0 AO1 AO2 AW AW0 AW1 AW2 AY AY0 AY1 AY2 EH EH0 EH1 EH2 ER ER0 ER1 ER2 EY EY0 EY1 EY2 IH IH0 IH1 IH2 IY IY0 IY1 IY2 OW OW0 OW1 OW2 OY OY0 OY1 OY2 UH UH0 UH1 UH2 UW UW0 UW1 UW2'
  inp3 = [ 'AA','AA0','AA1','AA2','AE','AE0','AE1','AE2','AH','AH0','AH1','AH2','AO','AO0','AO1','AO2','AW','AW0','AW1','AW2','AY','AY0','AY1','AY2','EH','EH0','EH1','EH2','ER','ER0','ER1','ER2','EY','EY0','EY1','EY2','IH','IH0','IH1','IH2','IY','IY0','IY1','IY2','OW','OW0','OW1','OW2','OY','OY0','OY1','OY2','UH','UH0','UH1','UH2','UW','UW0','UW1','UW2']
  format(inp)
  pri, other =  format3(inp3)
  format(pri)
  format(other)
main()
