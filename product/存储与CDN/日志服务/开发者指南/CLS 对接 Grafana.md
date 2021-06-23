## 操作场景

日志服务（Cloud Log Service，CLS）与 Grafana 打通，支持将 CLS 的原始日志数据与 SQL 聚合分析结果导出，并在 Grafana 展示。您只需安装 CLS 日志服务 Grafana 插件，并在 Grafana 填写检索分析的语句，即可在 Grafana 上展示结果。

您可以根据如下用户名和密码，前往 [CLS 对接 Grafana 的体验网站](http://106.53.153.13:3000/d/r6mrhEbGz/cls-demo) 进行体验。
- 用户名：Viewer
- 密码：clsdemo

本文档以 CentOS 操作系统为例，指导您安装和配置 Grafana。

## 操作步骤

### 安装 Grafana

安装 Grafana，具体操作请参见 [Grafana 官网文档](https://grafana.com/docs/grafana/latest/installation/)。
以 CentOS 安装 grafana 7.3.6 为例：
```
sudo yum install initscripts urw-fonts wget
wget https://dl.grafana.com/oss/release/grafana-7.3.6-1.x86_64.rpm
sudo yum install grafana-7.3.6-1.x86_64.rpm
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server 
sudo systemctl enable grafana-server  
```
如需安装更多可视化图表（例如饼图、趋势速览图等），请执行对应的命令安装 grafana panel 插件。
例如，您需要安装饼图（pie panel），可执行如下命令：
```
grafana-cli plugins install grafana-piechart-panel
service grafana-server restart
```
更多插件安装，请参考 [Grafana plugins](https://grafana.com/grafana/plugins?type=panel)。

### 安装和配置 CLS 对接 Grafana 插件

1. 在`/var/lib/grafana/plugins/`插件目录下安装 CLS 对接 Grafana 插件。
```
cd /var/lib/grafana/plugins/
wget https://github.com/TencentCloud/cls-grafana-datasource/releases/latest/download/tencent-cls-grafana-datasource.zip
unzip tencent-cls-grafana-datasource
```
>? 
> - 如果您的云服务器非 CentOS 系统，请先确认 Grafana 的插件目录位置，再进入该插件目录进行安装。
> - 需要安装 Grafana 7.0以上版本才可使用此插件。若 Grafana 版本低于7.0，需进行配置备份和升级，详情请参考 [Grafana 升级指南](https://grafana.com/docs/grafana/latest/installation/upgrading/)。
> 
2. 在已部署 Grafana 的机器中，打开 `grafana.ini` 配置文件。
 - MacOS 系统的文件路径：`/usr/local/etc/grafana/grafana.ini`
 - Linux 系统的文件路径：`/etc/grafana/grafana.ini`
3. 在 **plugins** 中设置 **allow_loading_unsigned_plugins** 参数。
```
allow_loading_unsigned_plugins = tencent-cls-grafana-datasource
```
5. 执行如下命令，重启 grafana 服务。
```
   service grafana-server restart
```

### 配置日志数据源<span id="ConfigLogDataSource"></span>
1. 在浏览器中访问以下地址，登录 Grafana。
>? Grafana 的默认端口为3000端口。
>
```
http://Grafana IP 地址:3000
```
2. 在左侧菜单栏中，选择设置图标，进入**Data Sources** 页面。
3. 在 **Data Sources** 页面，单击【**Add data source**】。
4. 选中【**Tencent Cloud Log Service Datasource**】，并按照如下说明配置数据源。
![image-20201229200229285](https://main.qcloudimg.com/raw/275835ded7a0826d6027984ab9aa0b84.png)
<table>
<tr><th>配置项</th><th>说明</th><tr>
<tr><td>Security Credentials</td><td>SecretId、SecretKey：API 请求密钥，用于身份鉴权。可前往 <a href="https://console.cloud.tencent.com/cam/capi">API 密钥管理</a> 获取地址。</td><tr>
<tr><td>Log Service Info</td><td><ul><li>region：日志服务区域简称。例如，北京区域填写`ap-beijing`。</br>完整的区域列表格式请参考 <a href="https://cloud.tencent.com/document/product/614/18940">地域列表</a>。</li><li>TopicId：日志主题 ID。</li></ul></td><tr>
</table>

### 配置 dashboard

1. 在左侧导航栏中，单击【**Creat Dashboards**】。
2. 在 Dashboard 页面，单击【**Add new panel**】。
3. 将数据源选择为您新建的日志数据源。如下图所示：
   ![image-20201229200254913](https://main.qcloudimg.com/raw/b0981c7c5e43d803d0eb694f3b737060.png)
4. 输入 Query 语句，并根据待展示的图表类型，选择 Format 形式。系统会自动转换数据以满足 Grafana 的展示。
<table>
<tr><th>Format 格式</th><th>描述</th><th>配置项</th><tr>
<tr><td>Log panel</td><td>log panel is used to shown log search result. Query syntax supports searching by keyword, fuzzy match. For more information, see [Syntax and Rules](https://intl.cloud.tencent.com/document/product/614/30439). Eg. status:400</td><td>limit：用于指定返回日志检索结果条数。</td><tr>
<tr><td>Table panle</td><td>Table panel will automatically show the results of whatever columns and rows your query returns</td><td>无</td><tr>
<tr><td>Graph,Pie,Gauge panel</td><td>In this pattern, there is a format transformation where data will be adapted to graph,pie,gauge panel</td><td><ul><li>Metrics：待统计指标。</li><li>Bucket：（选填）聚合列名称。</li><li>Time : （选填）若 query 返回结果为连续时间数据，则需指定 time 字段。若无，则不填写。</li></ul></td><tr>
</table>


## 操作示例

### 时间折线图

时间折线图（Graph） 展示 pv，uv 数据曲线。如下图所示：
![image-20201230174944290](https://main.qcloudimg.com/raw/a2251243a6e592bed01ad372a8ebbc55.png)
您可以根据如下信息进行配置：
- 输入的 Query 语句如下所示：
```
* | select histogram( cast(__TIMESTAMP__ as timestamp),interval 1 minute) as time, count(*) as pv,count( distinct remote_addr) as uv group by time order by time limit 1000
```
- Format：选择 **Graph,Pie,Gauge panel**。
- Metrics：**pv，uv**。
- Bucket：无聚合列，**不填写**。
- Time : **time**。

### 饼图

饼图（Pie）展示请求状态码分布。如下图所示：
![image-20201229205154667](https://main.qcloudimg.com/raw/95bee33d6332e70ee01c49c5f69d13ac.png)
您可以根据如下信息进行配置：
- 输入的 Query 语句如下所示：
```
* | select count(*) as count, status group by status
```
- Format：选择 **Graph,Pie,Gauge panel**。
- Metrics：**count**。
- Bucket：**status**。
- Time：不是连续时间数据，**不填写**。

### 柱状图，压力图

柱状图，压力图（bar gauge）统计访问延时前10的页面。如下图所示：
![image-20201230175052388](https://main.qcloudimg.com/raw/c8c9cade19d03458a99747b851a2df4e.png)
您可以根据如下信息进行配置：
- 输入的 Query 语句如下所示：
```
* | select http_referer,avg(request_time) as lagency group by http_referer order by lagency desc limit 10
```
- Format：选择 **Graph,Pie,Gauge panel**。
- Metrics：lagency。
- Bucket：http_referer。
- Time：不是连续时间数据，**不填写**。

### 表格Table

表格（Table）展示访问量前10的用户。如下图所示：
![image-20201229211653406](https://main.qcloudimg.com/raw/afbde7667f22458e5ae6e34ede848a56.png)
您可以根据如下信息进行配置：
- 输入的 Query 语句如下所示：
```
* | select remote_addr,count(*) as count group by remote_addr order by count desc limit 10
```
- Format：Table



