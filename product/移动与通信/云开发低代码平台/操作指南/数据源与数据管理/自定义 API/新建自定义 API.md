腾讯云微搭低代码自定义 API 支持调用第三方服务接口或使用代码来实现自定义业务逻辑。本文将介绍如何创建自定义 API 。

## 操作步骤
### 步骤1：填写基础信息
进入**微搭控制台** > **[自定义 API ](https://console.cloud.tencent.com/lowcode/datasource/custom-connector)** 页面，单击**新建自定义 API**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/6b51b3692c4d6945123889f16c52de2f.png" style="width:80%">

>!标识为自定义 API 的唯一标识，在微搭应用编辑器、自定义代码中均需要借助这个标识来使用。


### 步骤2：选择创建方式

创建方式分为两种：

- **从空白创建** ：创建一个不包含任何方法的自定义 API 。
- **Postman**：通过 Postman 导出的 Collection v2.1 文件, 生成包含对应 HTTP 方法的自定义 API 。

### 步骤3：实现 API 方法
目前自定义 API 支持三种方式来实现自定义业务逻辑：

- **HTTP 请求**：使用 HTTP 方式调用外部服务，通过简单的配置 HTTP 请求地址、方法、参数等即可完成方法的配置。
- **自定义代码**：集成了常用 NPM 包、数据模型、 API 等 API，只支持 JS 开发语言，可以用来实现自定义业务逻辑，具体参见 [自定义代码](https://cloud.tencent.com/document/product/1301/68440)。
- **云开发云函数**：用户可以创建和使用云开发的云函数来实现完整的服务端功能，并通过自定义 API 的方法绑定并调用。

<img src="https://qcloudimg.tencent-cloud.cn/raw/11208fdde5979120bf674046009a431e.png" width="800px">


开发者可以根据业务需求使用 **HTTP 请求**、**自定义代码** 或 **云开发云函数** 方式实现自定义 API 方法，下面只展示使用 **自定义代码** 实现方法的示例：

#### 外部 HTTP 服务 [](id:http)

若开发者有第三方服务可以通过 HTTP 调用，我们可以按照下列示例使用：
<dx-codeblock>
:::  js
const fetch = require('node-fetch');

module.exports = async function (params, context) {
  const response = await fetch(`https://reqres.in/api/users?page=${params.pageNo}`);
  const result = await response.json();

	// 这里的返回需要和出参结构对应
  return {
    pageNo: result.page,
    pageSize: result.per_page,
    total: result.total,
    records: result.data.map(d => ({
      _id: d.id,
      ...d,
    })),
  };
};
:::
</dx-codeblock>


#### 外部数据库 [](id:db)

若开发者有自己的数据库（腾讯云或自有数据库），可以使用 **云开发云函数** 来实现数据库连接和读写，以下是云函数示例：
<dx-codeblock>
:::  js
const mysql = require("mysql2/promise");
exports.main = async (event, context) => {
    try {
        const connection = await mysql.createConnection({
            host: process.env.HOST,
            user: process.env.USERNAME,
            password: process.env.PASSWORD,
            port: process.env.PORT,
            database: process.env.DB,
        });
        console.log('已连接')
        const [rows, fields] = await connection.execute('SELECT * FROM `weda_model_example`;');
				// 这里可以对返回数据做加工
        return rows;
    } catch(err) {
        console.log('错误连接', err);
        return err;
    }
};
:::
</dx-codeblock>
然后在自定义代码调用上述云函数：
<dx-codeblock>
:::  js
module.exports = async function (params, context) {
  const result = await context.app.callFunction({
    name: '云开发云函数名称',
    data: {}, // 方法入参
  });

  // 在这里返回这个方法的结果，需要与出参定义的结构映射
  return {
    _id: 123456
  };
};
:::
</dx-codeblock>
<dx-alert infotype="notice" title="">
只能调用与微搭相同云开发环境中的云函数。
</dx-alert>


#### 云开发数据库

若开发者想自己实现 DB 读写逻辑，可以通过下列方式直接操作数据库：
<dx-codeblock>
:::  js
module.exports = async function (params, context) {
  const result = await context.database.collection('数据库集合名称').get();

  // 在这里返回这个方法的结果，需要与出参定义的结构映射
  return {
    _id: 123456
  };
};
:::
</dx-codeblock>

<dx-alert infotype="notice" title="">
只能调用与微搭相同云开发环境中的数据库。其他更多能力请参见 [自定义代码](https://cloud.tencent.com/document/product/1301/68440)。
</dx-alert>






### 步骤4：启用方法
最后请勾选方法以启用已经实现的方法。
