弹性公网 IP（EIP） 是您可以独立购买和持有，且在某个地域下固定不变的公网IP地址，能够为私有网络的单台云服务器提供与公网交互的能力。本章节介绍单台云服务器通过绑定 EIP 来访问公网的详细操作。

## 操作场景
您VPC中的一台云服务器在购买时未分配普通公网IP，不具备公网交互的能力，现因业务需要，需与公网通信。
为解决该场景的通信需求，您可以为云服务器绑定弹性公网EIP。
![](https://main.qcloudimg.com/raw/e4a8b87e8190044f0993ecef09c96911.png)



## 操作步骤
### 步骤一：申请EIP
1. 登录[私有网络控制台](https://console.cloud.tencent.com/vpc/)。
2. 单击“IP与网卡 > 公网IP“，进入公网IP界面。
3. 在“公网IP”页面顶部，选择与云服务器相同的地域，然后单击“申请”。
    ![](https://qcloudimg.tencent-cloud.cn/raw/1e3da3c2085526969fc81e77f2f48eb5.png)
4. 在弹出的“申请EIP”界面，按实际需要配置参数，并单击“确定”。更多参数说明可参考 [申请EIP](https://cloud.tencent.com/document/product/1199/42122#.E7.94.B3.E8.AF.B7-eip.3Ca-id.3D.22step1.22.3E.3C.2Fa.3E)。
  
    ![](https://qcloudimg.tencent-cloud.cn/raw/7eebd8c14b4120bf8c53436a429eff2b.png)

### 步骤二：为云服务器绑定EIP

1. 在公网IP界面，选择新建的EIP右侧的“更多 > 绑定”。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ecdc04565dbd758e20fe4b2d783ee7fe.png)
2. 在弹出的“绑定资源”窗口中，选择“CVM实例”，并勾选您的云服务器实例ID，然后单击“确定”。
   ![](https://qcloudimg.tencent-cloud.cn/raw/1ddaf94a016a77d3140e7e1d3f034456.png)
   

### 步骤三：验证通过EIP访问公网
1. 进入云服务器控制台，单击云服务器右侧的“登录”，输入密码等信息，进入云服务器界面。
    ![](https://qcloudimg.tencent-cloud.cn/raw/503687df4970559e0e72cfe50f3783fb.png)
2. 执行如执行`ping www.qq.com`测试数据连通性，可看到有数据返回，表示该 CVM 可以访问公网。
   ![](https://main.qcloudimg.com/raw/40c8b66f305baac0a63858394ed88766.png)
