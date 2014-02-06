import urllib2
from bs4 import BeautifulSoup

def get_mail_address(url):
    """
        Ignore content_type
    """
    body = get_mail_content(url)
    transform = transform_mail_page if url.split('.')[-1].lower() in ['html', 'htm', 'php'] else lambda x:x  
    return transform(body)

def get_mail_content(url):
    """
        Return HTML from a page
    """
    return urllib2.urlopen(url).read()

def transform_mail_page(data):
    soup = BeautifulSoup(data)
    for img in soup.find_all('img'):
        print img['src'],img.get('width'),img.get('height')
        new_src = 'http://placekitten.com/g/{}/{}'.format(img.get('width'),img.get('height'))
        img['src'] = new_src
    return soup.prettify().encode('utf8')

def serve(xxx):
    pass

if __name__ == '__main__':
    print get_mail_address('http://www.dailymail.co.uk/ushome/index.html')[:100]
    
    print get_mail_address('http://i.dailymail.co.uk/i/sitelogos/logo_mol.gif')[:100]