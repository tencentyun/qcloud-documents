
目前腾讯云提供的硬件MFA设备为“腾讯云安全令牌”，也叫动态口令卡或token卡，首批token卡采用内测的形式发放给客户，照片如图所示（不同版本可能在外观上有差异）


![](https://mc.qcloudimg.com/static/img/e5fd0f764b6a40626557beb032a4d6b2/image.png)

### 1.绑定MFA设备

主要有以下几个步骤：

1）进入用户中心-->账户信息-->安全设置 点击“绑定”按钮

![](https://mc.qcloudimg.com/static/img/b0c34237e3eb039c08b8694693ef4f62/image.png)

2）弹出身份验证框，输入手机中收到的6位数验证码，点击“确定”按钮

![](https://mc.qcloudimg.com/static/img/4e7970d5974b2eb9ee58ea00464082f8/image.png)

3）绑定MFA设备页中选择“硬件MFA设备”，根据提示输入token卡背面的序列码（SN码），和token卡正面的6位数动态安全码

    启用范围可勾选也可以不勾选：
    - 不勾选则默认您的账户不开启安全保护；
    - 勾选登陆保护则登陆后需要验证token卡上的安全码；
    - 勾选操作保护则在账户中进行删除云主机，修改安全资料，查看云api密钥等敏感操作前需要验证token卡上的安全码;

![](https://mc.qcloudimg.com/static/img/ec0977f94c498f7d9b6e5f6ff301ba44/image.png)

信息输入无误后，点击确认则绑定完成，绑定成功，并开启登录保护和操作保护的状态如下图所示：

![](https://mc.qcloudimg.com/static/img/987b808159aef64c0cfdb14be3a4669c/image.png)




