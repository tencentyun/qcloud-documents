## 基本信息

脚本基于 JavaScript 语言进行封装，数据在 context 中进行传输，需以 return context 进行退出。



## context 数据结构

```JSON
{
    "data" : {
        "name" : "张三"
    },
    "operationType" : "CREATE"
}
```

## 函数说明

| 函数 | 功能 | 
|---------|---------|
| repo.executeUpdate() | 执行更新操作。|
| repo.executeCreate() | 执行创建操作。 | 
| repo.executeDelete() | 执行删除操作。 | 
| repo.executeDisable() | 执行停用操作。 | 
| repo.getObjectByID("ID") | 获取该 ID 对应的数据对象（同应用内）。 | 
| repo.abort("operationType") | 放弃执行 {operationType} 操作。<br>operationType 的值可以取 "CREATE"、"UPDATE"、"DELETE"、 "DISABLE"。不填默认放弃执行所有操作。 | 



## 示例

```JavaScript
//获取到该人员的部门的部门名
repo.getObjectByID(context.data.DeptID).name

// 如果人员的雇佣日期在今天之前，创建人员
if (context.data.hiredate - today() <= 0) {
    repo.executeCreate();
    return context;
}

// 如果人员的邮箱包含tencent，不进行更新操作
if (context.data.email.contain("tencent")) {
    repo.abort("UPDATE");
    return context;
}
```
