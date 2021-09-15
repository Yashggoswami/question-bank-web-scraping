import requests
from bs4 import BeautifulSoup

# url ="https://www.sanfoundry.com/advanced-java-questions-answers-application-lifecycle-ant-maven-jenkins/"
url = "https://www.sanfoundry.com/java-mcqs-integer-floating-data-types/"

s = set()
count = 3

# function for finding links to get data from

def get_all_link(url):
    s.add(url)
    global count
    count-=1
    if count <=0:
        return
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,'html.parser')
    link = None    
    for data in soup.select('header a'):
        if data.text == 'Next':
            link = data['href']
            break
    if link:
        get_all_link(link)

get_all_link(url)

print(s)



# function to find data from link

def find_data(url):
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,'html.parser')

    for data in soup.find_all("div",class_ ="entry-content"):
        st = data.get_text().replace("advertisement", "")
        print(st)
    print("<=========================== page break ========================>")


for link in s:
    find_data(link)
    















# r = requests.get(url)
# htmlContent = r.content
# print(htmlContent)

# soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.find_all('p'))
# print(soup.find('header')('a')[0]['href'])
# s = set()
# def get_all_data(url):
#     s.add(url)
#     r = requests.get(url)
#     htmlContent = r.content
#     soup = BeautifulSoup(htmlContent, 'html.parser')
#     link = soup.find('header')('a')
#     print(link)
    # for data in soup.find_all('p'):
    #     st = data.get_text().replace("\n", "")
    #     print(st)
    # print("hello")
#     if len(link) < 2:
#         return
#     newlink = link[1]['href']
#     get_all_data(newlink)


# get_all_data(url)
# print(s)
# for data in soup.find_all('p'):
#     st = data.get_text().replace("advertisement","")
#     st1 = st.replace('\n','')
#     print(st1)


