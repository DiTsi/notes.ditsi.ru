# BeautifulSoup, bs4

## Code example

```Python
from bs4 import BeautifulSoup

page_source = request.urlopen(full_url).read()
soup = BeautifulSoup(page_source, "html.parser")
pager = soup.find("div", {"data-qa": "pager-block"})
elements_list_1 = pager.findAll("dev", {"class": "class_name class2", "data-qa": "pager-page"})
elements_list_2 = pager.findAll("input", {"class": "class_name class3", "data-qa": "pager-page"})
element = pager.find("a", {"class": "class_name class4", "data-qa": "pager-page"})

# search inside elements_list_1
elements_list_1.findAll("a", {"class": "class_name class2"})
```