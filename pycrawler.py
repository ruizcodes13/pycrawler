import requests
from bs4 import BeautifulSoup

response = requests.get("http://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
for question in questions:
    print(questions.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())
