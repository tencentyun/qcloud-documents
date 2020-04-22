尊敬的腾讯云用户，您好！

CLB 配置访问日志到 COS 的功能将逐步下线，具体计划如下：
<table class="table"><thead><tr><th>时间</th><th>下线计划</th></tr></thead>
<tbody><tr><td>2020年4月26日 </td><td><strong>广州</strong>地域无法新增 CLB 访问日志到 COS，存量已配置的 COS 日志不受影响。</td></tr>
<tr><td>2020年5月15日 </td><td> <strong>北京、上海、香港、上海金融、深圳金融</strong>地域无法新增 CLB 访问日志到 COS，存量已配置的 COS 日志不受影响。 </td></tr>
<tr><td>2020年6月30日 </td><td> <strong>正式下线</strong>所有地域 CLB 配置访问日志到 COS 的功能，所有 CLB 不再提供该功能。 </td></tr></tbody></table>



CLB 配置访问日志到 COS 的升级版—— [配置访问日志到 CLS](https://cloud.tencent.com/document/product/214/41378) 已正式上线，相比于直接配置访问日志到 COS，配置访问日志到 CLS 可以提供：
- 分钟级粒度的实时日志，全文、键值、模糊关键字等多样化的在线检索。
- 多地域覆盖等能力，更加适合在生产环境大规模使用。

由于 COS 和 CLS 服务模式不同，我们无法帮您直接迁移，因此我们强烈建议您在2020年6月30日前将现有的 COS 日志迁移到 CLS 日志中，具体操作请参见 [配置访问日志到 CLS](https://cloud.tencent.com/document/product/214/41379) ，如有疑惑请参见 [常见问题 - 访问日志相关](https://cloud.tencent.com/document/product/214/43658)，对您造成的不便我们深感抱歉。

如您已经迁移，请忽略此通知，再次感谢您的理解与信任！

此致

腾讯云团队
