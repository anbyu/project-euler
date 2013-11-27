def main():
	ns = range(99)
	lns = len(ns)
	sns = map(str, ns)
	ds = range(100)
	lds = len(ds)
	sds = map(str, ds)
	
	dds = []
	nns = []
	
	for i in xrange(11, lns):
		n = ns[i]
		if n % 10 == 0:
			continue
		sn = sns[i]
		for j in xrange(n + 1, lds):
			d = ds[j]
			if d % 10 == 0:
				continue
			sd = sds[j]
			
			r = float(d) / n
			
			for ii in range(2):
				for jj in range(2):
					if sn[ii] == sd[jj]:
						nn = int(sn[1 - ii])
						dd = int(sd[1 - jj])
						
						if float(dd) / nn == r:
							nns.append(nn)
							dds.append(dd)
							print n, d, nn, dd
	pn = 1
	pd = 1
	ldds = len(dds)
	for i in xrange(ldds):
		pn *= nns[i]
		pd *= dds[i]
		
	print pn, pd
	return pd
	
print main()