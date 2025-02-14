# selenium

## Code example

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

download_path = os.path.realpath("./downloads")

prefs = {'download.default_directory' : download_path}

chrome_options = Options()
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent={Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36}")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)
driver.get("http://google.com")

...

driver.close()
```

## Docker errors and solution

```python
error: DevToolsActivePort file doesn't exist
solution: Try to add Chrome options --no-sandbox and --disable-dev-shm-usage
```

## Cookies between sessions:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pickle
import os


password = "jkhsdiuhw"
username = "sdiuwhs@gmail.com"


def main():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-data-dir=selenium")
    chrome_options.add_argument("user-agent={Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36}")
    driver = webdriver.Chrome(options=chrome_options)

    if os.path.exists("cookies.dump"):
        cookies = pickle.load(open("cookies.dump", "rb"))
        for cook in cookies:
            driver.add_cookie(cook)
        driver.get("https://www.duolingo.com/")
    else:
        driver.get("https://www.duolingo.com/")
        driver.find_element_by_id("sign-in-btn").click()
        driver.find_element_by_id("top_login").send_keys(username)
        driver.find_element_by_id("top_password").send_keys(password)
        driver.find_element_by_id("login-button").click()

    cookies_new = driver.get_cookies()
    pickle.dump(cookies_new, open("cookies.dump", "wb"))

    sleep(5)
    driver.close()


if __name__ == "__main__":
    main()
```

## Подход к поиску элементов с selenium

Открыть интересующую страницу

```python
driver.get("http://google.com")
```

Посмотреть код открытой страницы

```python
source_code = driver.page_source
```

Найти интересующие элементы в коде. Если они там есть, перейти к следующему шагу

Найти элементы, используя driver.find_elements_by_xpath или схожие команды. Пример:

```python
elements_list = driver.find_elements_by_xpath("//input[@name='username' and @name='username']")[1]
```

Если элемент один, заменить **driver.find_elements_by_xpath** на **driver.find_element_by_xpath**