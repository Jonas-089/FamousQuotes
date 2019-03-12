import time
import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.request import Request, urlopen
import random

def main():

    print("Dieses Programm gibt zufällige Zitate berühmter Persönlichkeiten aus.\n")

    while(True):
        person = input("Gib den Namen einer Person ein, um Zitate zu suchen, oder gib 'ende' ein,\n"
                       "um das Programm zu beenden.\n")

        if person == "ende" or person == "0":
            break

        print("\n")

        #print("Deine Person ist " + person + " – die Zitate werden gesucht. Das kann ein wenig dauern.")

        try:
            url = "https://www.brainyquote.com/authors/" + tokenizer(person)
            headers = {'User-Agent':'Mozilla/5.0'}
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")


            quote_list = []
            random_gen = random.SystemRandom()

            for tag in soup.find_all("a", title="view quote"):
                if(len(tag.text) > 0):
                #if tag.id != None:
                    quote_list.append(tag.text)

                #print(tag.text)

            ran = random_gen.randint(0, len(quote_list) - 1)
            print(quote_list[ran] + "\n")

            print("\n")

        except Exception:
            print("Leider ist etwas schiefgelaufen. Möglicherweise sind keine Zitate dieser Person verfügbar.")

def tokenizer(person):
    tokenized = ""

    wordlist = person.split()

    for word in wordlist[:-1]:
        word = word.lower()

        tokenized += word + "_"

    tokenized += wordlist[-1].lower()

    return tokenized

if __name__ == '__main__':
    main()