
腾讯物联网通信 REST API 为客户提供易于使用的 API（通过封装 HTTP 接口）。客户应用程序（例如，后台软件和 App 软件）可使用此 API 实现产品创建/删除、设备创建/删除、发布消息、影子数据操作等相关的功能。



## 目录说明

```
├── pythonlibs                     //使用前需要安装的依赖库
├── RestAPI                        //REST API 核心实现
│   ├── src                        //内部实现源文件
│   └── iotcloud.py                //接口文件
├── Demo.py                        //REST API 使用示例
```


## 操作步骤

>?部署 Python 2.7 版本，然后安装依赖库，依赖库见附件 pythonlibs（安装方法：python setup.py install，最后安装requests）。

1. 登录腾讯云访问管理控制台，选择【访问密钥】>【API 密钥管理】。
2. 进入API 密钥管理页面，单击【新建密钥】。
3. 新建成功后获取到 **SecretId** 和 **SecretKey**。
4. 以创建产品为例：
	```
	//初始化
	iotCloud = IoTCloud(region, secretId, secretkey)
	//创建产品
	response = self.iotCloud.create_product('ProductName')
	//打印结果
	{"productName":"ProductName","productID":"QZIAVH2HNS","message":"","codeDesc":"Success","code":0}
	```
5. 在 Demo.py 填写从官网获取的 SecretID 和用户从官网获取的 SecretKey，然后到根目录输入以下命令执行 Demo 代码。
	```
	python Demo.py
	```


## 接口说明
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


