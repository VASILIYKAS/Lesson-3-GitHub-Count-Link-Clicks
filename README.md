# Обрезка ссылок с помощью Битли
Это скрипт для получения сокращенной версии ссылки, которая 
ведет туда же куда и обычная ссылка. Например, вот эта: 
https://gist.github.com/dvmn-tasks/4a570d33bac973b0f4681cff520f6c6c \
и эта: https://vk.cc/cFFUvY это одна и та-же ссылка. Так же можно получить информация о количестве переходов
по короткой ссылке, если вместо обычной ссылке ввести короткую.
## Как установить

Для работы скрипта нужен "**Сервисный ключ доступа**", получить его можно после
создания приложения, ознакомиться можно 
[тут](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/tokens/service-token).
Выглядит ключ примерно так: `9ec2158c2ff8438c4cc8438rr02gec112c66ll76kk0476c2eu2011f3b4a779v4ec200l1`
Его нужно указать в файле `.env`, должно быть так: `VKCC_TOKEN="Здесь ваш сервисный ключ доступа"`

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:\
`pip install -r requirements.txt`

## Как запустить
1. Для запуска скрипта необходимо открыть терминал или командную строку.
2. Перейти в папку, где находится файл `main.py`. Для перехода используйте команду `cd`. Для перехода между 
дисками необходимо указать имя диска.
3. Ввести команду для запуска скрипта `python main.py "ваша ссылка"`\
Пример:\
[![Пример](https://i.postimg.cc/ZKhtWNSj/Screenshot-cmd.png)](https://postimg.cc/Dm5YD8mb)
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/)