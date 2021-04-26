
## SDK 获取
智能图像的 Java SDK 下载地址：[Java-SDK-V2.0](https://github.com/tencentyun/image-java-sdk-v2.0)。

## 使用前准备
1. 前往注册： [腾讯云账号注册](https://cloud.tencent.com/register) （详细指引见 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985)）。
2. 取得 **APPID**、**SecretId**、**SecretKey**：请前往 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) ，单击【新建密钥】（目前只支持主账号及密钥进行调用）。

## 集成方式
### 获得 SDK jar 文件
您可以通过以下两种方式获得文件：
- 直接使用` release/*-with-dependencies.jar`
- 自行编译：在工程根目录下执行命令`mvn assembly:assembly`，编译结果见 target/*-with-dependencies.jar

### 导入 jar 到项目中
根据项目具体情况导入 *-with-dependencies.jar

## 使用简介
### 初始化

```Java
ImageClient imageClient = new ImageClient(APPID, SecretId, SecretKey);
```

### 设置代理
根据实际网络环境设置代理，例如：

```Java
Proxy proxy = new Proxy(Type.HTTP, new InetSocketAddress("127.0.0.1", 8080));
imageClient.setProxy(proxy);
```

### 使用
SDK 提供功能如下：

**图像识别**：鉴黄、标签  

**文字识别（OCR）**：身份证、名片、通用、驾驶证行驶证、营业执照、银行卡、车牌号  

```Java
// 调用车牌识别 API 示例
String imageUrl = "http://youtu.qq.com/app/img/experience/char_general/icon_ocr_license_3.jpg";
String result = imageClient.ocrPlate(new OcrPlateRequest("bucketName", imageUrl));
System.out.println(result);
```

更多例子详情可参见 [Demo.java](https://github.com/tencentyun/image-java-sdk-v2.0/blob/master/src/main/java/com/qcloud/image/demo/Demo.java) 的代码。


##  Demo 工程
1. 修改文件 src/main/java/com/qcloud/image/demo/Demo.java 的 main() 方法，填入上述申请到的**APPID**、**SecretId**、**SecretKey**

2. 导入到 IDE：这个 Demo 工程是用 Maven 构建的，以 Intellij IDEA 为例，导入方式为：Import Project > 选择工程目录 > Import project from external model > Maven
3. 运行：Demo.java 右键，Run Demo.main()
