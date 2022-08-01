
## 操作场景
本章节介绍恢复逻辑备份到腾讯云 MariaDB 的操作指导，因为如下场景的操作和要求类似，本章节仅选取 MariaDB 逻辑备份恢复到腾讯云 MariaDB 作为示例。

- MariaDB 逻辑备份恢复到腾讯云 MariaDB（示例）
- MySQL 逻辑备份恢复到腾讯云 MariaDB
- Percona 逻辑备份恢复到腾讯云 MariaDB
>? 恢复到腾讯云 MariaDB 时，要求恢复的对象必须有主键，或者有非空唯一键，否则校验不通过，恢复任务报错。

## 前提条件
- 恢复目标数据库符合备份功能和版本要求，请参见 [备份和恢复能力汇总](https://cloud.tencent.com/document/product/1513/64026) 进行核对。
- 恢复账号需要具备目标数据库的如下对应权限。
  ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE USER, CREATE VIEW, DELETE, DROP, EVENT, EXECUTE, INDEX, INSERT, LOCK TABLES, PROCESS, REFERENCES, RELOAD, SELECT, SHOW DATABASES, SHOW VIEW, TRIGGER, UPDATE。
- 恢复任务过程中，DBS 会使用恢复任务的账号在目标库中写入系统库 `__tencentdb__`，用于记录恢复任务过程中的元数据信息，因此需要对目标数据库授权 `__tencentdb__` 的全部权限。
  - 为保证后续问题可定位，恢复任务结束后不会删除目标库中的`__tencentdb__`。
  - `__tencentdb__`系统库占用空间非常小，约为目标库恢复存储的千分之一到万分之一（例如恢复到目标库存储为50G，则`__tencentdb__`系统库约为 5K-50K） ，并且采用单线程，等待连接机制，所以对目标库的性能几乎无影响，也不会抢占资源。

## 操作步骤
1. 登录 [DBS 控制台](https://console.cloud.tencent.com/dbs)，在左侧导航选择**备份计划**页，进入备份计划页。
2. 选择指定的备份计划，单击任务 ID 或者在**操作**列单击**查看**，进入基本信息页面。
3. 切换**恢复数据库**页签，然后单击**恢复数据库**。
![](https://qcloudimg.tencent-cloud.cn/raw/f0b022c36c3f15efac879d0c3e25492c.png)
4. 在**配置恢复时间点**页面中，配置数据库恢复的时间点，完成后单击**测试连通性**，通过后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/4072e51dd0f920821955c3e662b2bb7c.png)
  <table>
  <thead><tr><th width="10%">设置类型</th><th width="20%">配置项</th><th width="70%">说明</th></tr></thead>
  <tbody>
  <tr>
  <td>任务设置</td>
  <td>任务名称</td>
  <td>设置一个具有业务意义的名称，便于识别。</td></tr>
  <tr>
  <td rowspan=3>恢复时间点</td>
  <td>可恢复的时间范围</td>
  <td>DBS 根据已有的备份数据情况，提供最大范围的可恢复范围，可恢复的起点为最早一次全量备份的结束时间，可恢复的终点为增量备份的结束时间。</td></tr>
  <tr>
  <td>恢复日期</td>
  <td>选择需要恢复的日期。</td></tr>
  <tr>
  <td>恢复时间点</td>
  <td>蓝色时间轴为可选择的恢复时间范围，挪动时间轴上的白色按钮选择一个恢复时间点。</td></tr>
  <tr>
  <td rowspan=9>恢复目标数据库</td>
  <td>目标库类型</td><td>根据您的情况选择，此处选择“MariaDB”。</td></tr>
  <tr>
  <td>接入类型</td><td>选择“云数据库”。
  </td></tr>
  <tr>
  <td>所属地域</td><td>备份计划中的地域，该地域为备份数据存储和恢复所在的地域。</td></tr> 
  <tr>
  <td>数据库实例</td><td>恢复到目标数据库实例的 ID。</td></tr>
  <tr>
  <td>帐号</td><td>目标数据库帐号。</td></tr>
  <tr>
  <td>密码</td><td>目标数据库帐号的密码。</td></tr>
  <tr>
  <td>连接方式</td><td><ul><li>非加密方式：DBS 与源数据库的连接不加密。</li><li>SSL 安全连接：DBS 与源数据库通过 SSL（Secure socket layer）安全连接，对传输链路进行加密。</li></ul><dx-alert infotype="explain" title="说明">选择 SSL 安全连接可能会增加源库的连接响应时间，一般腾讯云内网链路相对较安全，无需开启 SSL 安全连接，采用公网/专线等传输方式，并且对数据安全要求较高的场景，需要开启 SSL 安全连接。<br>选择<b> SSL 安全连接</b> 前，请先在源数据库中开启 SSL 加密。如果源库为腾讯云数据库，请参考 <a href="https://cloud.tencent.com/document/product/237/33944">开启 SSL 加密</a>。</dx-alert></td></tr>
  <tr>
  <td>CA 根证书</td><td>可选，上传 CA 证书后，DBS 会校验传输目标服务器的身份，使传输链路更加安全。</td></tr></tbody></table>
5. 在**配置恢复对象**页面中，选择恢复冲突选项和恢复对象，完成后单击**下一步**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/430444bf0116d82df641078b4b233a26.png" style="zoom:25%;" />
<table>
<thead><tr><th>配置项</th><th>说明</th></tr></thead>
<tbody><tr>
<td>冲突处理</td>
<td>对于库、表等可能同名发生冲突的情况，可选择不同的冲突策略。<ul><li>遇到同名对象则失败：恢复任务过程中，如果恢复的数据与目标库中的对象（库、表等）同名，则恢复任务失败。</li><li>遇到同名对象则重命名：恢复任务过程中，如果恢复的数据与目标库中的对象（库、表等）同名，则对恢复的数据进行重命名。</li></ul></td></tr>
<tr>
<td>恢复对象</td>
<td><ul><li>如果<strong>备份任务</strong>选择<strong>整个实例</strong>备份，同时开启了增量备份，那么源库中新增的对象，会同步到备份集中，<strong>恢复任务可以选择新增的对象</strong>（新增库表的时间需要在备份任务结束之前）。</li><li>如果<strong>备份任务</strong>选择<strong>指定对象</strong>，也开启了增量备份，源库新增的对象不会同步到备份集中，所以<strong>恢复任务</strong>也<strong>不能选择新增的对象</strong>。</li></ul></td></tr>
</tbody></table>
6. 在**预检查**页面中，进行任务预检查，待检查通过单击**启动任务**。
![](https://qcloudimg.tencent-cloud.cn/raw/e1db92711588e5517e01465e90f988d7.png)
7. 返回**恢复数据库**页签，查看恢复任务进度。
