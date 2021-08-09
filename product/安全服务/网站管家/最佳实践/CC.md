## 应用场景
针对短时间内大流量 CC 攻击，配置有效策略拦截 CC攻击，保障用户业务的数据和信息安全。

## 示例1：地域封禁配置
针对业务具体流量来源，通过封禁某些地区来阻止攻击回源到源站，如某域名没有海外流量，那么可以封禁海外地区的流量。
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航栏，选择【Web 安全防护】>【防护设置】>【基础设置】，进入基础设置页面。
2.  在基础设置页面，左上角处找到需要防护的域名。
![](https://main.qcloudimg.com/raw/08d7a28d7b3adb1f6fb29c9cdac34b4c.png)
3. 在地域封禁模块，单击【选择】，选定封禁地区后，单击【确定】。
![](https://main.qcloudimg.com/raw/d4da8f2378d8fba1c2bb307b021fe773.png)
4. 在地域封禁模块，单击![](https://main.qcloudimg.com/raw/019a8a5d31f9e10e90e0a701779729e2.png)图标开启封禁状态开关，使地域封禁配置生效。
![](https://main.qcloudimg.com/raw/4189eba4d4176bb28127c0ecc5abc7f5.png)

## 示例2： 自定义策略设置
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航栏，选择【Web 安全防护】>【防护设置】>【自定义策略】，进入自定义策略页面，可根据具体的 CC 攻击请求配置策略。
2. 在自定义策略页面，左上角处找到需要防护的域名。
![](https://main.qcloudimg.com/raw/fd91fc24b776ec2e7e200f8672068bea.png)
2. 在自定义策略页面，单击【添加规则】，可通过查看访问日志记录，统计最近访问量突增时间范围Top10 url、源ip、user-agent、cookie、headers、ip归属等。
![](https://main.qcloudimg.com/raw/2e927e9143ddb9d9760b06fcf171cacb.png)

### 例子A
在添加规则弹窗中，通过访问日志统计到某些 ua 占比异常，如某些 ua 请求占比特别大、ua 不存在或者为空等，可以通过根据正常业务请求是否拦截这些 ua。
![](https://main.qcloudimg.com/raw/4c680bbf16665be4162296535046227c.png)
![](https://main.qcloudimg.com/raw/eb2cbab1e4dcd7f51adf1defcea22257.png)
![](https://main.qcloudimg.com/raw/761157bdcaa6e46ad2b9e01187e62287.png)

### 例子B
如果统计访问日志没有发现异常的 ua，可通过其他维度来设置，如业务上某些接口需要验证或者自定义的 token 才可以访问。
![](https://main.qcloudimg.com/raw/e15e67bc66cda65080ba288ebdcbb8ab.png)

### 例子C
统计访问日志查询到某些 ip 访问量异常、url 分散或者集中,可通过 IP 黑白名单、 CC 策略或 BOT 策略来拦截异常请求。
![](https://main.qcloudimg.com/raw/50a86a4d978bf4c697694c4a32f6293a.png)


## 示例3： CC 防护设置
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/waf/overview)，在左侧导航栏，选择【Web 安全防护】>【防护设置】>【CC 防护设置】，进入CC 防护设置页面。
2. 在 CC 防护设置页，左上角处找到需要防护的域名。
![](https://main.qcloudimg.com/raw/5031a29c31447265f3def435a4a2af7a.png)
3. 在 CC 防护设置页，单击【添加 CC防护设置】，根据源 ip 做频率限制，当 ip 在一定时间内的请求次数超过设定的阈值就会执行相关动作，动作类型说明请参考 [CC 防护设置](https://cloud.tencent.com/document/product/627/11709)。
![](https://main.qcloudimg.com/raw/de2de951d5cbf449aaccba6d04f6b55d.png)
4. 在 CC 防护设置页， IP 识别方式在办公网、商超和公共 WIFI 场合，用户因使用相同 IP 出口存在误拦截问题，通过配置SESSION 维度的 CC 策略则不存在此问题。
![](https://main.qcloudimg.com/raw/291efbcb9888dfffcc9db8fa6b3c6e00.png)
5.如果用户不清楚 url 的访问量异常可以配置根目录的策略，此规则针对全站生效，请跟进正常业务设置访问频次，否则误拦截率较大。
![](https://main.qcloudimg.com/raw/a50fcd1044fb741d3c7eea63c20d3a77.png)


## 示例4：BOT 防护设置
如果配置了上面的策略，还是有部分攻击流量到达后端，业务侧也不好去调整策略以免产生误拦截，那么可以采用以下 BOT 功能:
- 访问的url集中，但是携带参数很少一样。
- 访问的url分散，但是携带参数重复比较高。
![](https://main.qcloudimg.com/raw/f97fccacb5c25db3f9235f9327199762.png)
