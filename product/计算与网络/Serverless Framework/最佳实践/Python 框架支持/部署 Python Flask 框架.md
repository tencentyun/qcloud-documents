## 操作场景
腾讯云 [Flask](https://github.com/pallets/flask) Serverless Component，支持 Restful API 服务的部署，不支持 Flask Command。
>?任何支持 WSGI（Web Server Gateway Interface，即 Web 服务器网关接口）的 Python 服务端框架都可以通过该组件进行部署，例如 Falcon 框架等。

## 前提条件
在使用此组件之前，需要先初始化一个 Flask 项目，具体步骤如下：
#### Flask 安装与配置
您可以在全局或虚拟环境中完成 Flask 安装。
1. 创建项目目录：
```shell
$ mkdir myapp
$ cd myapp
```
2. 在项目目录中生成依赖文件 `requiements.txt`：
```shell
$ pip freeze > requirements.txt
```
3. 将 `Flask` 和 `werkzeug` 添加到依赖文件 `requiements.txt` 中：
```txt
Flask==1.0.2
werkzeug==0.16.0
```
4. 完成 Flask 安装：
```shell
$ pip install -r requirements.txt
```

#### 创建应用服务
新增 API 服务 `app.py`，以下代码仅供参考：
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
#### 安装
通过 npm 全局安装 [Serverless CLI](https://github.com/serverless/serverless)：

```shell
$ npm install -g serverless
```

#### 配置
本地创建 `serverless.yml` 文件：
```shell
$ touch serverless.yml
```

在`serverless.yml` 文件中进行如下配置：
```yml
# serverless.yml

MyComponent:
  component: "@serverless/tencent-flask"
  inputs:
    region: ap-guangzhou 
    functionName: flask-function
    code: ./
    functionConf:
      timeout: 10
      memorySize: 128
      environment:
        variables:
          TEST: vale
      vpcConfig:
        subnetId: ''
        vpcId: ''
    apigatewayConf:
      protocol: https
      environment: release
```

[查看详细配置文档 >>](https://github.com/serverless-components/tencent-flask/blob/master/docs/configure.md)

#### 部署
如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

通过 `sls` 命令进行部署，并添加 `--debug` 参数查看部署过程中的信息。
>?`sls` 是 `serverless` 命令的简写。

```shell
$ sls --debug

  DEBUG ─ Resolving the template's static variables.
  DEBUG ─ Collecting components from the template.
  DEBUG ─ Downloading any NPM components found in the template.
  DEBUG ─ Analyzing the template's components dependencies.
  DEBUG ─ Creating the template's components graph.
  DEBUG ─ Syncing template state.
  DEBUG ─ Executing the template's components graph.
  DEBUG ─ Generated requirements from /Users/Downloads/myapp/requirements.txt in /Users/Downloads/myapp/.serverless/requirements.txt...
  DEBUG ─ Installing requirements from /Users/Library/Caches/serverless-python-requirements/78f1b71bd84112bad004679c938bd8c63c80ddf8c468c5484e3de8214a52a8bc_slspyc/requirements.txt ...
  DEBUG ─ Using download cache directory /Users/Library/Caches/serverless-python-requirements/downloadCacheslspyc
  DEBUG ─ Running ...
  DEBUG ─ Compressing function flask-function file to /Users/Downloads/myapp/.serverless/flask-function.zip.
  DEBUG ─ Compressed function flask-function file successful
  DEBUG ─ Uploading service package to cos[sls-cloudfunction-ap-guangzhou-code]. sls-cloudfunction-default-flask-function-1581890739.zip
  DEBUG ─ Uploaded package successful /Users/Downloads/myapp/.serverless/flask-function.zip
  DEBUG ─ Creating function flask-function
  DEBUG ─ Created function flask-function successful
  DEBUG ─ Setting tags for function flask-function
  DEBUG ─ Creating trigger for function flask-function
  DEBUG ─ Deployed function flask-function successful
  DEBUG ─ Starting API-Gateway deployment with name MyComponent.TencentApiGateway in the ap-guangzhou region
  DEBUG ─ Service with ID service-rf5pzbfy created.
  DEBUG ─ API with id api-6i3uv432 created.
  DEBUG ─ Deploying service with id service-rf5pzbfy.
  DEBUG ─ Deployment successful for the api named MyComponent.TencentApiGateway in the ap-guangzhou region.

  MyComponent: 
    region:              ap-guangzhou
    functionName:        flask-function
    apiGatewayServiceId: service-rf5pzbfy
    url:                 http://service-rf5pzbfy-1258834142.gz.apigw.tencentcs.com/release/

  75s › MyComponent › done
```

#### 移除
通过以下命令移除部署的服务：
```shell
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing function
  DEBUG ─ Request id
  DEBUG ─ Removed function flask-function successful
  DEBUG ─ Removing any previously deployed API. api-6i3uv432
  DEBUG ─ Removing any previously deployed service. service-rf5pzbfy

  17s › MyComponent › done
```

#### 账号配置（可选）
当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件：
```shell
$ touch .env # 腾讯云的配置信息
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


