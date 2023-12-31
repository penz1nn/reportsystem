# Система сбора инцидентов

## Инструкция по началу работы

### Системные требования

Для работы необходим docker engine v20+ и docker-compose v2+

### Установка 

*Далее рассмотрена установка на Linux-подобную систему с установленным необходимым ПО.*

Чтобы установить приложение, извлеките содержимое архива в директорию к которой есть полный доступ и перейдите в неё.

Находясь в этой директории (в ней должен находиться извлечённый файл *docker-compose.yml*) выполните команду:

```
# docker-compose up --build --detach
```

Ожидайте загрузки и установки контейнеров, после чего приложение будет запущено и готово к работе. По умолчанию приложение станет доступно на порте 5000.

### Остановка работы приложения

Для того чтобы остановить работу приложения, выполните команду в директории приложения:

```
# docker-compose stop
```

### Запуск приложения

*Запуск приложения по данной инструкции доступен только после его первичной установки*

Для того чтобы вновь запустить приложение, выполните команду в директории приложения:

```
# docker-compose start
```

## Инструкция пользователя для API

### (POST) /problems

* Запрос:

    Данные в HTTP Заголовках и (опционально) данные в теле запроса в JSON.

* Ответ:

    Значение хеша для сохранённой записи


Пример запроса:
```
curl -X POST -H "Some-Data: Some Value" -d '{"sample": "text"}' http://localhost:5000/problems
```

Пример ответа:
```
1808455333
```

### (POST) /find

* Запрос:

    На вход в теле запроса - JSON с парами ключ-значение для поиска

* Ответ:

    Все ранее сохранённые записи в которых есть какие-либо пары ключ-значение из предоставленных


Пример запроса:
```
curl -X POST -d '{"sample": "text"}' http://localhost:5000/find
```

Пример ответа:
```
[{"body":{"sample":"text"},"headers":{"Accept":"*/*","Content-Length":"17","Content-Type":"application/x-www-form-urlencoded","Host":"localhost:5000","User-Agent":"curl/8.2.1"}},{"body":{"sample":"text"},"headers":{"Accept":"*/*","Content-Length":"18","Content-Type":"application/x-www-form-urlencoded","Host":"localhost:5000","Some-Data":"Some Value","User-Agent":"curl/8.2.1"}}]
```

### (GET) /find2

* Запрос:

    В URL параметре h - значение хеша для поиска

* Ответ:

    Все ранее сохранённые записи с таким значением хеша


Пример запроса:
```
curl http://localhost:5000/find2?h=1808455333
```

Пример ответа:
```
[{"body":{"sample":"text"},"headers":{"Accept":"*/*","Content-Length":"18","Content-Type":"application/x-www-form-urlencoded","Host":"localhost:5000","Some-Data":"Some Value","User-Agent":"curl/8.2.1"}}]
```
