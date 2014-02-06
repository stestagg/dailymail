import urllib2

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
    return data

def serve(xxx):
    pass

if __name__ == '__main__':
    print get_mail_address('http://www.dailymail.co.uk/ushome/index.html')[:100]
    
    print get_mail_address('http://i.dailymail.co.uk/i/sitelogos/logo_mol.gif')[:100]