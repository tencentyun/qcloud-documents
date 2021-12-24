## 现象描述

使用 HTTPS 协议访问自定义源站域名时报错。
<img src="https://main.qcloudimg.com/raw/210dc87de0dc28eac8460114c642daef.png" style="width: 50%"></img>

## 可能原因

证书配置错误或没有配置自定义源站域名。

## 处理步骤

### 使用 CDN 证书

1. 登录 [内容分发网络控制台](https://console.cloud.tencent.com/cdn)。
2. 在左侧导航栏中，选择**域名管理**，进入域名管理页面。
3. 单击需要配置的域名，选择 **HTTPS配置**页签，进入 HTTPS 配置页面。
4. 在“HTTPS配置”栏中，单击**前往配置**，进行证书配置。
详情请参考内容分发网络的 [证书配置](https://cloud.tencent.com/document/product/228/41687#.E8.AF.81.E4.B9.A6.E9.85.8D.E7.BD.AE) 文档。
5. 等待约5分钟，待 CDN 域名重新完成部署后，即可成功访问 HTTPS 协议。


### 使用 COS 证书 

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航栏中，选择**存储桶列表**，进入存储桶管理页面。
3. 找到需要操作的存储桶，单击该存储桶名称，进入存储桶配置页面。
4. 在左侧导航栏中，选择**域名与传输管理 > 自定义源站域名**，进入自定义源站域名页面。
![](https://main.qcloudimg.com/raw/6e4039c5d208f4e49bd1623102fc3198.png)
5. 选择需要操作的域名，单击**绑定证书**，进行证书配置。
>! 绑定证书功能正在逐步开放。目前仅支持北京、上海、成都和香港地域，且不支持泛域名证书绑定。
>
6. 单击**确定**，完成绑定。
![](https://main.qcloudimg.com/raw/c81fbfa5878fc57b5a29c8fb6eec6082.png)
当 “HTTPS 证书”为“已上传”时，即可成功访问 HTTPS 协议。

### 使用 CVM 反代理证书 

参考 [配置自定义域名支持 HTTPS 访问](https://cloud.tencent.com/document/product/436/11142)。


