## 背景
Gitlab 是⼀种类似 github 的服务，企业可以使⽤它来提供 git 存储库的内部管理。它是⼀个⾃我托管的 Git-repository 管理系统，可以保持⽤户代码的私密性，并且可以轻松地部署代码的更改。其优势在于：
- GitLab 提供了 GitLab Community Edition 版本，供⽤户在他们的代码所在的服务器上进行定位。
- GitLab 免费提供⽆限数量的私人和公共存储库。
- 代码⽚段可以共享项⽬中的少量代码，⽽不是共享整个项⽬。

Gitlab 服务的元数据库在新版本（12.1）中目前仅⽀持 PostgreSQL，Gitlab 介绍不再支持 MySQL 的理由如下：
- ⽆法⽀持嵌套分组查询。
- 必须使用黑科技来提升 MySQL 对列的限制，这将导致 MySQL 拒绝存储数据。
- MySQL ⽆法添加 TEXT 类型字段的⻓度限制。
- MySQL 不⽀持分区索引。

而 PostgreSQL 都能支持到以上场景。所以 Gitlab 在安装包中集成了 PostgreSQL，但对于某些企业⽽⾔，集成的数据库服务存在⼀定的安全风险，并且数据库服务的可靠性和可⽤性都不能得到保证。为了确保代码托管服务的稳定，部分业务和企业会选择采⽤稳定的外部数据库服务。而 Gitlab 在 Gitlab HA Repmgr 包中才⽀持基于 patroni 版本的⾼可⽤数据库。但是⾃⾏维护集群是⼀件成本较⾼的事情，采⽤腾讯云数据库可极⼤的减少这些维护操作。

本⽂介绍如何将 Gitlab 中的嵌⼊式数据库服务更换为腾讯云数据库 PostgreSQL 服务。

## 步骤1：安装 GitLab
**1. 准备资源**
- CentOS Linux release 7.6.1810 (Core)。
- gitlab-ce 14.9.3 版本。
- 云服务器⼀台，内存需4GB以上，磁盘需50GB以上。建议 /opt 独⽴挂载⼀个数据盘。
- 腾讯云数据库 PostgreSQL ⼀个，规格根据⾃身实际情况进⾏配置。可初始选择⼀个规格较小的实例。再根据具体使用进行扩容。版本根据 Gitlab 的版本进行调整选择。

**2. 下载 GitLab**
[单击此处](https://mirrors.tencent.com/gitlab-ce/) 在跳转页面下找到想要安装的 Gitlab 安装包，下载到本地后再上传⾄需要安装 Gitlab 服务的服务器中。

**3. 安装 GitLab**
使⽤ root ⽤户执⾏下列语句安装 Gitlab，若最后⼀步操作提示存在依赖包未安装，可直接通过 yum 或其他安装⼯具提前安装完成：
```
curl https://packages.gitlab.com/install/repositories/gitlab/gitlabce/script.rpm.sh > gitlab-ee_install.sh
sh gitlab-ee_install.sh
export EXTERNAL_URL=https://gitlab.example.com
yum install -y curl policycoreutils-python openssh-server cronie
rpm -ivh gitlab-ce-13.10.2-ce.0.el7.x86_64.rpm
```

## 步骤2：初始化数据源 PostgreSQL
1. 安装外部数据库 PostgreSQL，亦可直接使⽤云上数据库服务，如腾讯云数据库 PostgreSQL，要创建腾讯云数据库 PostgreSQL 请参见 [创建 PostgreSQL 实例](https://cloud.tencent.com/document/product/409/56961)。
>!创建或安装数据库时需确保数据库版本与 GitLab 版本要对应。否则在初始化 GitLab 时候将提示版本不⼀致，⽆法创建成功。
<table>
<thead><tr><th>GitLab 版本</th><th>最⼩⽀持的 PostgreSQL 版本</th></tr></thead>
<tbody><tr>
<td>13.0</td><td>11</td></tr>
<tr>
<td>14.0</td><td>12</td></tr>
</tbody></table>
2. 通过客户端⼯具登录⾄腾讯云数据库 PostgreSQL 中。可使⽤ psql ⼯具测试是否可以直接访问数据库，若⽆法访问，请排查⽹络链路和安全组配置。
```
psql -U <数据库管理员> -p <端口> -d postgres -h <访问地址>
```
3. ⾸先在数据库中创建⼀个 GitLab 所使⽤的帐号，如 gitlab，请注意此帐号必须拥有 superuser 权限或者云数据库所给与的管理员权限，如腾讯云的 `pg_tencentdb_superuser`。
```
create user gitlab login password 'gitlab_****_password#123';
grant gitlab to <当前管理员帐号>; grant pg_tencentdb_superuser to gitlab;
```
4. 然后创建⼀个 gitlab 所管理使⽤的 database：
```
create database gitlab owner=gitlab ENCODING = 'UTF8';
```
>!在 GitLab 库中必须要能⽀持 `pg_trgm、btree_gist、plpgsql` 插件，⽆需提前创建，在初始化 GitLab 时候将⾃动创建。但是需要保证能创建成功。

## 步骤3：修改 GitLab 元数据库为腾讯云数据库 PostgreSQL
1. 登录⾄ GitLab 安装服务器中，找到 gitlab 配置⽂件，默认为：/etc/gitlab/gitlab.rb。默认此⽂件中未配置任何信息，可通过下列命令查看到相关信息：
```
# cat /etc/gitlab/gitlab.rb |grep -v ^# | grep -v ^$
external_url 'http://gitlab.example.com'
```
2. 在此⽂件的最后加⼊以下信息，将腾讯云数据库 PostgreSQL 数据源加⼊到 gitlab 中：
```
## postgresql connect
## 此参数设置为 false 指禁用内置的 postgresql，而使用外部 postgresql 数据源
postgresql['enable'] = false
gitlab_rails['db_adapter'] = "postgresql"
gitlab_rails['db_encoding'] = "utf8"
## 数据库名
gitlab_rails['db_database'] = "gitlab"
gitlab_rails['db_pool'] = 100 ## 数据库用户
gitlab_rails['db_username'] = "gitlab"
## 密码，请根据自身配置修改
gitlab_rails['db_password'] = "gitlab_Test_password#123" ## 访问地址
gitlab_rails['db_host'] = "gz-tdcpg-ep-6kvx6p19.sql.tencentcdb.com" ## 访问端口
gitlab_rails['db_port'] = "25870"
```

请注意，此处如果配置访问地址为域名时，在初始化时候，将提示：
`ActiveRecord::ConnectionNotEstablished: could not translate host name "gz-tdcpgep-6kvx6p19.sql.tencentcdb.com " to address: Name or service not known`

所以若数据库访问为域名时，请使⽤ `ping` 命令找到此域名的 IP 地址或者找到能解析此域名的 DNS 服务器，不建议将访问地址的域名直接修改为 IP 地址，因为使⽤域名的场景常伴有数据库后端是做了负载均衡或者⾼可⽤，可直接在服务器中配置 DNS 服务器或者 host。若数据库服务有变化，则可直接修改 host 或者 DNS 服务，避免对 GitLab 服务进⾏修改。

## 步骤4：初始化与登录使用 GitLab
1. 执⾏以下命令初始化 GitLab，此命令执⾏会消耗⼀段时间，请耐心等待，当提示：`gitlab Reconfigured!` 时，说明已经初始化完成。
```
gitlab-ctl reconfigure
```
2. 执⾏以下命令启动 GitLab。
```
gitlab-ctl startok
```
3. 可使⽤以下 URL 访问 GitLab，若⽆法访问通，可能是服务器防⽕墙的限制。
地址示例：`http://{可访问的服务器 IP 地址}/users/sign_in`
登录界面如下：
![](https://qcloudimg.tencent-cloud.cn/raw/058dd5653ae76c625133701b56f709dd.png)
4. 初始登录帐号为 root，初始密码在初始完成后，会有如下的提示：
```
Password stored to /etc/gitlab/initial_root_password. This file will be 
cleaned up in first reconfigure run after 24 hours.
```
>?可在服务器中的此⽂件中找到初始化密码。完成登录后，请记得修改密码。
>
![](https://qcloudimg.tencent-cloud.cn/raw/573929dbbcdd08d849ab528c5781a183.png)
此时，GitLab 就安装完成，后续将正式使⽤ GitLab。
