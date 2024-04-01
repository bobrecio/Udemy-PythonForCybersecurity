from urllib import response
import requests
import json


def display_books(start, end):
    try:
        print("------------")
        for book in results[start:end]:
            print(f"{results.index(book)}: {book['title']}")
        print("------------")
    except:
        print("That didn't work(display_books)")


base_url = 'https://gutendex.com/books?search='
no_results = True

try:
    while no_results == True:
        keywords = input(
            "Please enter keywords to search Titles and Author Names\n(seperated words by a space; use + to join multi-word keywords) >> ")

        query = keywords.replace(" ", "%20")

        r = requests.get(f'{base_url}{query}')

        results = r.json()["results"]

        if len(results) < 1:
            print("No results. Try another keyword.")
            no_results = True
        else:
            no_results = False
except:
    print("Something went wrong while calling API")

range_start = 0
range_end = 10
choice = ""

while choice != "q":
    match choice:
        case "n":
            if (range_start + 11 < len(results)):
                range_start += 10
                range_end += 10
            display_books(range_start, range_end)
            # print("------------")
            # for book in results[range_start:range_end]:
            #     print(f"{results.index(book)}:  {book['title']}")
            # print("------------")
        case "p":
            if (range_start - 10 >= 0):
                range_start -= 10
                range_end -= 10
            display_books(range_start, range_end)
        case "s":
            try:
                index = int(input("\nSelect a book by index >> "))
                book = results[index]
                book_id = book["id"]
                book_title = book["title"]
                book_author = book["authors"][0]["name"]
                book_downloads = book["download_count"]
                print(
                    f"============\n| Guten.ID: {book_id}\n| Title: {book_title}\n| Author: {book_author}\n| Downloaded {book_downloads} times\n============")
            except:
                print("That didn't work")
        case _:
            display_books(range_start, range_end)

    choice = input("Choose: (n)ext, (p)revious, (s)elect, (q)uit >> ")

print("Quitting")
