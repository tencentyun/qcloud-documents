
## 操作场景
腾讯云 [Flask](https://github.com/pallets/flask) Serverless Component，支持 Restful API 服务的部署，不支持 Flask Command。
>!任何支持 WSGI（Web Server Gateway Interface，即 Web 服务器网关接口）的 Python 服务端框架都可以通过该组件进行部署，例如 Falcon 框架等。

## 前提条件
1.在使用此组件之前，请确认您本地已安装好 Python 环境。
2.先初始化一个 Flask 项目，然后将 `Flask` 和 `werkzeug` 添加到依赖文件 `requirements.txt` 中，如下： 
```txt
Flask==1.0.2
werkzeug==0.16.0
```
 同时新增 API 服务 `app.py`，下面代码仅供参考：
```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Flask"

@app.route("/users")
def users():
    users = [{'name': 'test1'}, {'name': 'test2'}]
    return jsonify(data=users)

@app.route("/users/<id>")
def user(id):
    return jsonify(data={'name': 'test1'})
```

## 操作步骤
### 安装
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：

```shell
npm install -g serverless
```

### 配置
在项目根目录下创建 `serverless.yml` 文件：
```shell
touch serverless.yml
```

在 `serverless.yml` 中进行如下配置：

```yml
# serverless.yml

component: flask
name: flashDemo
org: orgDemo
app: appDemo
stage: dev

inputs:
  src:
    hook: 'pip install -r requirements.txt -t ./'
    dist: ./
    exclude:
      - .env
  region: ap-guangzhou
  runtime: Python3.6
  apigatewayConf:
    protocols:
      - http
      - https
    environment: release
```

[查看详细配置文档 >>]( https://github.com/serverless-components/tencent-flask/blob/master/docs/configure.md )

### 部署

执行以下命令进行扫码授权部署：

```console
sls deploy
```

>?微信扫码授权部署有过期时间，如果想要持久授权，请参考 [账号配置](#account)。

### 移除

执行以下命令移除部署的服务：

```console
sls remove
```

<span id="account"></span>
### 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：

```shell
touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存：

```text
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```

>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 SecretId 和 SecretKey。

