import urllib2
import SimpleHTTPServer
import SocketServer
import sys
import urllib
from bs4 import BeautifulSoup

PORT = int(sys.argv[1])


class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        print "GOT: %s" % (self.path, )
        if self.path == "http://www.dailymail.co.uk/":
            result= get_mail_address(self.path)
            self.wfile.write(result)
        else:
            self.copyfile(urllib.urlopen(self.path), self.wfile)
        self.wfile.flush()
httpd = SocketServer.TCPServer(("", PORT), Handler)

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

if __name__ == '__main__':
  print "Running proxy at: ", PORT
  httpd.serve_forever()
