## 说明
本文介绍windows环境如何使用帆软FineBI工具搭配CDW，进行数据的可视化分析。

## 前提条件
1. 已经创建CDW集群，并申请好外网IP，参见 [申请外网地址](https://cloud.tencent.com/document/product/878/31443)。
2. 将本机的IP添加到CDW的白名单，参见 [管理 IP 白黑名单](https://cloud.tencent.com/document/product/878/31444)。
3. 下载并安装好帆软，参见 [帆软下载页面](https://www.finebi.com/product/download)。

## 步骤

1. 连接CDW，需要下载JDBC Driver，参见 [Pivotal Greenplum Database数据连接](https://help.finebi.com/doc-view-289.html)
从该页面中下载org.postgresql.Driver，并将该驱动包放置%FineBI%\webapps\webroot\WEB-INF\lib（windows下为安装目录）下，重启 FineBI。

2. 打开客户端，设置好管理员账号后，选择数据库，单击 **内置数据库** 中的 **直接登录**，如下图所示：
![](https://main.qcloudimg.com/raw/a7bd9ab992f10d322733660072d0e069.png)

3. 选择  **管理系统**>**数据连接**>**数据连接管理**，点击 **新建数据连接**，在所有选项下选择 **Pivotal Greenplum Database**，如下图所示：
![](https://main.qcloudimg.com/raw/0d1f08ec2d303f4391f4cf9289320d6e.png)
 
4. 填写数据库连接信息，如下图所示：
注：
需要选择org.postgresql.dirver。
CDW如果没有创建数据库，默认使用postgres。
需要提前将本机的IP加入CDW的白名单中,否则将会返回带有"no pg_hba.conf entry"的错误信息。
![](https://main.qcloudimg.com/raw/d59efdcdf7d1d907e019f83e659b5c26.png)

5. 点击 **点击连接数据库**，如下图就表示连接成功：
![](https://main.qcloudimg.com/raw/b3ab04183936a883753baacd234b73ec.png)

6. 保存数据源，如下图所示：
注：
这里需要选择正确的模式，默认是拉取第一个，通常是系统模式
![](https://main.qcloudimg.com/raw/b454456ba6e38f73054c3eded10c2d33.png)
