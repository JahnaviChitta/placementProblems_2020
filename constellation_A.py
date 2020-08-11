letters = {'.*.****.*' : 'A', '*********' : 'E', '***.*.***' : 'I', '****.****' : 'O', '*.**.****' : 'U'}

n = int(input())
c = 0
l = []
while c < 3:
  s = input()
  s = ''.join(s.split())
  if len(s) == n:
    l.append(s)
    c += 1
fr, sr, tr = l

#print(fr, sr, tr)
start = 0
constellation = ""
presentShape = ""
while start < n:
  if fr[start] == '#':
    constellation += '#'
    start += 1
  elif fr[start] == '.' and sr[start] == '.' and tr[start] == '.':
      start += 1
  else:
    #print(start)
    ## Taking 3x3 matrix from the current position
    presentShape = fr[start:start + 3] + sr[start:start+3] + tr[start : start + 3] 
    #print(presentShape)
    constellation += letters[presentShape] ## Getting the letter from the dict
    start = start + 3

print(constellation)
    
    
    
