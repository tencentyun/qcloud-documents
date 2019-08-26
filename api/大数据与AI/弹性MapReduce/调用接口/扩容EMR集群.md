## 接口描述
 
本接口（EmrScaleoutCluster）用于扩容一个创建好的 EMR 集群。

接口请求域名：`emr.api.qcloud.com`

1. 可扩容的节点为 core 节点和 task 节点。
2. 扩容的节点配置和已有节点配置一致。
3. 新扩容的节点会自动安装已安装组件，并加入已有集群。

扩容限制为：
1. 单次扩容，core 节点和 task 节点最多支持20个。
2. 按量计费集群，扩容 core 节点和 task 节点的计费模式都只能是按量计费。
3. 包年包月集群，core 节点的扩容只能是包年包月，task 节点可以包年包月或者按量计费。

## 输入参数
 以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 <a href="/doc/api/372/4153" title="公共请求参数">公共请求参数</a> 页面。其中，此接口的 Action 字段 EmrScaleoutCluster。
 
 | 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| ClusterId | 是 | string | 待扩容的集群 ID，emr-xxxx 格式 |
| CoreNodes | 是 | uint | 扩容 core 节点个数 |
| TaskNodes | 是 | uint | 扩容 task 节点个数 |
| NodeChargeType | 是 | uint | 扩容节点的计费类型，0：按量计费，1：包年包月 |

## 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 <a href="https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81" title="公共错误码">公共错误码</a>。|
| message | String | 模块错误信息描述，与接口相关。|

## 示例
 包年包月集群扩容一个包年包月的 task 节点和 core 节点。
 
输入
<pre>
  https://emr.api.qcloud.com/v2/index.php?Action=EmrScaleoutCluster
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
  &ClusterId=emr-rowyenms
  &CoreNodes=1
  &TaskNodes=1
  &NodeChargeType=1

</pre>

输出
```
{
    "code": 0,
    "message": ""
}
```
