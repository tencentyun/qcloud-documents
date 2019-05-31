>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
本接口 (DescribeAvailabilityZones) 用于查询腾讯云可用区的详细信息。

接口请求域名：cvm.api.qcloud.com

* 可用区的定义请参看 [产品文档中的地域一节](https://cloud.tencent.com/doc/product/213/497#2.-.E5.8F.AF.E7.94.A8.E5.8C.BA)。
* 内容包括可用区具体的 IDC。
* 可以指定可用区 ID 来查看单一可用区的信息。
* 可用区 ID 列表如下：

| 可用区名称 |可用区 ID|
|---------|---------|
| 广州一区 |100001|
| 广州二区 |100002|
| 广州三区 |100003|
| 广州四区 |100004|
| 上海一区 |200001|
| 上海二区 |200002|
| 香港一区 |300001|
| 多伦多一区 |400001|
| 上海金融一区 |700001|
| 上海金融二区 |700002|
| 北京一区 |800001|
| 北京二区 |800002|
| 新加坡一区 |900001|
| 深圳金融一区 |110001|
| 深圳金融二区 |110002|
| 广州Open专区 |120001|
| 硅谷一区 |150001|
| 成都一区 |160001|
| 成都二区 |160002|
| 法兰克福一区 |170001|
| 首尔一区 |180001|

## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数见 [公共请求参数](/document/api/213/6976) 页面。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| zoneId| 否| Int| 可用区 ID。|




## 3. 输出参数


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code| Int| 错误码（0：成功，其他值：失败）。|
| message| String| 错误信息。|
| totalCount| Int| 可用区的数目。|
| zoneSet| Array| 可用区列表。|

zoneSet 是一个可用区信息的集合，单个可用区信息的数据结构如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| zoneId| Int| 可用区ID。|
| idcList| Array| IDC列表。|


idcList 是可用区下属 IDC 信息的集合，单个 IDC 信息的数据结构如下：

| 参数名称  | 类型 | 描述 |
|---------|---------|---------|
| idcId| Int| IDC的ID值。|
| idcName| String| IDC名称。|




## 4. 示例

输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeAvailabilityZones
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  zoneId=100001
</pre>

输出

```
{
	"code": 0,
	"message": "",
	"totalCount": 1,
	"zoneSet": {
		"zoneName": "广州一区",
		"idcList": [{
				"idcId": 685,
				"idcName": "广州电信亚太信息AC2楼"
			},
			{
				"idcId": 737,
				"idcName": "广州电信亚太信息AC4楼02"
			},
			{
				"idcId": 798,
				"idcName": "广州移动南方基地AC2楼"
			},
			{
				"idcId": 834,
				"idcName": "广州电信人民中路AC7楼"
			},
			{
				"idcId": 908,
				"idcName": "广州电信石基AC5楼"
			},
			{
				"idcId": 1035,
				"idcName": "广州电信石基AC4楼M2"
			},
			{
				"idcId": 1327,
				"idcName": "广州电信石基AC4楼M3"
			}
		],
		"zoneId": 100001
	}
}

```




