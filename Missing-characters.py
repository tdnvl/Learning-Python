def missing_char(str, n):
  templist = []
  for i in str:
   templist.append(i)
  templist.pop(n)
  print(''.join(templist))

missing_char('Kitten',3)
missing_char('Kitten',5)
missing_char('Kitten',1)
