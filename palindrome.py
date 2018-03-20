a = raw_input()
rev_a = reversed (a)
if list(a) == list(rev_a):
    print("yes")
else:    
    print("no")
