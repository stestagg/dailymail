import urllib2

def get_mail_address(url):
    body = get_mail_content()
    return transform_mail_page(body)

def get_mail_content(url):
    """
        Return HTML from a page
    """
    return urllib2.urlopen(url).read()

def transform_mail_page(data):
    pass
#     return xxx(data)

def serve(xxx):
    pass

if __name__ == '__main__':
    print get_mail_content('http://www.dailymail.co.uk/ushome/index.html')