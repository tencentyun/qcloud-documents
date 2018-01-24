> CDN 为您提供了 IP 访问限频配置，通过对源一个 IP 在每一个节点每一秒钟访问次数进行限制，进行 CC 攻击的抵御。配置开启后，超出QPS限制的请求会直接返回 514，设置较低频次限制可能会影响您的正常高频用户的使用，请根据业务情况、使用场景合理设置阈值。

## 配置指引

### 配置查看

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，选择左侧菜单栏的【域名管理】，单击您所要编辑的域名右侧的【管理】。
![](https://mc.qcloudimg.com/static/img/1f2cb594cd614b62b589cb20a20ed362/basic-config-1.png)
单击【访问控制】，您可以看到 **IP 访问限频配置** 模块：
![](https://mc.qcloudimg.com/static/img/b5a89c0c1f2913015a1f129918414f70/ipf-config-1.png)默认情况下，IP 访问限频配置为关闭状态。

### 修改限频配置

单击按钮打开 IP 访问限频，此时系统会根据您最近 30 天的单 IP 平均访问量给出一个建议阈值，您可以在下方 **当前单 IP 访问阈值** 看到给定的默认阈值。
![](https://mc.qcloudimg.com/static/img/145c8df5ad44613ed532c75b0216b723/ipf-config-2.png)默认阈值的算法为：计算区间为最近30天，每一天有288统计点（五分钟一个），每一个统计点计算单 IP 平均访问频次，取每天的最大值计算平均，为默认阈值。默认阈值最小为10 QPS，仅供参考，建议您根据业务波动合理设置阈值。

单击【编辑】按钮，可以设置单 IP 访问阈值：![](https://mc.qcloudimg.com/static/img/73219f647610ad68bd274868a0e255a6/ipf-config-3.png)

## 配置案例

若域名```www.test.com``` IP 访问限频配置如下：![](https://mc.qcloudimg.com/static/img/145c8df5ad44613ed532c75b0216b723/ipf-config-2.png)IP 为 ```1.1.1.1``` 的用户，在 1s 中请求了 11 次资源 ```http://www.test.com/1.jpg```，均访问至CDN加速节点 A 中的一台server，此时在该 server 上产生 11 条访问日志，其中有一条因超出QPS限制，状态码为 514。

IP 为 ```2.2.2.2``` 的用户，在 1s 中请求了 11 次资源 ```http://www.test.com/1.jpg```，访问平均分布在多个CDN加速节点上，此时每一个加速节点均会正常返回内容。

