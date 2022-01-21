## 适用场景

页面按钮触发的流程需要对数据进行批量新增/更新

## 关键字

<font color ="#0abf5b">批量创建/更新&nbsp;&nbsp;</font>
<font color ="#ff7200">iPaaS</font>

## 案例介绍

在学校管理系统中，录入学生基础信息后，需要对所有学生分别注册校园一卡通，并对休学或退学学生冻结或注销校园一卡通

## 实施步骤

### 设计态配置

1.对象模型如下

> 通用选项集
> <img src="https://qcloudimg.tencent-cloud.cn/raw/a515017259acd9049de7fcead13f6e18.jpg"></img>
> 对象模型
> ![img](https://qcloudimg.tencent-cloud.cn/raw/24dbeeed3d7b52ffe6c6980f7f8bee27.png)
2.使用从对象创建页面快速创建出列表页面，拖入开通一卡通按钮，并将点击条件设为选中记录，以便对数据进行批量操作

> <img src="https://qcloudimg.tencent-cloud.cn/raw/608dec426aa8110921f6ae37dbfa4890.png"></img>
> 将开通一卡通按钮绑定为触发开通校园卡流程
> <img src="https://qcloudimg.tencent-cloud.cn/raw/cb27f3ebef7a9db7230e86f849fa7296.png"></img>
3.流程中设置调用接口节点，并将请求地址设置为iPaaS网关地址，设置请求参数为选中的学生记录

> 设置请求地址
> <img src="https://qcloudimg.tencent-cloud.cn/raw/0cb9c09002dad80a272361d4db50575c.png"></img>
> 设置请求参数
> <img src="https://qcloudimg.tencent-cloud.cn/raw/d24967f52447c590b9435c22a3ff8a77.png"></img>
4.在对应的iPaaS继承流中，添加神笔连接器节点

> <img src="https://qcloudimg.tencent-cloud.cn/raw/0b4ca1c2725b481a262db4cce731da26.png"></img>
> 此处我们选择在业务数据管理分类中的批量创建业务数据
> <img src="https://qcloudimg.tencent-cloud.cn/raw/daafa421de7150b4dd9e42abb4004985.png"></img>
> 此处的应用code和对象key可以在神笔设计态进行查询
> <img src="https://qcloudimg.tencent-cloud.cn/raw/3f259f3ac01113ca4a689bcc8f285e32.png"></img>
> 对象code
> <img src="https://qcloudimg.tencent-cloud.cn/raw/0cfad183f2473c2f19129d1b94b84317.png"></img>
> 应用code
> <img src="https://qcloudimg.tencent-cloud.cn/raw/85dd3cae4da16437566a4c24afd25373.png"></img>
5.配置神笔连接器AK/SK

> 此处我们新建连接器配置
> <img src="https://qcloudimg.tencent-cloud.cn/raw/364d2cf7c4340188ea4e46cbda31f9d8.png"></img>
> ak/sk由神笔为每个租户生成，首次开通时可以向神笔提出开通openAPI申请
> <img src="https://qcloudimg.tencent-cloud.cn/raw/dd78011c4f560d3458428594bd19eab1.png"></img>
6.设置写入数据

> 这里我们使用低代码的方式写入数据
> <img src="https://qcloudimg.tencent-cloud.cn/raw/64fd0148940b86bbbc0922adc0c484bc.png"></img>
> 字段key列表返回需要写入的字段，字段指对象字段的api_key
``` python
    def dw_process(msg):
        #studentInfo 学生信息
        #openTime 开通时间
        #amount 余额
        #status 开通状态
        return ['studentInfo', 'openTime', 'amount', 'status']
```

> 字段值列表值需要写入的数据内容，数据的顺序需要与字段的顺序保持一致
``` python
    def dw_process(msg):
        #从iPaaS中取出神笔传入的学生记录
        payload = msg.vars.get('rootMessage').payload
        studentRecords = payload['studentRecords']
        #创建返回结果集
        res = []
        for record in studentRecords:
            #填充结果集
            res.append([
                #学生对象的业务ID
                record['studentID'],
                #当前时间戳
                int(round(time.time()*1000)),
                #余额为0
                0,
                #状态为正常
                ['正常']
            ])
        return res
```

7.批量更新操作同上，只需要更换连接器为批量更新业务数据即可。更多iPaaS调试等技巧请参考iPaaS使用文档(https://cloud.tencent.com/document/product/1359/58599)
