# 腾讯物联网通信 REST API
腾讯物联网通信 REST API 为客户提供易于使用的 API（通过封装HTTP接口）。客户应用程序（如：后台软件和APP软件）可使用此 API 实现产品创建/删除、设备创建/删除、发布消息、影子数据操作等相关的功能。



## 1. 目录说明

```
├── pythonlibs                     //使用前需要安装的依赖库
├── RestAPI                        //REST API 核心实现
│   ├── src                        //内部实现源文件
│   └── iotcloud.py                //接口文件
├── Demo.py                        //REST API 使用示例
```


## 2. 如何使用

### 2.1
部署Python 2.7版本，然后安装依赖库，依赖库见附件pythonlibs(安装方法:python setup.py install，最后安装requests)

### 2.2 获取云 API 密钥(SecretId、SecretKey)
登入 [控制台](https://console.cloud.tencent.com/iotcloud) 后，进入 [云API密钥](https://console.cloud.tencent.com/cam/capi)

![云API密钥](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/d7cbde91-5723-47f9-8c56-d0381bb3eb1b.png)

在 **API 密钥管理**中 点击 **新建密钥**，新建成功后获取到 **SecretId** 和 **SecretKey**

![新建密钥](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/ba3f3f9d-db13-45c4-bad6-e5c236ebcbba.png)

### 2.3 使用方法
以创建产品为例：

```
//初始化
iotCloud = IoTCloud(region, secretId, secretkey)

//创建产品
response = self.iotCloud.create_product('ProductName')

//打印结果
{"productName":"ProductName","productID":"QZIAVH2HNS","message":"","codeDesc":"Success","code":0}
```

### 2.4 运行

在 Demo.py 填写从官网获取的 SecretID 和用户从官网获取的 SecretKey，然后到根目录输入以下命令执行Demo代码
```
python Demo.py
```


## 3. 接口说明
####  iotcloud 接口及功能

| 序号 | 方法名                   | 说明                           |
| ---- | ------------------------ | ------------------------------ |
| 1    | set_region               | 设置区域参数                   |
| 2    | set_security_credential  | 设置安全凭证                   |
| 3    | create_product           | 创建产品                       |
| 4    | delete_product           | 删除产品                       |
| 5    | list_products            | 查询产品列表                   |
| 6    | create_device            | 创建设备                       |
| 7    | delete_device            | 删除设备                       |
| 8    | get_device_shadow        | 获取虚拟设备信息               |
| 9    | update_device_shadow     | 更新虚拟设备信息               |
| 10   | list_devices             | 查询设备列表                   |
| 11   | create_multi_devices     | 批量创建设备                   |
| 12   | get_create_multi_devtask | 查询批量创建设备任务的执行状态 |
| 13   | get_multi_devices        | 查询批量创建设备的执行结果     |
| 14   | publish                  | 向某个主题发布消息             |

