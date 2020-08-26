## 操作场景
REST API 模板使用 Tencent SCF 组件及其触发器能力，方便的在腾讯云创建，配置和管理一个 REST API 应用。您可以通过 Serverless SCF 组件快速构建一个 REST API 应用，实现 GET/PUT 操作。

## 操作步骤

### 1. 安装

安装 Serverless Framework：
```console
$ npm install -g serverless
```

### 2. 配置

通过如下命令直接下载示例：

```console
serverless create --template-url https://github.com/serverless/components/tree/v1/templates/tencent-python-rest-api
```
目录结构如下：
```
.
├── code
|   └── index.py
└── serverless.yml
```

目前 SCF 组件已支持 v2 版本，因此修改了 serverless.yml 文件，改为以下内容：

```yml
# serverless.yml 

component: scf 
name: apidemo 
org: test 
app: scfApp 
stage: dev 

inputs:
  name: myRestAPI
  enableRoleAuth: true
  src: ./code
  handler: index.main_handler
  runtime: Python3.6
  region: ap-guangzhou
  description: My Serverless Function
  memorySize: 128
  timeout: 20
  events:
      - apigw:
          name: serverless
          parameters:
            protocols:
              - http
            serviceName: serverless
            description: the serverless service
            environment: release
            endpoints:
              - path: /users/{user_type}/{action}
                method: GET
                description: Serverless REST API
                enableCORS: TRUE
                serviceTimeout: 10
                param:
                  - name: user_type
                    position: PATH
                    required: 'TRUE'
                    type: string
                    defaultValue: teacher
                    desc: mytest
                  - name: action
                    position: PATH
                    required: 'TRUE'
                    type: string
                    defaultValue: go
                    desc: mytest
```

查看 code/index.py 代码，可以看到接口的传参和返回逻辑：

```python
# -*- coding: utf8 -*-

def teacher_go():
    # todo: teacher_go action
    return {
        "result": "it is student_get action"
    }

def student_go():
    # todo: student_go action
    return {
        "result": "it is teacher_put action"
    }

def student_come():
    # todo: student_come action
    return {
        "result": "it is teacher_put action"
    }

def main_handler(event, context):
    print(str(event))
    if event["pathParameters"]["user_type"] == "teacher":
        if event["pathParameters"]["action"] == "go":
            return teacher_go()
    if event["pathParameters"]["user_type"] == "student":
        if event["pathParameters"]["action"] == "go":
            return student_go()
        if event["pathParameters"]["action"] == "come":
            return student_come()
```

### 3. 部署

通过`sls deploy`命令进行部署，并可以添加`--debug`参数查看部署过程中的信息。

如您的账号未 [登录](https://cloud.tencent.com/login) 或 [注册](https://cloud.tencent.com/register) 腾讯云，您可以直接通过**微信**扫描命令行中的二维码进行授权登录和注册。

```text
$ sls deploy

serverless ⚡ framework
Action: "deploy" - Stage: "dev" - App: "scfApp" - Instance: "myRestAPI"

FunctionName: myRestAPI
Description:  My Serverless Function
Namespace:    default
Runtime:      Python3.6
Handler:      index.main_handler
MemorySize:   128
Triggers: 
  apigw: 
    - http://service-jyl9i6mc-1258834142.gz.apigw.tencentcs.com/release/users/{user_type}/{action}

31s › myRestAPI › Success
```

### 4. 测试

通过以下命令测试 REST API 的返回情况：

>?如果 Windows 系统中未安装`curl`，也可以直接通过浏览器打开对应链接查看返回情况。

```console
$ curl -XGET http://service-9t28e0tg-1250000000.gz.apigw.tencentcs.com/release/users/teacher/go

{"result": "it is student_get action"}
```

```console
$ curl -PUT http://service-9t28e0tg-1250000000.gz.apigw.tencentcs.com/release/users/student/go

{"result": "it is teacher_put action"}
```

### 5. 移除

可以通过以下命令移除 REST API 应用：

```console
$ sls remove --debug

  DEBUG ─ Flushing template state and removing all components.
  DEBUG ─ Removing any previously deployed API. api-37gk3l8q
  DEBUG ─ Removing any previously deployed service. service-9t28e0tg
  DEBUG ─ Removing function
  DEBUG ─ Request id
  DEBUG ─ Removed function myRestAPI successful

  7s » myRestAPI » done
```

### 账号配置（可选）

当前默认支持 CLI 扫描二维码登录，如您希望配置持久的环境变量/密钥信息，也可以本地创建 `.env` 文件。

```console
$ touch .env # 腾讯云的配置信息
```

在 `.env` 文件中配置腾讯云的 SecretId 和 SecretKey 信息并保存。
```
# .env
TENCENT_SECRET_ID=123
TENCENT_SECRET_KEY=123
```
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取  SecretId 和 SecretKey。
