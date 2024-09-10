# e365

## Переменные окружения

| Имя | значение по умолчанию | обязательное | описание |
|-----|-----------------------|--------------|----------|
| SECRET_KEY | '' | да | Секретный ключ для конкретной установки Django. Используется для обеспечения криптографической подписи, и его значение должно быть уникальным и непредсказуемым. |
| DJANGO_DEBUG | false  | нет | Никогда не развертывайте сайт в производстве с включенной DEBUG |
| DJANGO_ALLOWED_HOSTS | '' | да | Список строк, представляющих имена хостов/доменов, которые может обслуживать этот сайт Django. |
| SQL_ENGINE | django.db.backends.sqlite3 | нет | |
| SQL_HOST | localhost | нет | |
| DBNAME | db.sqlite3 | нет | |
| DBUSER | user | нет | |
| DBPASS | password | нет | |
