import requests
import json

#items, volumeInfo are from the api not python inbuilt
# or predefined variable
base_url = 'https://www.googleapis.com/books/v1/volumes?q='

api_url = requests.get(base_url + 'soldier')
response = api_url.json().get('items') #convert to json and get the item list

book_details = [response[i].get('volumeInfo') for i in range(len(response))]#get volumeInfo of every item
book_details = json.dumps(book_details, indent=2)

for i in book_details:
    print(i)
    print("\n\n")

"""
all_books = {0:[title, author, image], 1:{title, author, image}, 2:{title, author, image}, 3:{title, author,}}
"""
#key = "AIzaSyBqxMPJz7YhN7RoB0U2-3iArbjLiroHw1c"


























"""
import requests

url = "https://www.googleapis.com/"

querystring = {"key":"AIzaSyBqxMPJz7YhN7RoB0U2-3iArbjLiroHw1c"}

headers = {
"X-RapidAPI-Host": "https://www.googleapis.com/books/v1/",
"X-RapidAPI-Key": "AIzaSyBqxMPJz7YhN7RoB0U2-3iArbjLiroHw1c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
"""