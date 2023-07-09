def mdc(a,b):
	if b==0:
		return a
	return mdc(b,a%b)

def mdc2(a, b):
    if b == 0:
        return a
    elif b > 0 and a % b > 0:
        return mdc(b, a % b)
    else:
        return b

