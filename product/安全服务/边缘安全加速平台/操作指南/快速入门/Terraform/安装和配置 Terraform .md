本文介绍如何安装和配置 Terraform。

## 步骤1：安装 Terraform[](id:Step1)
1. 前往 [Terraform 官网](https://www.terraform.io/downloads.html)，使用命令行直接安装 Terraform 或下载二进制安装文件。
2. 解压并配置全局路径。
若您通过命令行安装，则请跳过此步骤。若您通过下载二进制安装文件，则请配置全局路径。
<dx-tabs>
::: Linux 及 macOS
 1. 执行以下命令进行解压，请将 1.x.x 替换为您实际安装 Terraform 版本号。
```bash
unzip terraform_1.x.x_linux_amd64.zip
```
 2. 执行以下命令，将当前目录添加至 `~/.profile` 文件中。
```bash
echo $"export PATH=\$PATH:$(pwd)" >> ~/.bash_profile
```
 3. 执行以下命令，使全局路径配置生效。
```bash
source ~/.bash_profile
```
:::
::: Windows
1. 在桌面中，右键选择“计算机”，并在弹出菜单中选择**属性**。
2. 在弹出窗口中，找到并单击**高级系统设置**。
3. 在弹出的“系统属性”窗口中，单击**环境变量**。
4. 在“系统变量”中，找到 `Path`，将 `terraform.exe` 的绝对路径加入其中。如下图所示：
本文以 Windows 10 操作系统为例，`terraform.exe` 位于 `D:\xxxx\terraform` 文件下。
![](https://qcloudimg.tencent-cloud.cn/raw/7397b42ea05193f290adaa5dc81eb682.png)
5. 单击**确定**即可。

:::
</dx-tabs>
3. 执行以下命令，查看是否安装成功。
```bash
terraform  -version
```
返回信息如下所示（版本号可能存在差异），则表示安装成功。
```bash
> Terraform v1.0.10
> on darwin_amd64
> Your version of Terraform is out of date! The latest version
> is 1.1.0. You can update by downloading from https://www.terraform.io/downloads.html
```

##  步骤2：配置安全凭证[](id:capi)
在首次使用 Terraform 之前，请前往 [云 API 密钥页面](https://console.cloud.tencent.com/cam/capi) 申请安全凭证 SecretId 和 SecretKey。若已有可使用的安全凭证，则跳至第3步。

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，在左侧导航栏，选择**访问密钥** > **API 密钥管理**。
2. 在 API 密钥管理页面，单击 **新建密钥**，即可以创建一对 SecretId/SecretKey。
![](https://qcloudimg.tencent-cloud.cn/raw/0be75d948a22733581e1d5990bc4d643.png)
3. 您可通过以下两种方式进行鉴权：
<dx-tabs>
::: 环境变量鉴权
请将如下信息添加至环境变量配置：
`<your-secret-id>` 及 `<your-secret-key>` 请替换为 [获取凭证](#capi) 中的 `SecretId` 和 `SecretKey`。
```
export TENCENTCLOUD_SECRET_ID=<your-secret-id>
export TENCENTCLOUD_SECRET_KEY=<your-secret-key>
```
:::
::: 静态凭证鉴权
在用户目录下创建 `provider.tf` 文件，输入如下内容：
`<your-secret-id>` 及 `<your-secret-key>` 请替换为 [获取凭证](#capi) 中的 `SecretId` 和 `SecretKey`。
```
provider "tencentcloud" {
    secret_id = "<your-secret-id>"
    secret_key = "<your-secret-key>"
}
```
:::
</dx-tabs>
4. 到此已完成 Terraform 安装和环境变量配置，可进行下一步：[通过 Terraform 创建站点](https://cloud.tencent.com/document/product/1552/82136)。


