伸缩组是遵循相同规则、面向同一场景的云服务器实例的集合。

## 新建伸缩组
登录[弹性伸缩控制台](https://console.cloud.tencent.com/autoscaling/config)，点击导航条中的【伸缩组】。点击![](//mccdn.qcloud.com/static/img/9d38f7bfbe02a922370765f3adfa58bf/image.png)，在弹出页面填写伸缩组基本信息。其中![](//mccdn.qcloud.com/static/img/f9df27a1d1e0d42a7ff08dd884bfa34c/image.png)为必填项。

- 伸缩组的当前CVM实例数将维持在最小伸缩数与最大伸缩数之间。
- 起始实例数定义了伸缩组一开始CVM实例的数量；
	- 若当前CVM实例数小于最小伸缩数，弹性伸缩服务将自动添加实例，使其等于最小伸缩数；
	- 若当前CVM实例数大于最大伸缩数，弹性伸缩服务将自动减少实例，使其等于最大伸缩数。
- 选择已有的启动配置，您也可以新建启动配置。
- 选择网络、可用区、移出策略。
- **（可选）选择关联已有负载均衡策略或新建负载均衡。**

![](https://mc.qcloudimg.com/static/img/2fb365611291fb8917637dba46f398f4/image.png)

配置完成后，此条目将显示在页面的伸缩组列表中，示例如下：
![](https://mc.qcloudimg.com/static/img/c1c64cdb16c11aaa6d31bc4781db62c4/image.png)

## 添加云主机(可选)
现在我们来绑定云主机。

在云主机列表添加进我们要绑定的云主机实例。完成配置后，此条目将显示在页面的启动配置列表中，示例如下：
![](https://mc.qcloudimg.com/static/img/e3232872ad5fe19e89c9eb7306418a3d/image.png)
> 注：如果在此处您遇到无法添加云主机或者无法移出云主机的情况，请检查您设置的最大伸缩数和最小伸缩数。

