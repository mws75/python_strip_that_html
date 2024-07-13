import requests 
from bs4 import BeautifulSoup as bs 

def strip_that_html(url: str) -> str: 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    if response.status_code == 200:
        html_content = response.text
        soup = bs(html_content, "html.parser")
        html = soup.prettify()
        print(html)

def main():
    url = "https://www.alltrails.com/us/california/los-angeles"
    strip_that_html(url)

if __name__ == "__main__":
    main()