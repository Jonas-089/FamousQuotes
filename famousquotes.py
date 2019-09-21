import time
import bs4 as bs
from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.request import Request, urlopen
import random
import re


def main():

    print("This program retrieves quotes of celebrities.\n")
    person = input("Enter the name of a famous person or type 'exit' to exit the program.\n")

    while person != "exit" and person != "0":

        print("Your person is " + person + " – quotes are being searched. This may take a while.\n")

        print_quote(person)

        person = input("Enter the name of a famous person or type 'exit' to exit the program.\n")

    print("Goodbye.")


def print_quote(person):
    
    """
    Looks up the famous person and prints a random quote if found on the website, prints an error message if
    person was not found.
    :param person: the person whose quotes are being looked up
    """
    
    try:
        url = "https://www.brainyquote.com/authors/" + tokenizer(person)
        headers = {'User-Agent': 'Mozilla/5.0'}
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        quote_list = []
        random_gen = random.SystemRandom()

        for tag in soup.find_all("a", title="view quote"):
            if len(tag.text) > 0:
                quote_list.append(tag.text)

        ran = random_gen.randint(0, len(quote_list) - 1)
        print("'" + quote_list[ran] + "'" + "\n")

    except Exception:
        print("Unfortunately, something went wrong. Maybe there are no quotes available for this person.\n")


def tokenizer(person):
    
    """
    Support method. Prepares the name of the famous person to be appended to the url by inserting underscores.
    :param person: the person whose quotes are being looked up
    :return: the tokenized version of the name ready to be inserted into the url
    """

    tokenized = ""

    wordlist = person.split()

    for word in wordlist[:-1]:
        word = word.lower()

        tokenized += word + "_"

    tokenized += wordlist[-1].lower()

    return tokenized


if __name__ == '__main__':
    main()
