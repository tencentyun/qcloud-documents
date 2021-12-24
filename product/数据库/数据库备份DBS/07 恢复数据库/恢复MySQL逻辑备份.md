## 操作场景
本场景用于介绍恢复 MySQL 逻辑备份到腾讯云 MySQL 数据库中。

## 操作步骤
1. 登录 [DBS 控制台](https://console.cloud.tencent.com/dbs)，在左侧导航选择**备份计划**页，进入备份计划页。
2. 选择指定的备份计划，单击任务 ID 或者在**操作**列单击**查看**，进入基本信息页面。
![](https://qcloudimg.tencent-cloud.cn/raw/53cda8a2928d1967a31f7fa654eb5e45.png)
3. 切换页签，单击**恢复数据库**，然后单击**恢复数据库**。
![](https://qcloudimg.tencent-cloud.cn/raw/f0b022c36c3f15efac879d0c3e25492c.png)
4. 在**配置恢复任务**页面中，配置恢复时间点，配置完成后单击**测试连通性**，通过后单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/22fa75b71e695c248400ba10967c92ff.png)
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
<td>可以恢复数据的时间范围，DBS 根据已有的备份数据情况，提供最大范围的可恢复范围。</td></tr>
<tr>
<td>恢复日期</td>
<td>选择需要恢复的日期。</td></tr>
<tr>
<td>恢复时间点</td>
<td>选择需要恢复的时间点。</td></tr>
<tr>
<td rowspan=7>恢复目标数据库</td>
<td>目标库类型</td><td>选择“MySQL”。</td></tr>
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
<td>密码</td><td>目标数据库帐号的密码。</td></tr></tbody></table>
5. 在**配置恢复任务**页面中，配置恢复对象，完成后单击**下一步**。
   对于库、表等可能同名发生冲突的情况，可选择不同的冲突策略：
   - 遇到同名对象则失败：恢复任务过程中，如果恢复的数据与目标库中的对象（库、表等）同名，则恢复任务失败。
   - 遇到同名对象则重命名：恢复任务过程中，如果恢复的数据与目标库中的对象（库、表等）同名，则对恢复的数据进行重命名。
![](https://qcloudimg.tencent-cloud.cn/raw/c5a916c52405fdcac627b181f145cdef.png)
6. 在**配置恢复任务**页面中，进行任务预检查，预检查通过单击**启动任务**。
![](https://qcloudimg.tencent-cloud.cn/raw/cfc30be063235273d699bf9cb4b057c7.png)
7. 返回**恢复数据库**页签，查看恢复任务，任务正在运行中。
![](https://qcloudimg.tencent-cloud.cn/raw/bbadfee21ebc5fc357473519032a791d.png)
