import requests
import os
import argparse
from urllib.parse import urlsplit
from dotenv import load_dotenv


def shorten_link(token, url):
    short_url = 'https://api.vk.com/method/utils.getShortLink'
    params = {
        'access_token': token,
        'url': url,
        'v': '5.199'
    }

    response = requests.get(short_url, params=params)
    response.raise_for_status()
    short_link_response = response.json()

    if 'error' in short_link_response:
        raise ValueError(
            f"{short_link_response['error'].get('error_msg')}\n"
            f"код ошибки: {short_link_response['error'].get('error_code')}"
        )

    return short_link_response['response'].get('short_url')


def count_clicks(token, link):
    stats_url = 'https://api.vk.com/method/utils.getLinkStats'
    key = urlsplit(link)
    params = {
        'access_token': token,
        'key': key.path.replace('/', ''),
        'v': '5.199',
        'interval': 'forever',
        'extended': 0
    }

    response = requests.get(stats_url, params=params)
    response.raise_for_status()
    click = response.json()

    if 'error' in click:
        raise ValueError(
            f"{click['error'].get('error_msg')}\n"
            f"код ошибки: {click['error'].get('error_code')}"
        )

    return click['response']['stats'][0]['views']


def is_shorten_link(url):
    url_analysis = urlsplit(url)
    return 'vk.cc' in url_analysis.netloc


def main():
    load_dotenv()
    token = os.environ['VKCC_TOKEN']

    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, help='Нужно указать обычную или короткую ссылку')

    args = parser.parse_args()

    user_input = args.url

    try:
        if is_shorten_link(user_input):
            count_clicks_result = count_clicks(token, user_input)
            print(f'Кол-во переходов по ссылке: {count_clicks_result}')
        else:
            shorten_link_result = shorten_link(token, user_input)
            print(f'Сокращенная ссылка: {shorten_link_result}')

    except requests.exceptions.HTTPError as error:
        print(f"HTTP ошибка: {error}")
    except ValueError as error:
        print(f"Ошибка API: {error}")
    except Exception as error:
        print(f"Произошла ошибка: {error}")


if __name__ == '__main__':
    main()
