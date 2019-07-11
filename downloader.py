import requests
import argparse
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.2171.95 Safari/537.36'}


def download_url(pastvu_url):
    resp = requests.get(pastvu_url, headers=headers)
    if resp.status_code == 404:
        print('requested page [{}] not found'.format(
            pastvu_url))
    if resp.status_code == 200:
        page = resp.content.decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        pastvu_url = soup.find('meta', property='og:url')
        pastvu_title = soup.find('meta', property='og:title')
        pastvu_description = soup.find('meta', property='og:description')
        pastvu_image = soup.find('meta', property='og:image')
        print(pastvu_url["content"] if pastvu_url else "No meta url given")
        print(pastvu_title["content"] if pastvu_title else "No title found")
        print(pastvu_description["content"]
              if pastvu_description else "No description found")
        print(pastvu_image["content"]
              if pastvu_description else "No image found")
        download_file = requests.get(pastvu_image["content"], stream=True)
        data_dir = './data/'
        name = pastvu_title["content"]
        if '/' in name:
            name = name.replace('/', '')
        resulting_name = data_dir + name
        with open(resulting_name + '.jpg', 'wb') as f:
            for chunk in download_file.iter_content(chunk_size=1048576):
                if chunk:
                    f.write(chunk)
        with open(resulting_name + '.txt', 'w', encoding='utf-8') as f:
            f.write('url: %s\n' %
                    pastvu_url["content"] if pastvu_url else "No meta url given")
            f.write('title: %s\n' %
                    pastvu_title["content"] if pastvu_title else "No title found")
            f.write('description: %s' %
                    pastvu_description["content"] if pastvu_description else "No description found")
#        for link in soup.find_all('link', {'rel':'next'}):
#            next_url = soup.select("[rel='next']")[0]['href']
#            download_url(next_url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', nargs='+', help='package to upgrade')
    parser.add_argument('--file', help='file with packages list')
    args = parser.parse_args()
    if args.file is not None:
        with open(args.file) as file:
            for line in file:
                print('downloading %s' % line)
                package = line.strip()
                download_url(package)

    if args.url is not None:
        urls = [i for i in args.url if i is not None]
        for url in urls:
            # clear lists
            download_url(url)
