from urllib.request import urlopen#urlopen is used to fetch the contents of a URL
import re
def download_page(url):
    return urlopen(url).read().decode("utf-8")#converting the url in utf-8
def extractlinks(page):
    link_regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)#to catch the links in the specific format
    return link_regex.findall(page)
if __name__=="__main__":
    target_url="http://www.apress.com/"
    apress=download_page(target_url)
    links=extractlinks(apress)
    for link in links:
        print(link)
    
    
