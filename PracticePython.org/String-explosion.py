def string_splosion(str):
  l = []
  n = []
  for j in str:
    l.append(j)
  i = 0
  while i < len(l)+1:
      m = l[0:i]
      o = ''.join(m)
      n.append(o)
      i = i + 1
  n.pop(0)
  new_str = ''.join(n)
  print(new_str)

string_splosion('Code')
string_splosion('abc')
string_splosion('ab')
