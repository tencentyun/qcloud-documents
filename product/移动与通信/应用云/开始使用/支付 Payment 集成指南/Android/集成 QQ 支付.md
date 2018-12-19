无论您是采用 gradle 远程依赖还是手动集成的方式来接入 Payment 服务，如果您需要接入 QQ 支付，那么您都必须手动添加 [mqqopenpay.jar](http://tac-android-libs-1253960454.file.myqcloud.com/jars/mqqopenpay.jar) 到您工程的 `libs` 目录。

> ** 注意：**
> 因为 `mqqopenpay.jar` 没有上传到 jcenter 仓库下，因此在 gradle 远程依赖的方式下我们暂时无法自动帮您添加。
