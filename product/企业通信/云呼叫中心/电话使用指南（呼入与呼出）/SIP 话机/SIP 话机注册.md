腾讯云云呼叫中心允许客户将购买的 SIP 固话话机与云呼叫中心上的座席打通，从而让座席通过固话话机进行通话。主要功能包括：

- 管理员对 SIP 话机进行状态管理，包括注册、重置密码。
- 每个座席的 SIP 话机分别有专属分机号。
- 话机可绑定座席作为座席的专属话机，每个员工无需登录云呼叫中心即可使用话机办公，使用话机进行内部通话、外呼、呼入来电接听等场景。
- 话机可加入技能组，用户电话呼入时，系统可按照预先设置的规则将该技能组来电分配至合适的话机。

## 注册话机说明
1. 登录 [腾讯云呼叫中心 TCCC 管理工作台](https://cloud.tencent.com/document/product/679/73497#logintccc)。
2. 左侧导航栏单击**电话客服>话机管理**进入来电弹屏页面，左上角单击**注册话机**。
![](https://qcloudimg.tencent-cloud.cn/raw/5bc6e796856c953bcbc91f93936f6054.png)
3. 为话机设置一个**1到8开头，4到6位数字的分机号**，并设置话机的名称。
![](https://qcloudimg.tencent-cloud.cn/raw/961b00ebe6f71c0cb83746d52cc88799.png)
4. 将分机注册信息配置到您的 SIP 话机上。
<img src="https://qcloudimg.tencent-cloud.cn/raw/b1517a0340f2b6c40c0a8f71fa53859e.png" style="width:400px"> 
5. 在浏览器内输入话机的**IPv4地址**进入话机管理页面，请根据您的 SIP 话机类型，按照以下对应的操作指引，配置您的话机。
<img src="https://qcloudimg.tencent-cloud.cn/raw/3524ac2b199add643993313193d735ae.png" style="width:400px"> 


<dx-tabs>
::: 亿联（yealink）
标签、显示名、注册名、用户名处填写：话机分机号
密码处填写：话机密码
服务器主地址处填写：域名
传输选择：TLS
Outbound 代理服务器处填写：服务器地址
![](https://qcloudimg.tencent-cloud.cn/raw/dd75e420ca019f5cb1302c44c00fe6dc.png)
:::
::: 科尔特（CallTel）
用户名、电话号码、显示名字、代理服务器账号处填写：话机分机号
密码、代理服务器密码处填写：话机密码
服务器地址、服务器端口、本地域名处填写：域名
代理服务器地址、代理服务器端口、备份代理服务器地址、备份代理服务器端口处填写：服务器地址
![](https://qcloudimg.tencent-cloud.cn/raw/266275c8fec9dc2a8b7e99bbb75923fe.png)
SIP 高级设置里，传输协议选择 TLS：
![](https://qcloudimg.tencent-cloud.cn/raw/e3a3e1a1e4632ad958852634b7006654.png)
:::
::: 飞音
显示名称、注册账户、认证名称填写：话机分机号
密码、代理服务器密码处填写：话机密码
![](https://qcloudimg.tencent-cloud.cn/raw/19289f57a264b818dc8d574fef79c2a1.png)
:::
::: 阿尔卡特 朗讯
标签、显示名称、用户名、注册名称处填写：话机分机号
密码处填写：话机密码
服务器地址、服务器端口处填写：域名
传输方式选择：TLS
代理服务器地址、代理服务器端口填写：服务器地址
![](https://qcloudimg.tencent-cloud.cn/raw/e0a2c8e89d8d129bc269ef877a866ae9.png)
:::
</dx-tabs>
