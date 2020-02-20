strarray = []

def create_perm(l,r,str):
	if r > l:
		if l > 0:
			create_perm(l-1,r,str+"(")
		create_perm(l,r-1,str+")")
	elif l > 0:
		create_perm(l-1,r,str+"(")
	if l == 0 and r == 0:
		strarray.append(str)

if __name__ == "__main__":
    size = int(input("Enter number of parentheses: "))
    create_perm(size,size,"")
    print(strarray)