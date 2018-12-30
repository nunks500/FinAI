import requests
import time
from itertools import groupby
from operator import itemgetter
from bs4 import BeautifulSoup
from collections import Counter

def print_iteration(res, dataToWrite):
    for element in res:
        if element[0].isalpha():
            dataToWrite += element[0] + "--" + str(element[1]) + "\n"

    return dataToWrite

def page_crawler(iteration, dataToWrite):

    print('--Iteration-- ' + str(iteration))
    page = 1
    number_of_elements = 20
    current_elements = 0
    x = list()
    time_to_wait_in_seconds = 600 # waits for 10 minutes to do the process again

    while (number_of_elements > current_elements):
        url = "https://www.finai.pl/blog?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.findAll('a', {'class': 'entry-title'}):
            if number_of_elements > current_elements:
                x = x + Counter(link['title'].lower()).most_common()
                current_elements +=1

        res = [(k, sum(map(itemgetter(1), g)))
               for k, g in groupby(sorted(x, key=itemgetter(0)), key=itemgetter(0))] #sums ocurrences of all alpha characteres
        page += 1

    print('--Most used letters with frequency--')
    for element in res:
        if element[0].isalpha():   # if element is not ' ' or '-' , etc
            print(element)

    time.sleep(time_to_wait_in_seconds)
    dataToWrite += '#Iteration ' + str(iteration) + "\n"
    iteration += 1

    if(iteration <= 5):
        dataToWrite = print_iteration(res, dataToWrite)
    else:
        iterations = dataToWrite.split("#")  #if there are more than 5 iterations, the oldest record will be deleted
        dataToWrite = "#" + iterations[2] + "#" + iterations[3] + "#" + iterations[4] + "#" + iterations[5] + '#Iteration ' + str(iteration - 1) + "\n" + print_iteration(res, "")

    file = open("data.txt", "w", encoding='utf-8')
    print(dataToWrite)
    file.write(dataToWrite)
    file.close()

    page_crawler(iteration, dataToWrite)

page_crawler(0,"") #begins as an empty string, and while it iterates it fills up