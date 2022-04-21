本文将列出应用性能观测支持的 Python 框架及组件。

| 项目                                                         | Python 版本 - Lib 版本                                       | 插件名称            |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :------------------ |
| [aiohttp](https://docs.aiohttp.org/)                         | Python >=3.10 - NOT SUPPORTED YET; Python >=3.6 - [‘3.7.4’]; | `sw_aiohttp`        |
| [celery](https://docs.celeryproject.org/)                    | Python >=3.6 - [‘5.1’];                                      | `sw_celery`         |
| [django](https://www.djangoproject.com/)                     | Python >=3.6 - [‘3.2’];                                      | `sw_django`         |
| [elasticsearch](https://github.com/elastic/elasticsearch-py) | Python >=3.6 - [‘7.13’, ‘7.14’, ‘7.15’];                     | `sw_elasticsearch`  |
| [hug](https://falcon.readthedocs.io/en/stable/)              | Python >=3.10 - [‘2.5’, ‘2.6’]; Python >=3.6 - [‘2.4.1’, ‘2.5’, ‘2.6’]; | `sw_falcon`         |
| [flask](https://flask.palletsprojects.com/)                  | Python >=3.6 - [‘1.1’, ‘2.0’];                               | `sw_flask`          |
| [http_server](https://docs.python.org/3/library/http.server.html) | Python >=3.6 - ['*'];                                        | `sw_http_server`    |
| [werkzeug](https://werkzeug.palletsprojects.com/)            | Python >=3.6 - [‘1.0.1’, ‘2.0’];                             | `sw_http_server`    |
| [kafka-python](https://kafka-python.readthedocs.io/)         | Python >=3.6 - [‘2.0’];                                      | `sw_kafka`          |
| [psycopg[binary\]](https://www.psycopg.org/)                 | Python >=3.6 - [‘3.0’];                                      | `sw_psycopg`        |
| [psycopg2-binary](https://www.psycopg.org/)                  | Python >=3.10 - NOT SUPPORTED YET; Python >=3.6 - [‘2.9’];   | `sw_psycopg2`       |
| [pymongo](https://pymongo.readthedocs.io/)                   | Python >=3.6 - [‘3.11’];                                     | `sw_pymongo`        |
| [pymysql](https://pymysql.readthedocs.io/en/latest/)         | Python >=3.6 - [‘1.0’];                                      | `sw_pymysql`        |
| [pyramid](https://trypyramid.com/)                           | Python >=3.6 - [‘1.10’, ‘2.0’];                              | `sw_pyramid`        |
| [pika](https://pika.readthedocs.io/)                         | Python >=3.6 - [‘1.2’];                                      | `sw_rabbitmq`       |
| [redis](https://github.com/andymccurdy/redis-py/)            | Python >=3.6 - [‘3.5’];                                      | `sw_redis`          |
| [requests](https://requests.readthedocs.io/en/master/)       | Python >=3.6 - [‘2.26’, ‘2.25’];                             | `sw_requests`       |
| [sanic](https://sanic.readthedocs.io/en/latest)              | Python >=3.10 - NOT SUPPORTED YET; Python >=3.7 - [‘20.12’]; Python >=3.6 - [‘20.12’]; | `sw_sanic`          |
| [tornado](https://www.tornadoweb.org/)                       | Python >=3.6 - [‘6.0’, ‘6.1’];                               | `sw_tornado`        |
| [urllib3](https://urllib3.readthedocs.io/en/latest/)         | Python >=3.6 - [‘1.26’, ‘1.25’];                             | `sw_urllib3`        |
| [urllib_request](https://docs.python.org/3/library/urllib.request.html) | Python >=3.6 - ['*'];                                        | `sw_urllib_request` |

>?运行“celery-A…”的 celery 服务器需使用 HTTP 协议运行，因为默认情况下 celery 使用多处理，与当前 SkyWalking 中的 gRPC 协议实现不兼容。

