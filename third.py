# https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/

import requests
from bs4 import BeautifulSoup

data = {}

def find_data(count):
    for j in range(1,count+1):
        url = f"https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/?page={j}"

        r = requests.get(url)
        htmlContent = r.content

        soup = BeautifulSoup(htmlContent,"html.parser")


        for questions in soup.find_all(class_='question single-question question-type-normal'):
            try:
                # print(questions.find('h2').get_text(),end='')
                key = questions.find(class_='question-number').get_text()
                temp = {}
                que = questions.find(class_='question-main').get_text()
                temp["question"] = que
                
                # extracting all options
                flag,i = True,1
                for option in questions.find_all('label'):
                    if not flag:
                        # print(option.get_text())
                        temp[f'option{i}'] = option.get_text()
                        i+=1
                    flag = not flag
                
                correctAns = questions.find_all('strong')[0].get_text()
                
                if 'Option A' in correctAns:
                    temp['correctAns'] = temp['option1']
                elif 'Option B' in correctAns:
                    temp['correctAns'] = temp['option2']
                elif 'Option C' in correctAns:
                    temp['correctAns'] = temp['option3']
                elif 'Option D' in correctAns:
                    temp['correctAns'] = temp['option4']
                else:
                    temp['correctAns'] = temp['option5']
                
                global data
                data[key] = temp
            except:
                continue

find_data(3)
print(data)