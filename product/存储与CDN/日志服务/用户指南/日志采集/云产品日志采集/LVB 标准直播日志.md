## 简介
在借助标准直播 LVB 处理直播业务时，会产生大量的日志数据。标准直播 LVB 实时日志已经和腾讯云的日志服务 CLS 平台打通，将采集的实时日志实时推送至日志服务平台，5分钟快速接入日志服务 CLS ，帮助您实现“一站式”的日志管理。
![](https://main.qcloudimg.com/raw/5d8310deca5c97cd7225a297425c6089.png)

## 接入步骤

1. 登录 [标准直播控制台](https://console.cloud.tencent.com/live)，选择【日志分析】>【实时日志分析】，进入实时日志分析页面。
2. 如果首次进入实时日志，您需要单击【确定授权】，进行日志服务 CLS 的相关授权，才能正常使用检索功能。
   ![](https://main.qcloudimg.com/raw/9f343f94f60129df6352476892e23b78.png)
3. 单击【同意授权】，即可完成日志服务 CLS 的相关授权。
   ![](https://main.qcloudimg.com/raw/fb15cb0c2ec7b80d72866acaf1ce8a8a.png)
4. 您需要创建日志主题，并绑定域名。
	 ![](https://main.qcloudimg.com/raw/af3d8210ffe652d0622b8fc2a72fdb09.png)
	 >!创建成功后，该日志主题将默认创建在日志服务平台的成都地域。
5. 创建成功后，在日志主题右侧的操作栏中，单击【检索】，输入检索语句，可快速检索详细日志数据。日志服务的检索功能支持全文检索和键值检索，详细的检索语法，请参见检索 [语法与规则](https://cloud.tencent.com/document/product/614/16982)。
![](https://main.qcloudimg.com/raw/2cd4935e1a89246011c0276ec31e4570.png)
6. 若您需删除日志主题，可在日志主题右侧的操作栏中，单击【删除】。删除之后，系统将停止推送相关域名的日志数据，并将清除历史数据，同时您也无法再使用该主题对应的报表及检索功能。
	 ![](https://main.qcloudimg.com/raw/1c9420e60e645539906f35a4c1118e53.png)
7. 若您需关闭实时日志，可单击右上角的【关闭实时日志】开关。关闭之后，系统将停止推送日志数据，并将清除历史数据，同时您也无法再使用报表及检索等相关功能。
	 ![](https://main.qcloudimg.com/raw/29219ee80594c47ab55fc58185fe9017.png)


#### 日志字段说明
推送至日志服务平台的日志为标准直播的访问日志，日志字段如下：

| 字段名称           | 类型 | 说明               | 示例             |
| ------------------ | ---- | ------------------ | ---------------- |
| log_time           | long | 请求时间           | 20190527153501   |
| bytes_stream_id    | text | 流 ID              | test             |
| host               | text | 被访问的域名       | test.lvb.xyz     |
| uri                | text | URL                | /live/test.flv   |
| play_size          | long | 本次访问字节数大小 | 556              |
| play_tm            | long | 播放时长           | 311              |
| msg_client_ip      | text | 客户端IP           | 192.168.1.100    |
| client_province_id | long | 省份               | 19               |
| client_isp_id      | long | 运营商             | 1                |
| client_country_id  | long | country_id         | 1                |
| http_method        | text | HTTP Method        | GET              |
| connect_fd         | long | connect_fd         | 34596            |
| http_status        | long | HTTP 状态码        | 200              |
| user_agent         | text | User-Agent 信息    | "Lavf/58.15.100" |
| refer              | text | Refer信息          | "-"              |
| hit                | text | 缓存 HIT/MISS      | miss             |
| msg_self_ip        | text | 节点IP             | 10.10.1.2        |
| oc_country_id      | long | 服务器国家         | 1                |
| oc_area_info       | text | 服务器地区         | 中国             |



