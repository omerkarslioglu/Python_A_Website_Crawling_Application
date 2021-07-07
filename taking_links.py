from bs4 import BeautifulSoup
import requests
import urllib

def take_link_lists(url):
#    sayfa = urllib.request.urlopen(url)
#    soup = BeautifulSoup(sayfa, "html.parser")
#    ana=soup.find("body")
#    alt=ana.findAll("section",attrs={"class":"story"})
#    for i in alt:
#        textt=(i.href.text.strip())
#        print("\n"+textt)

    r=requests.get(url)
    soup=BeautifulSoup(r.content,"html.parser")
    linkler=soup.find_all("a",attrs={"class":"story"})
    links_list=[]
    for link in linkler:
        a=link.get("href")
        if a!=None and a!='#' and a!='/' and a!='h' and a!='https' and 'https' in a:
            links_list.append(a)

    return links_list
#url="https://www.dailystar.co.uk/news/latest-news/779548/derby-frank-lampard-bar-bill-play-off-leeds-aston-villa"
#print(take_link_lists(url))
#print(len(take_link_lists(url)))

