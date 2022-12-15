## Web/App 票据校验（DescribeCaptchaResult 接口）
接口返回不同的 CaptchaCode 处理建议如下：

1. 普通验证模式下：CaptchaCode 为1属于验证通过，CaptchaCode非1的情况需进行拦截。
2. 无感验证模式下：除了对 CaptchaCode 进行判断，还需要判断 EvilLevel 参数。如果 EvilLevel = 100，属于验证码判断出来验证中有恶意，需要进行拦截。
3. 建议业务针对 CaptchaCode 非1的情况进行日志监控，当 CaptchaCode 非1日志量突增时，及时进行分析处理：
   - CaptchaCod e= 100：大概率由于接入不合法导致，可检查最近是否有相关变更导致传入的验证码参数不合法。
   - CaptchaCode = 7/8/9/15：大概率由于黑产非法调用导致，一般突增一段时间会下降，及时观察即可。
   - CaptchaCode = 16：
     - 若 Ticket 不包含 terror 前缀：大概率由于接入不合法导致，可检查最近是否有相关变更导致传入的验证码参数不合法。
     - 若 Ticket 包含 terror 前缀时：一般是由于用户网络较差导致前端产生的容灾票据所致，可观察是否属于偶发。
   - CaptchaCode = 21：
     - 若 Ticket 不包含 terror 前缀：大概率由于黑产非法调用导致验证码进行策略拦截，一般突增一段时间会下降。
     - 当 Ticket 包含 terror 前缀：一般是由于用户网络较差导致前端产生的容灾票据，可观察是否属于偶发。
4. 如果发现数据持续异常，可登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击**快速咨询**联系我们。


>!1. 标准的容灾 ticket 格式为：
 ```.js
 terror_{前端错误码，比如1006}_{CaptchaAppId}_{时间戳}
 ```
标准容灾 ticket 票据校验时，验证码返回 code = 21，其他 terror 开头的票据校验若识别不出 CaptchaAppId 时，将返回 code = 16。
2. 容灾 ticket 来源包括：
 - 验证码自身为了在用户网络异常、系统异常情况下，保障业务正常运行而产生的 ticket。
 - 业务接入验证码时，自定义的js加载错误处理函数生成的 ticket。


## 微信小程序票据校验（DescribeCaptchaMiniResult 接口）

接口返回不同的 CaptchaCode 处理建议如下：

1. CaptchaCode 为1属于验证通过，CaptchaCode 非1的情况需进行拦截。
2. 建议业务针对 CaptchaCode 非1的情况进行日志监控，当 CaptchaCode 非1日志量突增时，及时进行分析处理：
   - CaptchaCode = 7/100：大概率由于接入不合法导致，可检查最近是否有相关变更导致传入的验证码参数不合法。
   - CaptchaCode = 8/10/15/16/21/25，大概率由于黑产非法调用导致，一般突增一段时间会下降，及时观察即可。
   - CaptchaCode = 31：验证码已停服导致接口没有调用权限。主要由于您账号购买的套餐包已失效且没有开通后付费，或者已开通后付费情况下账户欠费。请及时购买套餐包或续费账户（续费后注意登录验证码控制台重新开通后付费）。
   - CaptchaCode = 26：验证码系统发生内部错误。可登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击**快速咨询**联系我们。
3. 如果发现数据持续异常，可登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击**快速咨询**联系我们。

## 常见问题

详情参见 [接入相关问题](https://cloud.tencent.com/document/product/1110/36828)。

## 更多信息

您可以登录 [验证码控制台](https://console.cloud.tencent.com/captcha/graphical) ，在页面右上角单击**快速咨询**，了解更多详细信息。
