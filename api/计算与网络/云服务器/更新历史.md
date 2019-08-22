>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>



| 发布时间 | 更新概要 | 详细说明 |API版本 |
|---------|---------|---------|--------|
| 2017-09-26 |新增对弹性公网IP相关接口的支持 |新增支持的弹性公网IP接口如下：<br><li> 新增DescribeAddresses接口，查询弹性公网IP列表<br><li> 新增DescribeAddressQuota接口，查询弹性公网IP配额<br><li> 新增AllocateAddresses接口，创建弹性公网IP<br><li> 新增AssociateAddress接口，绑定弹性公网IP<br><li> 新增DisassociateAddress接口，解绑弹性公网IP<br><li> 新增TransformAddress接口，普通公网IP转弹性公网IP<br><li> 新增ModifyAddressAttribute接口，修改弹性公网IP属性<br><li> 新增ReleaseAddresses接口，释放弹性公网IP|2017-03-12|
| 2017-03-12 |新改版API接口第一版本上线 |如下相关接口，提供新改版API接口能力：<br><li> 地域相关所有接口 <br><li>实例相关所有接口 <br><li>镜像相关所有接口 <br><li>密钥相关所有接口|2017-03-12|


>? `API版本` 只限于在新改版后的API接口使用，每个新改版的接口也会要求必传该版本号；新改版API接口首次发布，版本号定为：`2017-03-12`。通常情况下API接口的变更都会保证向前兼容，这种时候API版本号不会出现变更；只有涉及重大变更或者新增修改无法向前兼容时我们才会推出新的版本号，用于区分不同的请求，实现向前兼容。
