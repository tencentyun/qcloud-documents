## 功能简介
EdgeOne SSL证书支持将已托管至SSL的证书批量部署至已接入EdgeOne的域名，适用于多域名或泛域名证书批量部署的场景，避免您多次重复繁琐的操作。如您需购买证书或上传自有证书请前往 [ SSL 证书控制台](https://console.cloud.tencent.com/ssl) 

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，进入到具体的站点且在左侧菜单栏中，单击**证书管理** > **SSL证书**。  

<img width="1397" alt="image" src="https://user-images.githubusercontent.com/114125357/208017897-dd491e5f-d1e6-4b2f-9aa6-77921e04c1d5.png">  
EdgeOne SSL列表页仅展示当前站点及子域名关联的证书，未关联当前站点及子域名关联的证书请前往 [ SSL 证书控制台](https://console.cloud.tencent.com/ssl)   
注意：如您申请证书类型为免费证书，其免费证书信息不会显示在EdgeOne SSL列表页，如需查看免费证书信息请单击**域名管理**，鼠标停留在<img width="24" alt="image" src="https://user-images.githubusercontent.com/114125357/208018433-1af4bdcc-b97e-4552-95c4-f44b65ac6ca7.png">上，免费证书信息显示如下所示：
<img width="289" alt="image" src="https://user-images.githubusercontent.com/114125357/208018574-fcf26c34-74f8-4f4a-a09e-153e1779e163.png">   







2. 在边缘节点证书页面，选择所需站点，单击**配置证书**。
![](https://qcloudimg.tencent-cloud.cn/raw/0539eeb1243d49c944b5e4be62a7e576.png)
3. 在配置证书页面，选中需绑定证书的域名，则证书列表自动展示  [SSL 证书控制台](https://console.cloud.tencent.com/ssl) 中该域名可关联的证书。
![](https://qcloudimg.tencent-cloud.cn/raw/52cf7d848064e44aaeae091866aa4541.png)
4. 如果暂无可关联的证书，您可以单击**上传自定义证书**上传该域名的证书。
![](https://qcloudimg.tencent-cloud.cn/raw/5b928e60ae9f074ec9fd2a564130f8d6.png)
5. 选择要关联的证书，单击**确定**，证书将自动部署到 EdgeOne 加速节点。
>?如果域名已关联过证书，重新关联将会覆盖旧的证书。

