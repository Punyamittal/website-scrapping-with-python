from urllib.request import urlopen#urlopen is used to fetch the contents of a URL
import re
def download_page(url):
    return urlopen(url).read().decode("utf-8")#converting the url in utf-8
def extract_image_location(page):
    img_regex=re.compile('<img[^>]+src=["\'](.*?)["\']',re.IGNORECASE)#to catch the images in the specific format
    return img_regex.findall(page)
if __name__=="__main__":
    target_url="http://www.apress.com/"
    apress=download_page(target_url)
    image=extract_image_location(apress)
    for img in image:
        print(img)
    
    
