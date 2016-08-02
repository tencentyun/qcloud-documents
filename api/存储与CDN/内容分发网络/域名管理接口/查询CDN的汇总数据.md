## 1. 接口描述
 
域名：cdn.api.qcloud.com
接口名: DescribeCdnHostInfo

查询接入CDN的Hosts在所查询时间内的汇总数据信息。
可获得最近30日内(含30日)的总数据;

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> startDate
<td> 是
<td> String
<td> 查询开始时间（日）
<tr>
<td> endDate
<td> 是
<td> String
<td> 查询结束时间（日）
<tr>
<td> statType
<td> 是
<td> String
<td> 选择要查看的维度:流量(Byte)、带宽(bps)、请求数、IP访问数、命中率('flux','bandwidth','requests','ip_visits','cache')；
<tr>
<td> hosts.n
<td> 否
<td> String
<td> Host为空时输出全部Hosts和的数据,输入一个Host输出这单个Host的数据,输入大于1个Host输出为输入的Hosts的和的数据
<tr>
<td> projects.n
<td> 是
<td> String
<td> host对应项目的项目ID
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
<td> 错误信息/查询结果:查询时间,HostList,查询类型:流量or带宽or请求数orIP访问数or命中率的数组；
</tbody></table>

 

## 4. 示例
 
输入
```
  https://domain/v2/index.php?Action=DescribeCdnHostInfo
  &statType=bandwidth 
  &startDate=2015-04-17 
  &endDate=2015-04-20 
  &projects.0=1000063 
  &projects.1=1000010 
  &hosts.0=www.gomezshuitest.com
```

输出
```
  {
      "code":0,
      "message": "",
  }

```


