from bs4 import BeautifulSoup
import urllib3
import random
import math

year = input("what year are we searching through?\n")


url = "http://www.imdb.com/search/title?release_date=" + year
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")

i = 0
movieArray = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
reducedArr = [0] * 50

for div_item in movieArray:
    div = div_item.find('div',attrs={'class':'lister-item-content'})
    #print (str(i) + '.')
    header = div.findChildren('h3',attrs={'class':'lister-item-header'})
   
    reducedArr[i] = (str((header[0].findChildren('a'))[0].contents[0].encode('utf-8').decode('ascii', 'ignore')))
    i += 1

def getScore(movie):
    url = movie
    ourUrl = urllib3.PoolManager().request('GET', url).data
    soup = BeautifulSoup(ourUrl, "lxml")
    result = soup.find('span',{"class":"mop-ratings-wrap__percentage"})
    try:
        rating = result.text
        print ("The score for this movie is: " + rating)
    except:
        print("Invalid RT website. You'll need to manually look that one up")

def pickMovie(arr):
    randomInt = math.floor(random.uniform(0,len(arr)-1))
    pick = arr[randomInt]
    print("=============================================")
    print("You can watch " + pick)
    pickFix = pick.replace(" ", "_")
    print("")
    rt = "www.rottentomatoes.com/m/" + pickFix
    #print("www.rottentomatoes.com/m/" + pickFix +"\n")
    getScore(rt)
    print("=============================================")

    repeat = input("\nWould you like to re-roll? (Yes/No)")
    if repeat == "Yes":
        del arr[randomInt]
        pickMovie(arr)

pickMovie(reducedArr)

    

