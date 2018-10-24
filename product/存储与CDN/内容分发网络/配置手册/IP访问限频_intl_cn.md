CDN 为您提供了 IP 访问限频配置，通过对每一个 IP 在每一个节点每一秒钟访问次数进行限制，进行 CC 攻击的抵御。

## 配置说明
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/f2f50e0d81eb0a8c0dcb61d2ee37e6c9/manage.png)
单击【访问控制】，您可以看到 **IP 访问限频配置** 模块。
![](https://mc.qcloudimg.com/static/img/eb166fb8f636d737f488d13c89325bca/iplimit.png)

### 默认配置
默认情况下，IP 访问限频配置为关闭状态。

### 自定义配置
单击按钮打开 IP 访问限频，此时系统会根据您最近 30 天的单 IP 平均访问量给出一个建议阈值，您可以在下方 **当前单 IP 访问阈值** 看到给定的默认阈值。
![](https://mc.qcloudimg.com/static/img/1e84f30c3e9e9d151e297a21ac47c72b/iplimit-QPS.png)
默认阈值的算法为：计算区间为最近30天，每一天有288统计点（五分钟一个），每一个统计点计算单 IP 平均访问频次，取每天的最大值计算平均，为默认阈值。默认阈值最小为10 QPS，仅供参考，建议您根据业务波动合理设置阈值。

单击【编辑】按钮，可以设置单 IP 访问阈值。
> **注意**：
> IP 访问限频设置针对单 IP 单节点每秒访问次数进行了限制，若超出限制，则会直接返回 514。
> 设置较低频次限制可能会影响您的正常高频用户的使用，因此请合理设置阈值。

![](https://mc.qcloudimg.com/static/img/425dc2fa5e49750cbcb5b26824d3f167/iplimit-QPSset.png)