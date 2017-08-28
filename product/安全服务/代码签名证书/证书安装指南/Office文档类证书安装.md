### 1. 获取签名证书

购买并成功申请到代码签名证书后，可收到pem格式的签名证书。需将pem格式转换成pfx格式证书后，进行微软OFFICE文档签名。  
证书转换推荐使用在线证书格式转换工具（如：亚洲诚信在线格式转换工具https://www.trustasia.com/tools-cert-converter ）或者使用openssl工具进行本地证书转换。详见[什么是OpenSSl](https://www.qcloud.com/document/product/400/5707)

> 注：由于用户没有上传pem私钥，因此使用亚洲诚信在线格式转换工具时，“PEM私钥密码”不用填写。

### 2. 证书导入

将证书对文档进行签名之前，需要将证书导入到的操作系统当中。在此提供证书导入的两种方法：

#### 2.1 运行命令安装

点击“开始”—“运行”（如果没用“运行”选项，直接使用快捷键windows键+R打开运行命令窗口）。
![2.1.1](https://mc.qcloudimg.com/static/img/9fccde0606d4eb9db9ff0f52afe52d6a/image.png)

在“打开”中输入`certmgr.msc`。  
![2.1.2](https://mc.qcloudimg.com/static/img/0ce12c604fc7796a2dbadb4c66bba3bf/image.png)  

点击“确定”打开证书 MMC 管理单元。    
![2.1.3](https://mc.qcloudimg.com/static/img/678b8cf3f83722ca14cbe7685efeff8e/image.png)  

打开“个人”-“证书”，进入证书页面，右键点击“所有任务”-“导入” 。   
![2.1.4](https://mc.qcloudimg.com/static/img/9efaae8c2e0519cce47827aafb50e387/image.png)  

点击“下一步”，导入本地证书。   
![2.1.5](https://mc.qcloudimg.com/static/img/104aab6246e93fcff4e9b338b36344d2/image.png)   

输入密码。用户如果填写私钥密码，则填写私钥密码，否则填写密码文件中的密码  
![2.1.6](https://mc.qcloudimg.com/static/img/6d93a81ac84708bf99ae3e6057649e36/image.png)    

添加证书成功后，在证书页面会显示出添加的证书，如下图  
![2.1.7](https://mc.qcloudimg.com/static/img/8b2cbf852042857c88491ff73a31a8c7/image.png)    

### 3. 文档签名

打开文档：文件—信息—保护文档—添加数字签名。  
![2.1.8](https://mc.qcloudimg.com/static/img/0a046ab44e9ec5a263fab03d6fd5a245/image.png)    

添加签名后可根据需要添加承诺类型和签署目的。点击“更改”可选择签名的证书，选择完成后，点击“签名”。  
![2.1.9](https://mc.qcloudimg.com/static/img/e53e0dbebbaf847c8e57e15d081a446d/image.png)     

签名完成后，会弹出签名确认，表明Office文档已成功签名。  
![2.1.10](https://mc.qcloudimg.com/static/img/1a3b1df6efccaf4a8ef957e516ba231f/image.png)    

文档签名后，“查看签名”和“保护文档”已标黄，重新打开文档，会出现“标记为最终版本”与“签名”提示。    
![2.1.11](https://mc.qcloudimg.com/static/img/c4c57c3269972f3474d560c5ac223af6/image.png)    

![2.1.12](https://mc.qcloudimg.com/static/img/8e49db5a9287d4692748132121093e7c/12.png)    
