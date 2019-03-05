SSL证书支持部署到负载均衡，步骤如下所示：

### 1. 选择证书
首先成功申请获取证书（参考[如何免费申请域名型证书](https://cloud.tencent.com/document/product/400/6814)），或者选择上传的证书，展开【更多】操作，选择【部署到负载均衡】。
![](https://mc.qcloudimg.com/static/img/f63593c744fe88e386ce1157526b468f/1.png)

### 2. 选择LB实例
根据项目和地区筛选LB实例（目前不支持华南地区-深圳金融），且只能选择一个实例。
![](https://mc.qcloudimg.com/static/img/b6261451a354dac96679737014938e52/2.png)

### 3. 创建监听器
跳转到负载均衡控制台，打开创建监听器弹窗，并且监听协议端口已切换到Https，服务器证书为已选中的证书，然后完成剩余的基本配置。
![](https://mc.qcloudimg.com/static/img/e997310524fd15288fca7c91ae7a2e6c/3.png)

### 4. 继续完成配置
继续完成创建监听器的其他配置，即可实现负载均衡的Https。
