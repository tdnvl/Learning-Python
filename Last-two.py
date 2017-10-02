def last2(str):
  end_sub = str[-1:-3:-1]
  end_sub = end_sub[::-1]
  # print(end_sub)
  if str.count(end_sub) >= 2:
      # print(str.count(end_sub) - 1)
      print(str.count(end_sub) - 1)
  else:
      print(0)
last2('hixxhi')
last2('axxxaaxx')
last2('jflkanvaionzz')
