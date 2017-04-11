from urllib.request import urlopen
import os


def download_card_list(url):
    start_delete_str = 'cards='

    data = str(urlopen(url).read().decode('utf-8'))
    start_index = data.find(start_delete_str) + len(start_delete_str)
    data = data[start_index:]
    return data

with open(os.path.join(os.path.dirname(__file__), "bin/answer.txt"), "w") as f:
    f.write(download_card_list("http://www.cardsagainsthumanity.com/wcards.txt"))

with open(os.path.join(os.path.dirname(__file__), "bin/question.txt"), "w") as f:
    f.write(download_card_list("http://www.cardsagainsthumanity.com/bcards.txt"))
    f.write(download_card_list("http://www.cardsagainsthumanity.com/bcards1.txt"))
    f.write(download_card_list("http://www.cardsagainsthumanity.com/bcards2.txt"))
