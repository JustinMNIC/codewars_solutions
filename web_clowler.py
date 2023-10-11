import requests
from bs4 import BeautifulSoup


def crawl_web(url, max_depth=3):
    visited_urls = set()
    crawl_queue = [(url, 0)]

    while crawl_queue:
        current_url, depth = crawl_queue.pop(0)

        if current_url in visited_urls or depth > max_depth:
            continue

        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Here you can add your code to extract information from the page
                print(f"Crawling {current_url}")
                # For example, print the page title:
                print(f"Title: {soup.title.string}")

                # Add links from the current page to the crawl queue
                links = soup.find_all('a')
                for link in links:
                    href = link.get('href')
                    if href and href.startswith('http'):
                        crawl_queue.append((href, depth + 1))

                visited_urls.add(current_url)
            else:
                print(f"Failed to retrieve {current_url} - Status code: {response.status_code}")
        except Exception as e:
            print(f"Error while processing {current_url}: {str(e)}")


if __name__ == "__main__":
    starting_url = "https://example.com"
    crawl_web(starting_url)