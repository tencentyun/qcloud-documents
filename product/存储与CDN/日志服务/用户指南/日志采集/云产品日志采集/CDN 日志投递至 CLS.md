## 简介

将域名接入内容分发网络 CDN 后，所有用户侧资源请求将调度至 CDN 节点进行响应。为了方便用户对资源访问情况进行统计分析，内容分发网络 CDN 已经与日志服务 CLS 平台打通，CDN 访问日志可实时上传至 CLS 进行多维分析，如质量和性能监控分析，用户访问 Top 分析，下载流量统计等。

>?目前 CDN 实时日志服务处在内测中，您可以填写 [申请表](https://cloud.tencent.com/apply/p/f4gs2k0au1i) 申请试用。如果您已经提交申请，我们将在七个工作日内对您的申请进行审核。



## 日志采集

1. 登录 [内容分发网络 CDN 控制台](https://console.cloud.tencent.com/cdn)，单击左侧目录的【日志服务】，进入日志服务页面后，单击【实时日志】页签。
2. 单击【新建】，创建日志主题。
3. 填写新增日志主题名称，绑定域名到该日志主题下：
	- 新建日志主题名称不可与现存日志主题名称相同
	- 一个域名只能绑定到一个日志主题下，不可绑定多个日志主题
	- 配置信息保存后，配置生效时间大约为15分钟
![](https://main.qcloudimg.com/raw/e04e398136dc52192752e866041ca109.png)
4. 登录 [日志服务 CLS 控制台](https://console.cloud.tencent.com/cls/)，单击左侧目录的【检索分析】，进入检索分析页面，如下配置：
 - 选择上海地域
 - 日志集选择 cdn_logset
 - 日志主题选择上述步骤3中创建日志主题的名称
5. 单击【检索分析】，即可实时检索 CDN 访问日志数据。
![](https://main.qcloudimg.com/raw/933dc1e79519e6fbbbdbde28eae78d2f.png)
#### 日志数据说明
推送至日志服务平台的日志为内容分发网络的日志，日志字段如下：
<table>
<thead>
<tr>
<th>日志字段</th>
<th>原始日志类型</th>
<th>日志服务类型</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>app_id</td>
<td>Integer</td>
<td>long</td>
<td>腾讯云账号 APPID</td>
</tr>
<tr>
<td>client_ip</td>
<td>String</td>
<td>text</td>
<td>客户端 IP</td>
</tr>
<tr>
<td>file_size</td>
<td>Integer</td>
<td>long</td>
<td>文件大小</td>
</tr>
<tr>
<td>hit</td>
<td>String</td>
<td>text</td>
<td>缓存 HIT / MISS，在 CDN 边缘节点命中、父节点命中均标记为 HIT</td>
</tr>
<tr>
<td>host</td>
<td>String</td>
<td>text</td>
<td>域名</td>
</tr>
<tr>
<td>http_code</td>
<td>Integer</td>
<td>long</td>
<td>HTTP 状态码</td>
</tr>
<tr>
<td>isp</td>
<td>String</td>
<td>text</td>
<td>运营商</td>
</tr>
<tr>
<td>method</td>
<td>String</td>
<td>text</td>
<td>HTTP Method</td>
</tr>
<tr>
<td>param</td>
<td>String</td>
<td>text</td>
<td>URL 携带的参数</td>
</tr>
<tr>
<td>proto</td>
<td>String</td>
<td>text</td>
<td>HTTP 协议标识</td>
</tr>
<tr>
<td>prov</td>
<td>String</td>
<td>text</td>
<td>运营商省份</td>
</tr>
<tr>
<td>referer</td>
<td>String</td>
<td>text</td>
<td>Referer 信息，HTTP  来源地址</td>
</tr>
<tr>
<td>request_range</td>
<td>String</td>
<td>text</td>
<td>Range 参数，请求范围</td>
</tr>
<tr>
<td>request_time</td>
<td>Integer</td>
<td>long</td>
<td>响应时间（毫秒），指节点从收到请求后响应所有回包再到客户端所花费的时间</td>
</tr>
<tr>
<td>rsp_size</td>
<td>Integer</td>
<td>long</td>
<td>返回字节数</td>
</tr>
<tr>
<td>time</td>
<td>Integer</td>
<td>long</td>
<td>请求时间，UNIX 时间戳</td>
</tr>
<tr>
<td>ua</td>
<td>String</td>
<td>text</td>
<td>User-Agent 信息</td>
</tr>
<tr>
<td>url</td>
<td>String</td>
<td>text</td>
<td>请求路径</td>
</tr>
<tr>
<td>uuid</td>
<td>String</td>
<td>text</td>
<td>请求的唯一标识</td>
</tr>
<tr>
<td>version</td>
<td>Integer</td>
<td>long</td>
<td>版本协议</td>
</tr>
</tbody></table>



## 日志分析示例

### 整体质量分析

#### 健康日志请求数
```plaintext
http_code<500 | select count(*)
```
![](https://main.qcloudimg.com/raw/249f81bd2ef8ac6d18726ce6ce135dbd.png)

#### 访问平均延时
```plaintext
select ROUND(avg(request_time),2)
```
![](https://main.qcloudimg.com/raw/de7476f4e9132bbea2b0f5ed9a0e5016.png)

### 错误诊断

#### 错误码分布
```plaintext
select http_code,count(*) as c group by http_code order by c desc
```
![](https://main.qcloudimg.com/raw/d16e394982efa873dd7785ab2a7b42fc.png)

#### 对某类错误码的日志查看分析
```plaintext
http_code:403
```
![](https://main.qcloudimg.com/raw/c175381141045fec430d2f06c19ff396.png)

