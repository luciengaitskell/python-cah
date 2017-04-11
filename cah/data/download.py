from urllib.request import urlopen

def download_card_list(url):
    start_delete_str = 'cards='

    data = str(urlopen(url).read().decode('utf-8'))
    start_index = data.find(start_delete_str) + len(start_delete_str)
    data = data[start_index:]
    return data

with open("bin/answer.txt", "w") as f:
    f.write(download_card_list("http://www.cardsagainsthumanity.com/wcards.txt"))

with open("bin/question.txt", "w") as f:
    f.write(download_card_list("http://www.cardsagainsthumanity.com/bcards.txt"))
    f.write(download_card_list("http://www.cardsagainsthumanity.com/bcards1.txt"))
    f.write(download_card_list("http://www.cardsagainsthumanity.com/bcards2.txt"))
