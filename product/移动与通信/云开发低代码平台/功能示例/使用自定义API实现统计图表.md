微搭中的统计组件有柱状图、折线图、饼状图及统计卡片等，这些组件除了使用数据源实现数据统计展示外，还可以使用自定义 API 对数据处理后实现统计展示。本文将使用自定义API对示例数据模型中的数据进行处理，然后实现柱状图、折线图、饼状图和统计卡片的展示。

## 示例数据模型及应用
创建名称为“统计示例数据”的数据模型，并通过后台**管理数据**添加演示数据。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/9dcdfc8c20f7ab2acc9c096b6da25114.png" />
这里添加了12个月的“销售”、“利润”、“成本”演示数据。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/05358f3d427ab08f9baa6cef1d65e666.png" />
创建示例应用，然后在应用中新建页面用于展示统计数据。

## 自定义 API 及方法
创建名称为“统计 API”的自定义 API，然后添加柱状图统计、曲线图统计、饼状图统计、卡片图统计等四个 APIs 方法。
![](https://qcloudimg.tencent-cloud.cn/raw/041a03db3b3cea31575fc04de965c8d4.png)

### 柱状图统计方法
柱状图统计方法的功能主要是查出“统计示例数据”数据模型中12个月的数据，然后计算出四个季度的“销售”、“利润”、“成本”数据，最后拼接成柱状图要求返回的数据格式。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/580f76a259641f7bd32b6efbd1724709.png" />
**代码如下：**
```javascript
module.exports = async function (params, context) {
  const respond = await context.callModel({
        dataSourceName: 'tjslsj_paye50s', // 数据模型名称
        methodName: 'wedaGetRecords', // 更新方法
        params: {
          pageSize:1000 // 很重要，默认查询10条，需要设置条数
        },
    });

  let array = respond.records;
  //处理数据，整理成每个季度
  jd_array = [];
  var xse = 0;
  var lr = 0;
  var cb = 0;
  for(var i = 0 ; i < array.length ; i++ ){
    if((i+1) % 3 != 0){
      xse = xse + array[i].xse;
      lr = lr + array[i].lr;
      cb = cb + array[i].cb;
    }else{
      var name = "第" + (((i+1) / 3).toString()) + "季度" ;
      xse = xse + array[i].xse;
      lr = lr + array[i].lr;
      cb = cb + array[i].cb;
      var v = {quarter:name, xse:xse, lr:lr , cb:cb};
      jd_array.push(v);
      xse = 0;
      lr = 0;
      cb = 0; 
    }
  }

 //拼接统计格式参数
  let jsonData = [];
  jd_array.forEach(item =>{
    var v = { XLabel:{Value:item.quarter},
    YLabels:[
      {Name: "销售额", Value:item.xse},
      {Name: "利润", Value:item.lr},
      {Name: "成本", Value:item.cb},
    ]}; 
    jsonData.push(v);
  });
  return {result:jsonData};
}

```

**这里需要注意的是自定义方法的返回参数格式必须按照要求配置**。方法出参可以使用**添加出参**进行配置，也可以在**方法测试**中运行测试方法，待测试成功后使用**出参映射**进行配置。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/b66026fd67a7a23842e009cfe0eaf58e.png" />

### 折线图统计方法
折线图统计方法的功能主要是查出“统计示例数据”数据模型中12个月的数据，最后拼接成折线图要求返回的数据格式。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/1cc5a66dbd3192fa188502375287ac5f.png" />
**代码如下：**
```javascript
module.exports = async function (params, context) {
  const respond = await context.callModel({
        dataSourceName: 'tjslsj_paye50s', // 数据模型名称
        methodName: 'wedaGetRecords', // 更新方法
        params: {
          pageSize:1000 // 很重要，默认查询10条，需要设置条数
        },
    });

  let array = respond.records;

 //拼接统计格式参数
  let jsonData = [];
  array.forEach(item =>{
    var v = { XLabel:{Value:item.yd},
    YLabels:[
      {Name: "销售额", Value:item.xse},
      {Name: "利润", Value:item.lr},
      {Name: "成本", Value:item.cb},
    ]}; 
    jsonData.push(v);
  });
  return {result:jsonData};
}
```

### 饼状图统计方法
饼状图统计方法的功能主要是查出“统计示例数据”数据模型中12个月的数据，然后计算出全年的“销售”、“利润”、“成本”数据，最后拼接成饼状图要求返回的数据格式。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/fe3a52299d7d6e984dedcc36457801a5.png" />
**代码如下：**
```javascript
module.exports = async function (params, context) {
  const respond = await context.callModel({
        dataSourceName: 'tjslsj_paye50s', // 数据模型名称
        methodName: 'wedaGetRecords', // 更新方法
        params: {
          pageSize:1000 // 很重要，默认查询10条，需要设置条数
        },
    });

  let array = respond.records;
  //处理数据，统计12个月销售额度、利润、成本
  var total_xse = 0;
  var total_lr = 0;
  var total_cb = 0;
  array.forEach(item =>{
    total_xse = total_xse + item.xse;
    total_lr = total_lr + item.lr;
    total_cb = total_cb + item.cb
  })

 //拼接统计格式参数
  let jsonData = [
    { XLabel:{Value:"销售额"},
    YLabels:[
      {Name: "金额", Value:total_xse}
    ]}, 
    { XLabel:{Value:"利润"},
    YLabels:[
      {Name: "金额", Value:total_lr}
    ]}, 
    { XLabel:{Value:"成本"},
    YLabels:[
      {Name: "金额", Value:total_cb}
    ]}, 
  ];
  return {result:jsonData};
}
```

### 卡片图统计方法
卡片图统计方法的功能主要是查出“统计示例数据”数据模型中12个月的数据，然后计算出全年的“销售”数据，最后拼接成卡片图要求返回的数据格式。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/2d21125c12379006fda0fb655c50e42a.png" />

**代码如下：**
```javascript
module.exports = async function (params, context) {
  const respond = await context.callModel({
        dataSourceName: 'tjslsj_paye50s', // 数据模型名称
        methodName: 'wedaGetRecords', // 更新方法
        params: {
          pageSize:1000 // 很重要，默认查询10条，需要设置条数
        },
    });

  let array = respond.records;
  //处理数据
  //处理数据，统计12个月销售额度
  var total_xse = 0;

  array.forEach(item =>{
    total_xse = total_xse + item.xse;
  })
 //拼接统计格式
  let jsonData = [
    { Name:"销售额", Value:total_xse }, 
  ];
  
  return {result:jsonData};
}
```

## 统计图表展示配置
在统计页面分别添加柱状图、折线图、饼状图、统计卡片组件，在各种组件的属性中配置数据源。
### 柱状图配置
拖拽柱状图组件，在属性区域中**数据源**选择**自定义 APIs**，**自定义 APIs** 选择**统计 API**，**调用方法**选择**柱状图统计**，其它属性根据需求自行设置。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/847c2e39ac3e6fe0ad66643bfdd10733.png" />

### 折线图配置
拖拽折线图组件，在属性区域中**数据源**选择**自定义 APIs**，**自定义 APIs** 选择**统计 API**，**调用方法**选择**折线图统计**，其它属性根据需求自行设置。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7a4410ddca6f64b79a8dccdca0b8fddf.png" />

### 饼状图配置
拖拽饼状图组件，在属性区域中**数据源**选择**自定义 APIs**，**自定义 APIs** 选择**统计 API**，**调用方法**选择**饼状图统计**，其它属性根据需求自行设置。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/f1b6f6733d705d49f11bc53fd080e3b0.png" />

### 卡片图配置
拖拽统计卡片组件，在属性区域中**数据源**选择**统计 API 或卡片图统计**”，其它属性根据需求自行设置。
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/44b28aafcf352e8c10fa14f3e7fb6543.png" />
