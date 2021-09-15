# https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/

import requests
from bs4 import BeautifulSoup


url = "https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/"


# single-question

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent,"html.parser")

i = 1
for questions in soup.find_all(class_='question single-question question-type-normal'):
    try:
        print(questions.find('h2').get_text(),end='')
        flag = True
        for option in questions.find_all('label'):
            if not flag:
                print(option.get_text())
            flag = not flag
    except:
        continue
    # print(que)
    #    h2 = question['h2']
    #    que = h2['question-main']
    

    # print(i+" "+question['style'])