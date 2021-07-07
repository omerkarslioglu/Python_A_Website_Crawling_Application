from taking_links import take_link_lists
from main import main_process

def crawl(url,depth,html_or_text_title,number_for_name=0):
    try:
        if depth<0:
            return
        else :
            link_list=take_link_lists(url)
            main_process(url,html_or_text_title,number_for_name)
            for alink in link_list:
                crawl(alink,depth-1,html_or_text_title,number_for_name+1)
    except FileNotFoundError:
        return
    return


url='https://www.dailystar.co.uk/news/latest-news/779548/derby-frank-lampard-bar-bill-play-off-leeds-aston-villa'

print("******************************************************************************")
print("***** Newspaper Webpage Crawling Program v1.0 Powered by Omer Karslioglu *****")
print("******************************************************************************")

print("\nOur Url Is "+" ' "+url+" ' ")

print("\nThe address to save data : C:/Users/Ömer/Documents/pyhton_project ")

print("\nEnter (0) To Save(as .txt) and Take Title-Text From The Link "
      + "\nEnter (1) To Save(as .html) and Take Html Codes From The Link "
      + "\nEnter (2) To Do Both Of Them")
htott=int(input("Please Enter : "))

print()

depth=int(input("Please Enter The Depth (How You Want) : "))

crawl(url,depth,htott)
