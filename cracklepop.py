for x in xrange(1,101):
     if x%3==0 and x%5!=0:
          print"pop"
          continue
     elif x%5==0 and x%3!=0:
          print"crackle"
          continue
     elif x%5==0 and x%3==0:
          print"cracklepop"
          continue
     else:
          print x
