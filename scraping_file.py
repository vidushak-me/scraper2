from bs4 import BeautifulSoup
import requests
from constant import *
import datetime


def get_title(title_soup):
    title = title_soup.find(title_tag)
    return title.string.strip()


def get_image_url(soup):
    img_url = " "
    responce = soup.find_all(image_tag)
    for img in responce:
        img_url += f"'{img['src']}',"
    return img_url


def get_subtitles(article_body_soup):
    subtitles = " "
    table = article_body_soup.find_all(subtitle_tag)
    for row in table:
        subtitles += f"'{row.text.strip()}'"
    return subtitles


def get_content(article_body_soup):
    content = " "
    table = article_body_soup.find_all(content_tag)
    for row in table:
        content += f"{row.text.strip()},"
    return content


def get_hash_tags(main_header_soup):
    hash_tags = " "
    response = main_header_soup.find(class_=hashtag_class)
    for row in response.find_all(hashtag_tag):
        hash_tags += f"'{row.text.strip()}' : '{row['href']}',"
    return hash_tags


def get_code(article_body_soup):
    codes = " "
    tables = article_body_soup.findAll(codes_tag)
    for line in tables:
        codes += f"{line.text.strip()}"
    return codes


def get_auther_name(soup):
    auther = soup.find(class_=auther_class)
    return auther.text.strip()


def get_auther_bio(soup):
    auther_bio = soup.find(class_=auther_bio_class)
    return auther_bio.text.strip()


def get_post_date(main_auther_soup):
    time = main_auther_soup.find(post_tag)
    date =  time['datetime']
    format_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%Sz")
    return datetime.date.strftime(format_date, '%Y-%m-%d')

def get_hearts(hearts_soup):
    loves = []
    hearts = hearts_soup.find(id=Id_hearts)
    loves.append(hearts.text.strip())
    return loves

def get_scraped(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    main_header_soup = soup.find(id=Id_main_title)
    article_body_soup = soup.find(id=Id_article_body)
    #hearts_soup = soup.find(class_='crayons-article-actions__inner')

    dev = {}
    dev['title'] = get_title(main_header_soup)
    dev['subtitle'] = get_subtitles(article_body_soup)
    dev['content'] = get_content(article_body_soup)
    dev['img_url'] = get_image_url(soup)
    dev['hash_tags'] = get_hash_tags(main_header_soup)
    dev['codes'] = get_code(article_body_soup)
    dev['auther_name'] = get_auther_name(main_header_soup)
    dev['auther_bio'] = get_auther_bio(soup)
    dev['post_date'] = get_post_date(main_header_soup)
    #dev['no_of_hearts'] = get_hearts(soup)
    return dev

