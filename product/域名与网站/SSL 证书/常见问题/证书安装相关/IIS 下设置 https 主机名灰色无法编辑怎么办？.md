## 现象描述
使用 IIS 管理器进行安装证书时，将 pfx 证书文件导入后，在添加网站绑定域名过程中，类型选择为 “https” 时，主机名显示无法编辑。如下图所示：
![](https://main.qcloudimg.com/raw/b109991fe1a8191d6e0d86618f9a1548.png)

## 可能原因
Windows Server 2008不支持该操作，需要修改对应文件。

##  解决办法
1. 请按路径 `C:\Windows\system32\inetsrv\config\applicationHost.config` 打开 `applicationHost.config` 文件。
2. 修改内容如下：
>?
>- 以 “tencent.com” 域名为例。
>- 将 `<binding protocol="https" bindingInformation="*:443:" />` 修改为
 `<binding protocol="https" bindingInformation="*:443:tencent.com" />`。
>- 文件无法直接修改时，可以尝试使用管理员权限进行修改或复制文件到桌面修改后，进行替换。
>
```
<site name="example.tencent.com" id="8">
                <application path="/">
                    <virtualDirectory path="/" physicalPath="D:\web\tencent" />
                </application>
                <bindings>
                    <binding protocol="http" bindingInformation="*:80:example.tencent.com" />
                    <binding protocol="http" bindingInformation="*:80:www.tencent.com" />
                    <binding protocol="https" bindingInformation="*:443:" />   
                </bindings>
            </site>
```
3. 文件保存后，重新添加网站绑定即可。



