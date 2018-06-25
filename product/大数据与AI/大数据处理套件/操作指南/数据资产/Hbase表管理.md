## 搜索 hbase 表
在库表管理左侧标签页中单击【Hbase 的库表】进入 hbase 表管理的单独页面，可以通过表名称搜索表。
![hbase](//mc.qcloudimg.com/static/img/e757c8a756dff984941a0f5a2d10e2bd/image.png)
## 新建 hbase 表
单击【库表管理】标签页右上角的【新建表】，填写配置信息，单击【提交】。
- 表名：以命名空间：表名称构成，如果不填写命名空间，默认为 default，普通用户没有权限在该命名空间中建表；需要在库表管理新建库表时，创建属于当前用户的 hbase 命名空间。
- 列族：可以添加多个，并且可以设置对应列族的属性。
![创建新表](//mc.qcloudimg.com/static/img/abef9e7e4ab3a7def1bdd187b9ac7580/image.png)
## 查看 hbase 表
新建 hbase 表完成后即可在页面中看到当前创建的表，也可以搜索 ns_demo 这个命名空间的表查询。
![查询](//mc.qcloudimg.com/static/img/6038e381a5544842597621b67dad7d8d/image.png)
## hbase 表操作
对有权限的表可以进行启用、禁用和丢弃操作。
启用（enable）操作：在库表列表选中要启用的列表，单击【启动】按钮。
![启用](//mc.qcloudimg.com/static/img/6549eaede7e37fac0e36f97791896243/image.png)
禁用（disable）操作：在库表列表选中要启用的列表，单击【禁用】按钮。
![禁用](//mc.qcloudimg.com/static/img/a1a80d58b22181121c04e7377e972478/image.png)
丢弃（delete）操作：在库表列表选中要启用的列表，单击【丢弃】按钮。
![丢弃](//mc.qcloudimg.com/static/img/eedfdd0d8d7615d88f54fb617b0c2e20/image.png)
## 查看 hbase 表数据
单击表名称后，进入新页面可以看到当前表中的数据，并提供表数据查询、过滤、排序展示等功能。如下图所示：
![查看数据](//mc.qcloudimg.com/static/img/5df12b315ace27c30241594b9b402ec5/image.png)
## hbase 表数据操作
### 创建新行
单击【新建行】，添加行键、字段以及对应的值。
- 行键：rowkey，hbase 行唯一 ID。
- 字段：按照列族：列字段命名填写对应的 value 值即可。
![新建行](//mc.qcloudimg.com/static/img/bb21434ce0afa3e2757a809ca23d3fc2/image.png)
提交后可以看到表中的数据如下：
![新行结果](//mc.qcloudimg.com/static/img/20a3d18b0386a8be71dfb83e51c993d9/image.png)
### 创建新列
![创建新列](//mc.qcloudimg.com/static/img/9f6632e5f59e582f85b57e7b727d2789/image.png)
![创建新列](//mc.qcloudimg.com/static/img/21368cc4e70f14fd654ffae02c322cbf/image.png)
![新列结果](//mc.qcloudimg.com/static/img/21368cc4e70f14fd654ffae02c322cbf/image.png)
### 删除行
![删除行](//mc.qcloudimg.com/static/img/1c2097eddda134951444e4db62f11931/image.png)
### 删除列
![删除列](//mc.qcloudimg.com/static/img/a423a9bd2da7ff959bbdcaf6c103033b/image.png)
![确认删除列](//mc.qcloudimg.com/static/img/d40ef3f4830de8155a0e5185f9d983cb/image.png)
### 修改行数据
![修改行数据](//mc.qcloudimg.com/static/img/98b70d30bab84addadd31077f12bade2/image.png)
### 批量上传数据
![批量上传](//mc.qcloudimg.com/static/img/5e7953ab1bf53dbfa8479ce9db4b61e3/image.png)
csv文件示例：
![csv示例](//mc.qcloudimg.com/static/img/b7dc32a5947ffb5e4d40a1dfdbfacf8f/image.png)
上传选择该文件，即可查看到当前表中的数据如下：
![最终结果](//mc.qcloudimg.com/static/img/8a4bf547d0c2b8ae42d12d9018dafabe/image.png)
