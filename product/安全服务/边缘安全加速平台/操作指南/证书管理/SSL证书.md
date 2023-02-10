## 功能简介
EdgeOne SSL 证书支持将已托管至 SSL 的证书批量部署至已接入 EdgeOne 的域名，适用于多域名或泛域名证书批量部署的场景，避免您多次重复繁琐的操作。如您需购买证书或上传自有证书请前往 [ SSL 证书控制台](https://console.cloud.tencent.com/ssl)。 

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，进入到具体的站点且在左侧菜单栏中，单击**证书管理** > **SSL 证书**。  
![](https://qcloudimg.tencent-cloud.cn/raw/658e2eacbda25dcb74e6fed812ca4d31.png)
>!
>- EdgeOne SSL 列表仅展示当前站点及子域名关联的证书，未关联当前站点及子域名的证书请前往 [SSL 证书控制台](https://console.cloud.tencent.com/ssl)。
>- 如您申请证书类型为免费证书，其免费证书信息不会显示在 EdgeOne SSL 列表，如需查看免费证书信息请单击**域名管理**，鼠标停留在<img width="24" alt="image" src="https://user-images.githubusercontent.com/114125357/208018433-1af4bdcc-b97e-4552-95c4-f44b65ac6ca7.png">上，免费证书信息显示如下所示：  
<img width="289" alt="image" src="https://user-images.githubusercontent.com/114125357/208018574-fcf26c34-74f8-4f4a-a09e-153e1779e163.png">   
2. 在 EdgeOne SSL 列表，单击**部署**，选择域名，支持批量选择多个域名，单击**确定**即可完成部署。  
![](https://qcloudimg.tencent-cloud.cn/raw/fe9f202bf1131028fbcda4b8867054b7.png)
>!证书单次部署最多支持选择100个域名，如您的域名个数超过100个请分批操作。  
>
如果证书绑定的域名未接入 EdgeOne 则会提示如下图所示：   
![](https://qcloudimg.tencent-cloud.cn/raw/4d5d15545cee5d5a2b557fd8dacf73fa.png)
3. 已完成证书部署的域名信息查看在 EdgeOne SSL 列表页单击<img src="https://qcloudimg.tencent-cloud.cn/raw/44d307b79b31749005e6f442fd0b3b2b.png" width=24px>后，如下图所示：  
![](https://qcloudimg.tencent-cloud.cn/raw/40c2abadd92aeddb9c058a2ad194c05e.png)
>?其中数字1代表的是证书已部署至 EdgeOne 域名的个数。
>
