
from bs4 import BeautifulSoup, SoupStrainer
import requests

class Data_collector():
    def __init__(self):

        first_link = "https://www.azlyrics.com/l/lanadelrey.html"
        self.first_link = first_link

    def saving_links(self):
        page = requests.get(self.first_link)    
        data = page.text
        soup = BeautifulSoup(data)

        f = open("links_to_songs.txt", "w")

        for link in soup.find_all('a'):
            for link2 in soup.find_all('href'):
                #all_link = link.get('href')
                f.write(link2)

        f.close()
        
    def collecting_text_of_songs(self):
        f = open("links_to_songs.txt") 
        link1 = f.readline()
        link2 = f.readline()
        return link1, link2


col = Data_collector()
col.saving_links()
l1, l2 = col.collecting_text_of_songs()
print("First link %s" % l1)
print("Second link %s" % l2)