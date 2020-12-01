from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import urllib.request
import re



url = input("Which page would you like to check? Enter full URL: ")
keyword = input("What is your SEO Keyword?")
html = urllib.request.urlopen(url).read()

keyword = keyword.casefold()

try:
    req = Request(url, headers = {'User-Agent': 'Mozilla/6.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'})
    html = urlopen(req)
except HTTPError as e:
    print(e)
   


data = BeautifulSoup(html, "html.parser")

def seo_title_found(keyword, data):

    if data.title:
        if keyword in data.title.text.casefold():
            status = "Found"

        else:
            status = "Keyword Not Found"

    else:
        status = "No title found"
    return status


def seo_title_stop_words(data):
    words = 0
    list_words = []
    if data.title:
        with open('stopwords.txt', 'r',) as f:
            for line in f:
                if re.search(r'\b' + line.rstrip('\n') + r'\b', data.title.text.casefold()):
                    words += 1
                    list_words.append(line.rstrip('\n'))
        if words > 0:
            stop_words = "we found  {} stop words in your title. You should consider removing them. {}".format(words, list_words)
        else:
            stop_words = "We found no Stop words in the title. Good Work"
    else:
        stop_words = "we could not find a title"
    
    return stop_words


def seo_title_length(data):
    if data.title:
        if len(data.title.text) < 60:
            length = "Your Length is under the maximum suggested length of 60 characters. Your title is {}".format(len(data.title.text))
        else:
            length = "Your length is over the maximum suggest length of 60 character. Your title is {}".format(len(data.title.text))

    else:
        length = "No title was found"

    return length


def seo_url(url):
    if url:
        if keyword in url:
            slug = "Your keyword is found in your slug"
        else:
            slug = "Your Keyword was not found in your slug. It is suggested to add keyword to your slug"
    else:
        slug = "No url was returned"

    return slug



def seo_url_length(url):
    if url:
        if len(url) < 100:
            url_length = "Your URL is less than the 100 character maximum suggested length, Good Work"
        else:
            url_length = "Your URL length is over 100 characters. Your URL currently is {}. You Should change this.".format(len(url))
    else:
        url_length = "URL was not found"

    return url_length


def seo_h1(keyword, data):
    h1_tag = ''
    if data.h1:
        all_tags = data.find_all('h2')
        for tag in all_tags:
            tag = str(tag.string)
            if keyword in tag.casefold():
                h1_tag = "Found Keyword in h1 tag. You have a total of {} H1 Tags and your keyword was found in {} of them". format()
            else:
                h1_tag = "Did not find a keyword in h1 tag."
    else:
        h1_tag = "No H1 tags Found."

    return h1_tag



def seo_h2(keyword,data):
    if data.h2:
        all_tags = data.find_all('h2')
        for tag in all_tags:
            tag = str(tag.string)
            if keyword in tag.casefold():
                h2_tag = "Found your keyword in atleast one h2 tag"
            else:
                h2_tag = "we did not find your keyword in a single h2 tag. you should add {} to h2 tag".format(keyword)
    else:
        h2_tag = "No h2 tags found. you should have atleast one containing your keyword "

    return h2_tag



print(seo_title_found(keyword, data))
print(seo_title_stop_words(data))
print(seo_title_length(data))
print(seo_url(url))
print(seo_url_length(url))
print(seo_h1(keyword, data))
print(seo_h2(keyword,data))