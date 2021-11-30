在添加 Hive 数据库前，请先将商业智能分析 BI 的 IP 地址添加至数据库安全组，详见 [数据库连接方式概览](https://cloud.tencent.com/document/product/590/19294)。
1. 登录 [商业智能分析 BI 控制台](https://console.cloud.tencent.com/bi)，在添加数据源首页单击 **Hive 数据库**，进入新建页面。新建的页面如下：
   ![](https://main.qcloudimg.com/raw/cd2e0b6e54a7b041cc26b51ba0dfd56a.png)
2. 填写相应的 Hive 数据库连接信息。选择**服务器登录**为 Kerberos 登录方式，界面展示如下： ![](https://main.qcloudimg.com/raw/9aaa97118466f490dfdfe53afd767700.png)
<table>
<thead>
<tr>
<th>配置项</th>
<th>必填</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>选择数据源</td>
<td>是</td>
<td>默认是在首页选择的数据库类型。用户也可以在下拉列表里选择其它的数据库类型，此处选中的是 Hive。</td>
</tr>
<tr>
<td>仅对有写权限的用户可见</td>
<td>否</td>
<td>如果 user1 对数据源只有读权限，对依赖此数据源的数据集有读或者读写权限，勾选此项，用 user1 登录，进入创建数据集模块，打开数据源会提示“仅对有些权限的用户可见”，打开依赖此数据源的数据集，数据源信息是收起的且不可展开。</td>
</tr>
<tr>
<td>驱动</td>
<td>是</td>
<td>用户可手动填写或选择需要的驱动类型。</td>
</tr>
<tr>
<td>URL</td>
<td>是</td>
<td>设定数据源 URL。</td>
</tr>
<tr>
<td>服务器登录</td>
<td>是</td>
<td>包含四种方式：用户名和密码、无身份验证、用户名、Kerberos。当数据库设定了访问权限后，用户需要使用用户名和密码或者只有用户名来访问当前数据库。</td>
</tr>
<tr>
<td>密钥文件路径</td>
<td>是</td>
<td>KeyTab 文件的路径，如：<code>/opt/xxx/user.keytab</code>。</td>
</tr>
<tr>
<td>Krb5 文件路径</td>
<td>是</td>
<td>Krb5 文件的路径。Linux 环境下 Krb5 文件的名字为<code>Krb5.conf</code>；Windows 环境下名字为<code>Krb5.ini</code>。Krb5 文件一般会放到一个默认的位置，无需另外配置该项。如果客户未提供此文件，即表示已在默认位置放置此文件。一般情况下，Windows 的默认位置是 <code>C:\Windows\Krb5.ini</code> 或者 <code>C:\winnt\Krb5.ini</code>；Linux 的默认位置是<code>/etc/Krb5.conf</code>或者 <code>/etc/krb5/krb5.conf</code>。</td>
</tr>
<tr>
<td>Jaas 文件路径</td>
<td>否</td>
<td>Jaas 文件的路径。该配置文件一般是用于 Zookeeper 安全认证的。例如<code>/opt/xxx/jaas.conf</code>。</td>
</tr>
<tr>
<td>用户名</td>
<td>是</td>
<td>用户所对应的 Kerberos Principal Name。</td>
</tr>
<tr>
<td>最大连接数</td>
<td>否</td>
<td>该数据源最多的连接个数。</td>
</tr>
<tr>
<td>队列名</td>
<td>否</td>
<td>Hadoop 设置任务执行的队列以及优先级。</td>
</tr>
<tr>
<td>表结构模式</td>
<td>否</td>
<td>控制数据源下展示的表结构模式。当选择一个表结构模式，数据源下就只展示指定的这一个，如果此处不做指定，那将显示所有的表结构模式。</td>
</tr>
</tbody></table>
2. 单击**测试连接**，提示“测试成功”，即该数据源成功连接到相应数据库。
3. 单击菜单栏**保存**，保存该数据源。创建数据集和制作报告模块都可以使用已保存的数据源。
