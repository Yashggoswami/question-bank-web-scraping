# https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/

import requests
from bs4 import BeautifulSoup


# url = "https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/"

url = "https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/?page=2"

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
        # j = 1
        
        # for cur in questions.find_all('i'):
        #     if 'text-success' in cur['class']:
        #         print("correct ans is "+j)
        #         break
        #     j+=1
    except:
        continue
    # print(que)
    #    h2 = question['h2']
    #    que = h2['question-main']
    

    # print(i+" "+question['style'])