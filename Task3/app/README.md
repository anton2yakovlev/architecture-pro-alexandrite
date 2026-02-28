Для удобства запустил все через docker-compose, надеюсь это не критично для задания.

# Запуск

Переходим в директорию `app`.

Собираем все сервисы: `docker-compose build`

Запускаем в фоне: `docker-compose up -d`


# Запущенные сервисы

Jaeger UI: http://localhost:16686

service-a: http://localhost:7001/docs

service-b: http://localhost:7002/docs

# Проверка

Сервис service-a косвенно вызывает service-b. Делаем запрос через swagger:

![Запрос через swagger](result/result-1.png)

Далее переходим в jaeger и находим этот вызов.

![trace запроса](result/result-2.png)

В детализации видно, что внутри service-a делает вызов к service-b и все корректно фиксируется в jaeger:

![trace запроса](result/result-3.png)
