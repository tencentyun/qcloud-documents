
### IIS 下设置 https 主机名灰色无法编辑怎么办？
使用 https，主机名变成灰色无法编辑。

####  解决办法
1. 在 IIS 设置中，选择 https，选择相应的 SSL 证书，单击【确定】。
2. 打开 `C:\Windows\system32\inetsrv\config\applicationHost.config`。
3. 修改内容如下：
>?
>- 以 “cloud.com” 域名为例。
>- 将 `<binding protocol="https" bindingInformation="*:443:" />` 修改为
 `<binding protocol="https" bindingInformation="*:443:cloud.com" />`。
>- 文件无法直接修改时，可以尝试使用管理员权限进行修改或复制文件到桌面修改后，进行替换。
>
```
<site name="example.cloud.com" id="8">
                <application path="/">
                    <virtualDirectory path="/" physicalPath="D:\web\cloud" />
                </application>
                <bindings>
                    <binding protocol="http" bindingInformation="*:80:example.cloud.com" />
                    <binding protocol="http" bindingInformation="*:80:www.cloud.com" />
                    <binding protocol="https" bindingInformation="*:443:" />   
                </bindings>
            </site>
```

