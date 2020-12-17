尊敬的腾讯云用户，您好！

CLB 配置访问日志到 COS 的功能将逐步下线，具体计划如下：
<table class="table"><thead><tr><th>时间</th><th>下线计划</th></tr></thead>
<tbody><tr><td>2020-04-26 00:00:00 </td><td><strong>广州</strong>地域无法<strong>新增配置</strong>访问日志到 COS，存量已配置的 COS 日志不受影响。</td></tr>
<tr><td>2020-05-15 00:00:00 </td><td> <strong>北京、上海、香港、上海金融、深圳金融</strong>地域无法<strong>新增配置</strong>访问日志到 COS，存量已配置的 COS 日志不受影响。 </td></tr>
<tr><td>2020-06-30 00:00:00 </td><td> <strong>正式下线所有地域 CLB 配置访问日志到 COS 的功能，所有 CLB 不再提供该功能。</strong> </td></tr></tbody></table>



CLB 配置访问日志到 COS 的升级版 —— [配置访问日志到 CLS](https://cloud.tencent.com/document/product/214/41378) 已正式上线，相较于配置访问日志到 COS，配置访问日志到 CLS 可以提供：
- 分钟级粒度的实时日志，全文、键值、模糊关键字等多样化的在线检索。
- 多地域覆盖等能力，更加适合在生产环境大规模使用。
- 使用 CLS 方案后，可以按需[从 CLS 投递到 COS ](https://cloud.tencent.com/document/product/614/37908)。

由于 COS 和 CLS 服务模式不同，我们无法帮您直接修改配置，因此我们建议您在2020-06-30 00:00:00前，将现有的配置访问日志到 COS 改为配置到 CLS 中，请先 [配置访问日志到 CLS](https://cloud.tencent.com/document/product/214/41379) 后，关闭 [配置访问日志到 COS ](https://cloud.tencent.com/document/product/214/10329#.E5.85.B3.E9.97.AD.E8.AE.BF.E9.97.AE.E6.97.A5.E5.BF.97.E5.AD.98.E5.85.A5-cos) 即可。

腾讯云默认情况下不承诺存储访问日志，如有业务需要请自行 [配置访问日志到 CLS](https://cloud.tencent.com/document/product/214/41379) ，对您造成的不便我们深感抱歉。

如您已经修改配置，请忽略此通知，再次感谢您的理解与信任！

此致

腾讯云团队
