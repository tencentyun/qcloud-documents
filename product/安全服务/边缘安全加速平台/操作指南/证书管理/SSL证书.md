## 功能简介
EdgeOne SSL证书支持将已托管至SSL的证书批量部署至已接入EdgeOne的域名，适用于多域名或泛域名证书批量部署的场景，避免您多次重复繁琐的操作。如您需购买证书或上传自有证书请前往 [ SSL 证书控制台](https://console.cloud.tencent.com/ssl) 

## 操作步骤
1. 登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone)，进入到具体的站点且在左侧菜单栏中，单击**证书管理** > **SSL证书**。  

<img width="1397" alt="image" src="https://user-images.githubusercontent.com/114125357/208017897-dd491e5f-d1e6-4b2f-9aa6-77921e04c1d5.png">   

EdgeOne SSL列表页仅展示当前站点及子域名关联的证书，未关联当前站点及子域名关联的证书请前往 [ SSL 证书控制台](https://console.cloud.tencent.com/ssl)   
注意：如您申请证书类型为免费证书，其免费证书信息不会显示在EdgeOne SSL列表页，如需查看免费证书信息请单击**域名管理**，鼠标停留在<img width="24" alt="image" src="https://user-images.githubusercontent.com/114125357/208018433-1af4bdcc-b97e-4552-95c4-f44b65ac6ca7.png">上，免费证书信息显示如下所示：  
<img width="289" alt="image" src="https://user-images.githubusercontent.com/114125357/208018574-fcf26c34-74f8-4f4a-a09e-153e1779e163.png">   


2. 在EdgeOne SSL列表页单击**部署**后如下图所示：  

<img width="1391" alt="image" src="https://user-images.githubusercontent.com/114125357/208019228-78f908fe-0546-41f7-bfd8-2da4be6cb531.png">    

支持批量选择多个域名单击**确定**即可完成部署。
注意：证书单次部署最多支持选择100个域名，如您的域名个数超过100个请分批操作。

3. 已完成证书部署的域名信息查询在EdgeOne SSL列表页单击<img width="44" alt="image" src="https://user-images.githubusercontent.com/114125357/208019571-31161009-1b80-43db-96c0-6e019d1b21d0.png">后如下图所示：  
<img width="256" alt="image" src="https://user-images.githubusercontent.com/114125357/208019616-2b90f08b-025e-4383-96b6-433972c27ddc.png">  
其中数字”1“代表的是证书已部署至EdgeOne域名的个数。








