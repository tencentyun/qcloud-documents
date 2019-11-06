## 操作场景
Drupal 是使用 PHP 语言编写的开源内容管理框架（CMF），由内容管理系统（CMS）及 PHP 开发框架（Framework）共同构成。Drupal 具备强大的定制化开发能力，您可使用 Drupal 作为个人或团体网站开发平台。
本文档以 CentOS 7.6 的 Linux 操作系统的腾讯云云服务器（CVM）为例，手动搭建 Drupal 个人网站。 

Drupal 组成及版本使用说明：
- Linux：Linux 操作系统，本文使用 CentOS 7.6。
- Apache：Web 服务器软件，本文使用 Apache 2.4.6。
- MariaDB：数据库管理系统，本文使用 MariaDB 10.4。
- PHP：脚本语言，本文使用 PHP 7.0.33。
- Drupal：网站内容管理框架，本文使用 Drupal 8.1.1。


## 技能要求
进行 Drupal 网站搭建，您需要熟悉 Liunx 操作系统及命令，例如 [CentOS 环境下通过 YUM 安装软件](https://cloud.tencent.com/document/product/213/2046) 等常用命令，并对所安装软件的使用及版本兼容性比较了解。


## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 已登录 Linux 云服务器。如果您还未登录，请准备好云服务器的登录密码及公网 IP，参考 [使用标准方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436) 完成登录。


## 操作步骤
### 搭建 LAMP 环境
当您登录 Linux 云服务器后，请完成 LAMP 环境的搭建。详情请参考 [手动搭建 LAMP 环境](https://cloud.tencent.com/document/product/213/38402)。

### 下载 Drupal
1. 依次执行以下命令，进入网站根目录并下载 Drupal 安装包。
```
cd /var/www/html
```
```
wget wget http://ftp.drupal.org/files/projects/drupal-8.1.1.zip
```
2. 依次执行以下命令，解压安装包并重命名。
```
unzip drupal-8.1.1.zip 
```
```
mv drupal-8.1.1/ drupal/
```
3. 依次执行以下命令，下载中文语言包。
```
cd drupal/
```
```
wget -P sites/default/files/translations https://ftp.drupal.org/files/translations/8.x/drupal/drupal-8.7.8.zh-hans.po
```

### 配置 Drupal 
1. 执行以下命令，打开 Apache 配置文件。
```
vi /etc/httpd/conf/httpd.conf
```
2. 按 “**i**” 或 “**Insert**” 切换至编辑模式，找到 `Directory "/var/www/html"></Directory>` 中的 `AllowOverride None` 并替换为以下内容：
```
AllowOverride All
```
修改完成后如下图所示：
![](https://main.qcloudimg.com/raw/c68f918f22d9c29607d59fe1847eff69.png)
3. 按 “**Esc**”，输入 “**:wq**”，保存文件并返回。
4. 执行以下命令，修改网站根目录用户权限。
```
chown -R apache:apache /var/www/html
```
5. 执行以下命令，重启 Apache 服务。
```
systemctl restart httpd
```


#### 配置 Drupal 数据库<span id="database"></span>
>!根据 MariaDB 版本，设置用户身份验证方式有一定区别，具体步骤请参见 MariaDB 官网。
>
1. 执行以下命令，进入 MariaDB。
```
mysql
```
2. 执行以下命令，创建 MariaDB 数据库。例如 “drupal”。
```
CREATE DATABASE drupal;
```
3. 执行以下命令，创建一个新用户。例如 “user”，登录密码为 `123456`。
```
CREATE USER 'user'@'localhost' IDENTIFIED BY '123456';
```
4. 执行以下命令，赋予用户对 “drupal” 数据库的全部权限。
```
GRANT ALL PRIVILEGES ON drupal.* TO 'user'@'localhost' IDENTIFIED BY '123456';
```
5. 执行以下命令，使所有配置生效。
```
FLUSH PRIVILEGES;
```
6. 执行以下命令，退出 MariaDB。
```
\q
```

#### 配置 root 帐户
1. 执行以下命令，进入 MariaDB。
```
mysql
```
2. 执行以下命令，设置 root 帐户密码。
>?MariaDB 10.4 在 CentOS 系统上已增加了 root 帐户免密登录功能，请执行以下步骤设置您的 root 帐户密码并牢记。
>
```
ALTER USER root@localhost IDENTIFIED VIA mysql_native_password USING PASSWORD('输入您的密码');
```
3. 执行以下命令，退出 MariaDB。
```
\q
```

### 安装 Drupal
1. 使用浏览器访问以下地址，进行 Drupal 安装。
```
http://云服务器公网IP/drupal
```
2. 单击【Save and contiue】，选择语言为简体中文。如下图所示：
![](https://main.qcloudimg.com/raw/bf2e3c265fcba528432cef6811b8ad4d.png)
3. 单击【保存并继续】，选择标准安装方式。如下图所示：
![](https://main.qcloudimg.com/raw/90dce9410361652ec8fc0de101c01657.png)
4. 输入在 [配置 Drupal 数据库](#database) 中已设置的数据库相关信息，并单击【保存并继续】。如下图所示：
>?当服务器环境配置正确，Drupal 会直接跳过检查安装需求此步骤。若您未通过检查，请结合实际情况，处理问题后再次安装。
>
![](https://main.qcloudimg.com/raw/df0771e770fb7ff0957f68842b191b52.png)
5. 等待安装完成后，自动进入网站设置页面。请结合您的实际需求进行填写，并单击【保存并继续】。如下图所示：
>?请记录站点维护帐号及密码。
>
![](https://main.qcloudimg.com/raw/8d371d5d27f4fe8d7cf565eb848e74bf.png)
6. 安装完成后，网站自动进入首页并登录维护帐号。如下图所示：
![](https://main.qcloudimg.com/raw/386561c62047ce3785ca8663a0308381.png)
您已成功搭建 Drupal 个人站点，可根据实际需求对网站进行个性化设置。
