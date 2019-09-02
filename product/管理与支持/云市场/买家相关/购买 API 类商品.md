## 浏览商品
您可在 [腾讯云云市场](https://market.cloud.tencent.com/categories?dt=api) 选购 API 类商品。

## 选购商品
寻找到您所需要的商品后，选择您所需的商品规格以及使用期限，单击【立即购买】。
![](https://main.qcloudimg.com/raw/62914a44d876ae9ac23bd188268dbdd5.png)  

## 核对订单信息并支付 
核对订单信息，单击【确认购买】后进行支付。
![](https://main.qcloudimg.com/raw/df74eec9b5a30c62fbdede34fea6fe75.png)
![](https://main.qcloudimg.com/raw/a230689886bc3b8b7326bd5c437706d6.png)

## 确认支付结果             
支付成功后，您选购的 API 商品购买流程结束。            
- 单击【进入管理中心】可进入 [已购产品与服务](https://console.cloud.tencent.com/servicemarket/services) 页面，可查看资源实例相关信息。           
- 单击【查看我的订单】可进入 [我的订单](https://console.cloud.tencent.com/deal) 页面，可查看订单相关信息。
![](https://main.qcloudimg.com/raw/0f97f5601e5822c3bc3e3c1f2694463d.png)

## 使用资源实例
进入 [已购产品与服务](https://console.cloud.tencent.com/servicemarket/services) 页面，单击【管理】或资源实例 ID，即可获取 API 相关信息。
![](https://main.qcloudimg.com/raw/5d0db78f2803b8bdd57947f40b97fe00.png)   

>? 
- **secretId/secretKey：**secreId 用于标识所使用的哪个密钥，并参与签名计算，传输过程中体现。secretKey 用于签名计算，传递过程中无体现。如需了解详情，请参照 [secretId + secretKey 认证](https://cloud.tencent.com/document/product/628/11819)。  
- **总使用情况：**汇总累计您购买的可调用次数和已消耗的调用次数，例如，“0/100” 是指可调用次数为100，已消耗的调用次数为0。


## 调试 API
您可在商品详情页的 API 接口中单击【去调试】，输入相应参数即可调试。            
![](https://main.qcloudimg.com/raw/79abf713f4f92696df57c82f01e60a00.png)                 
若在调试页面中需输入 secretId 以及 secretKey，则可单击【获取 secretId 】进入 [已购产品与服务](https://console.cloud.tencent.com/servicemarket/services) 页面，复制该资源实例的 secretId 以及 secretKey 到 API 调试页面中即可调试。                 
![](https://main.qcloudimg.com/raw/22d05633849a6655bec92e7ddc22c51a.png)              
>!若商品参数为购买后调试，则需购买完成后才能进行调试，每次调试均会扣取次数包中的调用次数。

API 接口页面提供了 Python、curl、PHP、C#、go、Java、JavaScript 示例代码，您可通过搭建开发环境调用 API 接口进行调试。
