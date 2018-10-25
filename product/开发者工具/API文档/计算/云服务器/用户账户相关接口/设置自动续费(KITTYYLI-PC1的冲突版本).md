## 1. 接口描述
 
域名：trade.api.qcloud.com
接口名: SetAutoRenew


批量修改CVM或CDB自动续费标识。设置自动续费标识后，每次在CVM或者CDB到期时，会自动续费一个月。

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> instanceType
<td> 是
<td> Int
<td> 实例类型，1：CVM，2：CDB
<tr>
<td> instanceIds.n
<td> 是
<td> String
<td> 一个或者多个实例ID，当instanceType为1时，表示主机的实例ID，可通过<a href="http://cloud.tencent.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8" title="DescribeInstances">DescribeInstances</a>接口返回字段中的 unInstanceId、instanceId 获取（建议使用 unInstanceId ）；此接口支持同时输入多台主机的实例ID( 如：要输入两台主机，则设置 instanceIds.1&instanceIds.2)。
<tr>
<td> autoRenew
<td> 是
<td> Int
<td> 自动续费标识，0为不自动续费，1为自动续费，2为不再续费
</tbody></table>

 

## 3. 输出参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message
<td> String
<td> 错误信息
</tbody></table>

 

## 4. 示例
 
输入
```
  https://cvm.api.qcloud.com/v2/index.php?Action=SetAutoRenew
  &instanceType=1&instanceIds.1=qcvm1234&autoRenew=1
  &COMMON_PARAMS
```

输出
```
  {
      "code":0,
      "message": "success",
  }
```
