from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(open("nav.html".decode('utf-8') ,"r").read())
tab = soup.findAll('a')

print (len(tab))
i=0
for t in tab:
	print (t['href'])
	fi = open(t['href'],"rb")
	txt = fi.read()
	fi.close()
	start=i-3
	if i<4: start=0
	if i>len(tab)-4: start = len(tab)-7
	lnks=""
	j=0
	while(j<7):
	   lnks += str(tab[j+start]) + "<br>\r\n"
	   j += 1
	#print(lnks)
	dc = "<div class=\"nav\">"
	start = txt.find(dc)
	end = txt[start:].find("</div>")
	#print(start,end, len(lnks))
	htm = txt[:start+len(dc)] + "\r\n"
	htm += lnks
	htm += txt[start+end:]
	#print(htm)
	fo = open(t['href'],"wb")
	fo.write(htm)
	fo.close()
	i += 1
#help(soup)
