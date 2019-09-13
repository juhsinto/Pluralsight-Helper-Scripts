from bs4 import BeautifulSoup

with open("page.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    result = soup.find_all('section', 'module open')	
    idx = 1
    print "----------------- Chapter Headings -----------------"
    for tag in result:
    	# gets the chapter heading
    	h2_element = tag.find_all('h2')
    	for tag in h2_element:
    		print str(idx) + " - " + tag.text
    		idx = idx + 1
    	print "-"
    	# break

    idx = 1
    print "----------------- Chapter Titles -----------------"
    for tag in result:
    	# gives the chapter titles
    	result = tag.find_all('h3')
    	for tag in result:
    		print str(idx) + " - " + tag.text
    		idx = idx + 1
    	print "-"
    	
