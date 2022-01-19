## **适用场景**

对象间N:N的数据创建，解决多对多的关系存储以及展示

## **关键字**

<font color ="#0abf5b">多对多&nbsp;&nbsp;</font>
<font color ="#ff7200">关联选择器&nbsp;&nbsp;</font>
<font color ="#e54545">对象建模&nbsp;&nbsp;</font>

## **案例介绍**

在学校管理系统中，学生和课程属于多对多关系，1个学生可以选修多门课程，1个课程可以被多个学生选修。

## **实施步骤**

### **设计态配置**

1.创建对象关系表「学生课程关系表」

>     提示：关系表中维护了学生和课程的绑定关系

![img](https://qcloudimg.tencent-cloud.cn/raw/e70d03eaa6279c90385e25e5b3abae44.png)

2.创建课程管理页面，完成课程的增删改查等（此步省略）

3.创建新增学生页面

>     提示：这里我们使用关联选择器组件，属性配置如下：
>          ① 设置选择类型为：多选
>          ② 设置选择对象为：学生课程关系表（此处会拉取存储学生对象为关联关系的对象集合）
>          ③ 选择字段：课程（学生课程关系表）
>          ④ 选择展示字段：课程名称（课程表）

![img](https://qcloudimg.tencent-cloud.cn/raw/e853c303aaa537a0581f95455c3b506c.png)

4.创建学生列表页面

>     提示：这里我们对表格组件进行配置，配置属性如下：
>
>          数据源为数据库
>          设置选择对象为：学生
>          新建列：点击如图1中按钮，列名设置为学生课程
>          数据源：点击如图2中按钮，在选择字段中勾选展示关联子对象后，选择学生课程关系表对象中的子对象“课程”，在右侧子对象字段选择框中选择“课程名称”

![img](https://qcloudimg.tencent-cloud.cn/raw/6e08bf4ab8cf7a4032007fd1e921fcd8.png)

>         展示关联子对象：即展示当前对象的下级子对象，可选择子对象中的字段，如果子对象中的字段为关联字段，则可以在右侧选择关联对象的具体字段。

![img](https://qcloudimg.tencent-cloud.cn/raw/17aa8d576c6f61c71671c871884dbb90.png)

### 运行态效果

1.创建学生对象，选择课程信息

![img](https://qcloudimg.tencent-cloud.cn/raw/10e0d8d059b5f20be9bd1d6c0aa5ce1e.png)

2.查看学生列表详情，实现学生与课程多对多展示。

![img](https://qcloudimg.tencent-cloud.cn/raw/93504952b27594556de83c36d38a0d54.png)

3.点击查看操作，进入学生信息详情页面。

![img](https://qcloudimg.tencent-cloud.cn/raw/fdebf5593fbca2309fd113225dce21b7.png)