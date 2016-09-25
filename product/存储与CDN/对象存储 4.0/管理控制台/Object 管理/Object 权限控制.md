Object 访问权限提供了基于 Object 维度的访问权限控制，且该配置优先级高于 Bucket 权限。

通过修改 Object 访问权限，可以实现例如：在私有 Bucket 中设置个别允许公有访问的 Object，或在公有 Bucket 中设置个别需要鉴权才可以访问的 Object。Object 的权限有如下类型：

- 默认状态：任何一个新的 Object 被创建时，其不具备权限属性，则访问会跳过 Object 直接匹配 Bucket 的权限。

- 公有读私有写状态：当产生访问时，COS 会读取到 Object 的权限为公有读，此时无论 Bucket 为何种权限，Object 都可以被直接下载。

- 私有读写状态：当产生访问时，COS 会读取到 Object 权限为私有读写，此时无论 Bucket 为何种权限，Object 都需要通过[签名鉴权](/doc/api/435/6054)才可访问。

- 继承 Bucket 权限：在修改 Object 权限后，恢复其权限与 Bucket 一致。当产生访问时，COS 会读取到Object 权限为继承，转而再匹配 Bucket 的权限，来响应访问。

> 设置的Object权限只有通过直接访问域名（外网访问、内网访问）有效。对于使用 CDN 加速域名访问（形如 .file.myqcloud.com 或在 CDN 绑定了自定义域名）的访问，鉴权要求以 Bucket 权限为准。

假设在 APPID 为 1250000000 下创建了权限为**公有读私有写** Bucket 名称为 test，在 Bucket 根目录上传了Object a.txt。此时访问 `http://test-1250000000.cos.myqcloud.com/a.txt` 可以正常下载。

## 1. 私有读写

设置 a.txt 的 Object 访问权限为私有读写，尝试访问。

访问` http://test-1250000000.cos.myqcloud.com/a.txt `将返回 403 Forbidden，内容为 {"errorcode":-45086,"errormsg":"sign check fail"} 签名鉴权失败。在进行[签名](/doc/api/435/6054)后访问 `http://test-1250000000.cos.myqcloud.com/a.txt?sign=[签名字符串]` 可以正常访问。

## .2. 共有读私有写

设置 a.txt 的Object访问权限为公有读私有写，尝试访问。

访问 `http://test-1250000000.cos.myqcloud.com/a.txt` 可以正常下载。再一次修改 Bucket 属性，将 Bucket 权限设置为**私有读写**，尝试访问 `http://test-1250000000.cos.myqcloud.com/a.txt`，仍可正常下载。

## 3. 覆盖 Bucket 权限

修改 Bucket 权限设置为**私有读写**，设置 a.txt Object 访问权限为私有读写，尝试访问。

访问` http://test-1250000000.cos.myqcloud.com/a.txt` 返回 403 Forbidden，内容为 {"errorcode":-45086,"errormsg":"sign check fail"} 签名鉴权失败。在签名后访问 `http://test-1250000000.cos.myqcloud.com/a.txt?sign=[签名字符串]` 则可以正常访问。

此时，修改 Bucket 权限设置为**公有读私有写**，尝试访问 `http://test-1250000000.cos.myqcloud.com/a.txt` 返回 403 Forbidden，内容为 {"errorcode":-45086,"errormsg":"sign check fail"} 签名鉴权失败。在签名后访问 `http://test-1250000000.cos.myqcloud.com/a.txt?sign=[签名字符串]` 则可以正常访问。

