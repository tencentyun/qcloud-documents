## 操作场景
GitLab 是使用 Ruby 开发的开源版本管理系统，以 Git 作为代码管理工具并实现自托管的 Git 项目仓库，可通过 Web 界面访问公开或私人的项目。本文介绍如何在腾讯云云服务器上安装并使用 GitLab。



## 示例版本
- GitLab：社区版 14.6.2 
- 本文使用的云服务器配置如下：
	- vCPU：2核
	- 内存：4GB
	- Linux 操作系统：以 CentOS 8.2 及 CentOS 7.9 为例

## 前提条件
- 已购买 Linux 云服务器。如果您还未购买云服务器，请参考 [快速配置 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。
- Linux 实例已配置安全组规则：放通80端口。具体步骤请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。

## 操作步骤
### 安装 GitLab
1. 登录实例，详情请参见 [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。
2. 对应实际使用的操作系统执行以下命令，安装依赖包。
<dx-tabs>
::: CentOS 8.2
```
yum install -y curl policycoreutils-python-utils openssh-server
```
:::
::: CentOS 7.7
```
yum install -y curl policycoreutils-python openssh-server
```
:::
</dx-tabs>
3. 依次执行以下命令，设置 SSH 开机自启动并启动 SSH 服务。
```
systemctl enable sshd
```
```
systemctl start sshd
```
4. 执行以下命令，安装 Postfix。
```
yum install -y postfix
```
5. 执行以下命令，设置 Postfix 服务开机自启动。
```
systemctl enable postfix
```
6. 执行以下命令，打开 Postfix 的配置文件 main.cf。
```
vim /etc/postfix/main.cf
```
7. 按 **i** 进入编辑模式，删除 `inet_interfaces = all` 前的 `#`，在 `inet_interfaces = localhost` 前加上 `#`。修改完成后如下图所示： 
![](https://main.qcloudimg.com/raw/57fa73bdcd05343b5dcee24e47b5f09a.png)
8. 按 **Esc** 并输入 **:wq** 保存修改并退出文件。
9. 执行以下命令，启动 Postfix。
```
systemctl start postfix
```
10. 执行以下命令，添加 GitLab 软件包仓库。
```
 curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
```
11. 执行以下命令，安装 GitLab。
```
sudo EXTERNAL_URL="实例公网 IP 地址" yum install -y gitlab-ce
```
如何获取实例公网 IP，请参见 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。
12. 在本地浏览器中访问已获取的公网 IP，返回页面如下所示，则表示已成功安装 GitLab。
<img src="https://qcloudimg.tencent-cloud.cn/raw/abaf3b700a58ed5b4a1e13e9d82eaf7e.png"/>


### 设置管理员帐户密码
1. 获取管理员帐户默认密码。
 登录实例，并执行以下命令获取管理员 `root` 帐户登录密码。
```
cat /etc/gitlab/initial_root_password
```
获取如下图所示密码：
![](https://qcloudimg.tencent-cloud.cn/raw/01bfa701452cc470fbdbfb82ab294237.png)
2. 登录 GitLab。
在本地浏览器中访问云服务器的公网 IP，进入 GitLab 登录界面。使用 `root` 帐户及已获取的登录密码进行登录。
3. 修改管理员帐户密码。
由于保存默认密码的文件将在首次配置运行24小时后自动删除，请尽快修改 `root` 帐户登录密码。
 1. 选择页面右上角的用户头像，在弹出菜单中选择 **Perferences**。
 2. 在 “User Settings” 页面中，选择左侧导航栏的 **Password**。
 3. 在页面中输入目前使用密码，新密码及确认新密码后，单击 **Save Password** 即可。如下图所示：
 ![](https://qcloudimg.tencent-cloud.cn/raw/25adb5b68d48873392684d1a1030bbe1.png)

### 创建项目
1. 使用 `root` 帐户及已设置的登录密码进行登录。
2. 根据页面指引创建私人项目，本文以 `test` 为例。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/a6d85a83b86a44c1f39dbd363a3311ce.png)
3. 成功创建项目后，单击页面上方提示中的 **Add SSH Key**。
4. 进入 “SSH Keys” 页面，按照以下步骤添加 SSH Key：
 1. 通过 [获取密钥](#getKey) 步骤，获取需纳入项目管理 PC 的密钥信息，粘贴在 “Key” 中。
 2. 在 “Title” 中自定义命名该密钥。
 3. 单击 **Add key** 即可添加密钥。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/504b7a69215471516f7ace36bb5606af.png)
如下图所示则表示密钥添加成功：
![](https://qcloudimg.tencent-cloud.cn/raw/2d46dcb48b51243ce4fc91b319b3ede3.png)
5. [](id:Step5)返回项目首页，单击 **clone** 记录项目地址。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9edb130321b5df140cfc863c73f6837d.png)


### 克隆项目
1. 在已纳入管理的 PC 上执行以下命令，配置使用 Git 仓库的人员姓名。
```
git config --global user.name "username" 
```
2. 执行以下命令，配置使用 Git 仓库的人员邮箱。
```
git config --global user.email "xxx@example.com" 
```
3. 执行以下命令，克隆项目。其中“项目地址”请替换为已在 [步骤5](#Step5) 中获取的项目地址。
```
git clone “项目地址”
```
克隆项目成功后，会在本地生成同名目录且包含项目中所有文件。

### 上传文件
1. 执行以下命令，进入项目目录。
```
cd test/
```
2. 执行以下命令，创建需上传至 GitLab 的目标文件。本文以 test.sh 为例。
```
echo "test" > test.sh
```
3. 执行以下命令，将 test.sh 文件加入索引中。
```
git add test.sh
```
4. 执行以下命令，将 test.sh 提交至本地仓库。
```
git commit -m "test.sh"
```
5. 执行以下命令，将 test.sh 同步至 GitLab 服务器。
```
git push
```
返回 test 项目页面，即可查看文件已成功上传。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/0440c9a53b3a93d056119fd47f39638e.png)

## 相关操作
### 获取密钥[](id:getKey)
1. 在需要纳入项目管理的 PC 上执行以下命令，安装 Git。
```
yum install -y git
```
2. 执行以下命令，生成密钥文件 .ssh/id_rsa。生成密钥文件步骤中请按 **Enter** 保持默认设置。
```
ssh-keygen
```
3. 执行以下命令，查看并记录密钥信息。
```
cat .ssh/id_rsa.pub
```
