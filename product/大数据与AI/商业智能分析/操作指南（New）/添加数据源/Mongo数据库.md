在添加 Mongo 数据库前，请先将商业智能分析 BI 的 IP 地址添加至数据库安全组，详见 [数据库连接方式概览](https://cloud.tencent.com/document/product/590/19294)。
1. 登录 [商业智能分析 BI 控制台](https://console.cloud.tencent.com/bi)，在添加数据源首页单击 **Mongo 数据库**，进入新建页面。新建的页面如下：
   ![](https://main.qcloudimg.com/raw/b277fe6cb82415a7c3ef401430cd2734.png)
2. 填写相应的 Mongo 数据库连接信息。
<table>
<thead>
<tr>
<th>配置项</th>
<th>必填</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>URL</td>
<td>是</td>
<td>MONGO 数据库的 URL 地址。</td>
</tr>
<tr>
<td>选择转换时区</td>
<td>否</td>
<td>输入数据存入 Mongo 时的时区。如果数据存入 Mongo 时，没有指定时区，即可以不用做选择。如果存入数据时，指定了时区，在这需要选择相应的时区对数据进行转换。</td>
</tr>
<tr>
<td>服务器登录</td>
<td>是</td>
<td>包含两种方式：用户名和密码、无身份验证。当数据库设定了访问权限后，用户需要使用用户名和密码来访问当前数据库。</td>
</tr>
<tr>
<td>默认数据库</td>
<td>否</td>
<td>控制数据源下展示的数据库。当输入一个默认数据库，数据源下就只展示这一个，如果此处不做指定，那将显示所有的数据库。</td>
</tr>
</tbody></table>
3. 单击**测试连接**，提示“测试成功”，即该数据源成功连接到相应数据库。
4. 单击菜单栏**保存**，保存该数据源。创建数据集和制作报告模块都可以使用已保存的数据源。
