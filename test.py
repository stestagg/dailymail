from bs4 import BeautifulSoup



#print(soup.prettify())


def main():
	mail = open('mail.html')
	soup = BeautifulSoup(mail.read())
	for img in soup.find_all('img'):
		print img['src'],img.get('width'),img.get('height')
		new_src = 'http://placekitten.com/g/{}/{}'.format(img.get('width'),img.get('height'))
		img['src'] = new_src
	print(soup.prettify())
	mailOut = open('out.html','w')
	mailOut.write(soup.prettify().encode('utf8'))

if __name__ == "__main__":
	main()

