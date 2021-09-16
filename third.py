# https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/

import requests
from bs4 import BeautifulSoup

data = {}

def find_data(count):
    for j in range(1,count+1):
        # url = f"https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/?page={j}"
        url = f"https://www.examveda.com/computer-fundamentals/practice-mcq-question-on-computer-fundamental-miscellaneous/?section=2&page={j}"
        r = requests.get(url)
        htmlContent = r.content

        soup = BeautifulSoup(htmlContent,"html.parser")


        for questions in soup.find_all(class_='question single-question question-type-normal'):
            try:
                # print(questions.find('h2').get_text(),end='')
                key = questions.find(class_='question-number').get_text()
                temp = {}
                que = questions.find(class_='question-main').get_text()
                temp["questionStatement"] = que
                
                # extracting all options
                flag,i = True,1
                for option in questions.find_all('label'):
                    if not flag:
                        # print(option.get_text())
                        temp[f'option{i}'] = option.get_text()
                        i+=1
                    flag = not flag
                
                correctAnswer = questions.find_all('strong')[0].get_text()
                
                if 'Option A' in correctAnswer:
                    temp['correctAnswer'] = temp['option1']
                elif 'Option B' in correctAnswer:
                    temp['correctAnswer'] = temp['option2']
                elif 'Option C' in correctAnswer:
                    temp['correctAnswer'] = temp['option3']
                elif 'Option D' in correctAnswer:
                    temp['correctAnswer'] = temp['option4']
                else:
                    temp['correctAnswer'] = temp['option5']

                global data
                data[key] = temp
            except:
                continue

if __name__=='__main__':
    find_data(5)
    for k,v in data.items():
        columns = ','.join("`"+str(x).replace('/','_')+"`" for x in v.keys())
        values = ','.join("'"+str(x).replace('/','_')+"'" for x in v.values())
        sql = f"Insert Into Questions ({columns}) values ({values});"
        print(sql)

