# otus_clickhouse_course_project
Course project on Clickhouse

Порядок установки
1) Создать виртуальную машины в Yandex Cloud с конфигурацией 4CPU и 32GB RAM, 250 GB HDD
2) Установть на ВМ СУБД Clickhouse
3) Создать в БД уменьшенный датасет hackernews (скрипты в каталоге sql), около 10 млн записей, выполнение займет около 12 часов (рекомендуется использовать tmux)
4) Склонировать на ВМ git репозиторий git clone https://github.com/AAKvashnin/otus_clickhouse_course_project
5) Установить Python 3.12, создать виртуальное окружение, установить в окружение пакеты из файла requirements.txt
6) Создать файл .env с параметрами DATABASE_HOST, DATABASE_USER, DATABASE_PASS, DEEPSEEK_API_KEY
7) Запустить приложение python main.py
8) Открыть приложение в браузере