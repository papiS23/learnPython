def domain_name(url):
    if 'www' in url:
        return url[url.index('www')+4:url.index('.', url.index('.')+1)]
    elif 'http://' in url or 'https://' in url:
        return url[url.index('/')+2:url.index('.')]
    else:
        return url[0:url.index('.')]

print(domain_name('https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python'))