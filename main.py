leet = {'a':'4','b':'13','c':'(','d':'[)','e':'3','f':'f','g':'6','h':'|-|','i':'|','j':'j',
'k':'|<','l':'1','m':'m','n':'/\/','o':'0','p':'|>','q':'q','r':'|2','s':'5','t':'7','u':'|_|','v':'\/',
'w':'w','x':'}{','y':'y','z':'2'}

def convertToLeet(inp):
	a=[]
	arr = inp.split(" ")	
	for word in arr:
		for i in word:
			a.append(leet[i])
		a.append(" ")

	print "LEET EQUIVALENT:"
	print "".join(a)

inp = raw_input("Enter string: ")
convertToLeet(inp)