import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url, depth=0, visited=None):
  if visited is None:
    visited = set()

  if url in visited: return
  print(f"Level {depth}: {url}")
  visited.add(url)
  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for link in soup.find_all("a", href=True):
      if link["href"].startswith("#"): continue
      new_url = urljoin(url, link["href"])
      if not new_url.startswith(url): continue
      crawl(new_url, depth + 1, visited)
  except Exception as e: print("Error:", e)

if __name__ == "__main__":
  root = "https://mithibai.ac.in/"
  crawl(root)