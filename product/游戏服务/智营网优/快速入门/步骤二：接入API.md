## 1 API 概览

| 接口功能 | Action Name | 功能描述 |
|---------|---------|---------|
| 获取运营商接口URL | [geturl](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E8%8E%B7%E5%8F%96%E8%BF%90%E8%90%A5%E5%95%86%E6%8E%A5%E5%8F%A3URL.md) |调用接口得到一个URL字符串，通过访问该URL可以获得该手机用户在运营商数据库的唯一标示|
| 启用 4G 加速 | [open](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E5%BC%80%E9%80%9A%204G%20%E5%8A%A0%E9%80%9F%E6%9C%8D%E5%8A%A1.md) |启用 4G 网络加速服务功能，加速服务 1 小时后自动关闭|
| 停用 4G 加速 | [close](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E5%85%B3%E9%97%AD%204G%20%E5%8A%A0%E9%80%9F%E6%9C%8D%E5%8A%A1.md) | 停用 4G 加速服务后，加速效果将失效| 


## 2. 相关术语
终端用户：即手机用户
开发商：游戏产品开发商
运营商：指移动、联通和电信
运营商接口URL：运营商提供给终端用户查询该终端用户在运营商数据库的唯一标示号码（加密后的号码字符串）
签名信息：开发商按照腾讯云提供的算法，生成签名信息，用于腾讯云对用户进行鉴权


## 3. 调用示例

### 启用4G加速服务
主要步骤如下：  
1）[生成签名信息](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E7%94%9F%E6%88%90%E7%AD%BE%E5%90%8D%E4%BF%A1%E6%81%AF.md)  
2）[获取运营商（电信、移动和联通）接口地址URL](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E8%8E%B7%E5%8F%96%E8%BF%90%E8%90%A5%E5%95%86%E6%8E%A5%E5%8F%A3URL.md)  
3）[获取手机用户唯一标示值](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E8%8E%B7%E5%8F%96%E6%89%8B%E6%9C%BA%E7%94%A8%E6%88%B7%E5%94%AF%E4%B8%80%E6%A0%87%E7%A4%BA%E5%80%BC.md)  
4）[开通4G加速服务](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E5%BC%80%E9%80%9A%204G%20%E5%8A%A0%E9%80%9F%E6%9C%8D%E5%8A%A1.md)  


### 停用4G加速服务
主要步骤如下：  
1）[生成签名信息](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E7%94%9F%E6%88%90%E7%AD%BE%E5%90%8D%E4%BF%A1%E6%81%AF.md)  
2）[获取运营商（电信、移动和联通）接口地址URL](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E8%8E%B7%E5%8F%96%E8%BF%90%E8%90%A5%E5%95%86%E6%8E%A5%E5%8F%A3URL.md)  
3）[获取手机用户唯一标示值](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E8%8E%B7%E5%8F%96%E6%89%8B%E6%9C%BA%E7%94%A8%E6%88%B7%E5%94%AF%E4%B8%80%E6%A0%87%E7%A4%BA%E5%80%BC.md)   
4）[关闭4G加速服务](https://github.com/hymanwangsz/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/%E6%99%BA%E8%90%A5%E7%BD%91%E4%BC%98/API/%E5%85%B3%E9%97%AD%204G%20%E5%8A%A0%E9%80%9F%E6%9C%8D%E5%8A%A1.md)  


