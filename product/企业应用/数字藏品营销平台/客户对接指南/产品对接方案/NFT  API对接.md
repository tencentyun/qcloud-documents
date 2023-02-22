## 适用场景
**数字藏品免费营销场景：**
- 客户自有客户端（小程序、App、H5 站点），有研发资源。
- 个性化活动链路，按客户侧需求定制数字藏品活动，例如：积分商城兑换、会员运营活动抽奖等。
- 个性化数字藏品管理链路。例如：在客户自有客户端个人中心中作为一个子模块。支持数字藏品查看、分享。

**搭售场景：**
- 客户自有客户端（小程序、App、H5 站点），有研发资源支持。
- 在现有的交易场景实现数字藏品搭售或买赠，例如：购买景区门票、演出门票、实物商品后赠送数字藏品。


## 功能说明

接口列表：

<table>
<thead>
<tr>
<th>序号</th>
<th>接口分类</th>
<th>接口名称</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td>1</td>
<td>发行服务（待开放）</td>
<td>企业注册、系列管理、介质上传、发行上链</td>
<td>待开放</td>
</tr>
<tr>
<td>2</td>
<td rowspan="4">用户管理</td>
<td>发放验证码接口</td>
<td>-</td>
</tr>
<tr>
<td>3</td>
<td>用户注册接口</td>
<td>-</td>
</tr>
<tr>
<td>4</td>
<td>查询用户信息接口</td>
<td>-</td>
</tr>
<tr>
<td>5</td>
<td>用户资产更新通知</td>
<td>需客户侧订阅</td>
</tr>
<tr>
<td>6</td>
<td rowspan="4">藏品管理</td>
<td>转移藏品接口</td>
<td>-</td>
</tr>
<tr>
<td>7</td>
<td>查询藏品转移状态接口</td>
<td>-</td>
</tr>
<tr>
<td>8</td>
<td>权益发放接口</td>
<td>-</td>
</tr>
<tr>
<td>9</td>
<td>系统对账接口</td>
<td>-</td>
</tr>
</tbody></table>



## 对接流程

1. 客户侧申请小程序数字藏品类目。
2. 客户侧设计藏品素材、个性化活动链路、个性化藏品管理、活动对接。
3. 腾讯侧完成藏品发行、活动规则法务审核。
4. 客户侧研发：
	4.1 邮件申请 API 权限
	4.2 通过对接 NFT API 完成用户注册、数字藏品发放、查看、分享。
5. 小程序提审、上线。



## 相关资料
- [腾讯 Web3.0 数字营销平台 API 协议 - v2.3 - 20220802](https://doc.weixin.qq.com/doc/w3_AQ0ARgYnABA7hHdTcPUQLeL11xhPS)
- [腾讯 Web3.0 数字营销平台 - 品牌小程序对接流程图](https://doc.weixin.qq.com/flowchart/f3_AQ0ARgYnABAZXOQtslATOOG6ZD1nU?scode=AJEAIQdfAAosICjcQlAQ0ARgYnABA)
