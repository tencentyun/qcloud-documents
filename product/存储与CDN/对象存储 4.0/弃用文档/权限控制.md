腾讯云 Bucket 默认支持两种访问权限：公有读私有写和私有读写

- 公有读私有写：任何人（包括匿名访问者）都对可以读取该 Bucket 中的文件，但只有 Bucket 创建者及有相应权限的账号才对该 Bucket 中的文件有写权限，具有权限的相关帐号进行写操作时均需要进行[鉴权](/doc/api/264/5993)。
- 私有读写：只有该 Bucket 的创建者及有相应权限的账号才对该 Bucket 中的文件有读写权限，其他任何人对该 Bucket 中的文件都没有读写权限；具有权限的相关帐号进行读写操作时均需要进行[鉴权](/doc/api/264/5993)。

用户可以通过控制台和 API 来修改 Bucket 访问权限

除了在创建时对 Bucket 的访问权限进行选择外，还可以随时对 Bucket 的权限进行修改。进入 COS 管理控制台，点击需要修改权限的 Bucket。进入到 Bucket 后，点击 **基础配置** ：

![](https://mc.qcloudimg.com/static/img/e2532927eb0ba207eb7838fe76e39797/image.png)

找到 **访问权限** ，点击 **编辑** 按钮 修改 Bucket 的访问权限：

![](https://mc.qcloudimg.com/static/img/2c6e7ac571068ac9a332a1eaac81ccad/image.png)


