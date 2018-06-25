### 1. 获取云 API 密钥(SecretId、SecretKey)

登入 [控制台](https://console.cloud.tencent.com/iotcloud) 后，进入 [云API密钥](https://console.cloud.tencent.com/cam/capi)

![云API密钥](https://mc.qcloudimg.com/static/img/62352850496e6184f6a74f496f8d8638/miyao1.png)

在 **API 密钥管理**中 点击 **新建密钥**，新建成功后获取到 **SecretId** 和 **SecretKey**

![新建密钥](https://mc.qcloudimg.com/static/img/81d74a87132a2b8e92989bd4abd32278/miyao2.png)


### 2. 引入SDK

下载并解压 [Java RestAPI SDK](https://mc.qcloudimg.com/static/archive/3421d16447a99bebf042880b7fadc8e1/qcloud-restapi-java-release-1.0.0.zip), 将下列 JAR 包导入到应用代码工程中。

```
qcloud-restapi-java-release.jar
gson-2.6.2.jar
```

其中，gson-2.6.2.jar 包为第三方依赖包 。


例如：IntelliJ IDEA 工程中引入两个 JAR 包依赖。


第一步：将 JAR 放到代码工程中
![配置1](https://mc.qcloudimg.com/static/img/d7bc0f601398e989c759d553ab3f3d07/restapi-java-config-step1.png
)


第二步：配置依赖
![配置1](https://mc.qcloudimg.com/static/img/be64061452a5e2ce92d6534cef2aa281/restapi-java-config-step2.png)

 
### 3. 初始化

```
private static final String SECRET_ID  = "Your SecretID";    //用户从官网获取的SecretID
private static final String SECRET_KEY = "Your SecretKey";   //用户从官网获取的SecretKey

TXIotCloud iotCloud = new TXIotCloud(SECRET_ID, SECRET_KEY);  //创建实例
```
 

### 4. 发起调用
以创建产品为例：

```
//创建产品 
CreateProductResponse  response = iotCloud.createProduct(new CreateProductRequest("YourTestProduct", "by testing", "gz"));

//打印结果
System.out.println("response code:" + response.getCode());
System.out.println("response codeDesc:" + response.getCodeDesc());
System.out.println("response message:" + response.getMessage());
System.out.println("response productID:" + response.getProductID());
System.out.println("response productName:" + response.getProductName());
```



### 5. 接口说明
####  TXIoTCloud 接口及功能 （详见TXIotCloud.java代码注释）

| 序号  |         方法名         | 说明                          |
| ---- | --------------------- | ------------------------------|
| 1    | setConnectTimeout     | 设置HTTP连接超时时间             |
| 2    | setReadTimeout        | 设置HTTP读超时时间              |
| 3    | createProduct         | 创建产品                       |
| 4    | createDevice          | 创建设备                       |
| 5    | getDeviceShadow       | 获取设备影子信息                |
| 6    | listDevices           | 查询设备列表                    |
| 7    | listProducts          | 查询产品列表                    |
| 8    | updateDeviceShadow    | 更新设备影子信息                 |
| 9    | createMultiDevice     | 批量创建设备                    |
| 10   | deleteDevice          | 删除设备                        |
| 11   | deleteProduct         | 删除产品                        |
| 12   | getCreateMultiDevTask | 查询批量创建设备任务的执行状态      |
| 13   | getMultiDevices       | 查询批量创建设备的执行结果.        |
| 14   | publish               | 向指定的 TOPIC 发布消息          |

