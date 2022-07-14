<style>
table th:nth-of-type(1) {
width: 40%        
}
</style>

EntityService 对象模型服务作用于特定的对象模型上的前端服务。

## 使用指引

在 Apaas 模型中，对象模型的标识分为 apiKey 和 code。apiKey 是开发者自定义的标识，code 是系统默认生成的。一般我们使用 apiKey 保持一定的可读性。以用户对象为例，apiKey 为 `user`，code为 `10000`。

### 原生获取

``` ts
const entityService = SDK.getEntityService('user');
```

### React Hooks 中获取

`useEntityService` 的作用与 `getEntityService` 相同，但是 `useEntityService` 对 React Hooks 的调用方式做了优化，更节省性能。

``` ts
function HelloWorld () {
  const entityService = SDK.useEntityService('user');

  return <div></div>;
}
```

## API 参考

### getRecordById

**功能：**根据 recordId 获取单条数据记录。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} recordId`  | 记录 ID |
| `options`  | 参数配置 | 

**返回值**

|参数名 | 参数说明 | 
|---------|---------|
| `{Promise<EntityHttpResponse<RecordData>>}` | 返回一条数据记录 |
 
**示例**
``` ts
type EntityHttpResponse<T> = {
  data: T;
}

type RecordData = {
  entityCode: string; // 对象编码code
  entityApiKey: string; // 对象apiKey
  mainField: string; // 主字段值
  recordId: string; // 数据记录ID
  fieldValueMap?: Record<string, any>;
  fieldValueMapWithCode?: Record<string, any>;
}
```

### getRecordsByFilter

**功能：**根据筛选条件获取多条数据。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{GetRecordByFilterRequestParams} params`  | 查询数据请求参数 | 

**示例**
``` ts
type GetRecordByFilterRequestParams = {
  queryBy?: 'apiKey' | 'code',
  fieldCodes?: string[],
  fieldApiKeys?: string[],
  filter?: {
    condition?: RecordFilterCondition;
    option?: {
      offset: number;
      limit: number;
      orderBy?: {
        fieldApiKey: string;
        order: 'DESC' | 'ASC';
      };
      count?: boolean;
    };
  };
}

/**
 * EQ(相等) / NOT_EQ(不相等)：支持number类型；
 * CONTAINS(包含) / NOT_CONTAINS(不包含)：支持enum类型包含条件、string类型模糊匹配
 * GT(大于)/GTE(大于等于)：支持number和日期类型
 * LT(小于)/LTE(小于等于)：支持number和日期类型
 */
type RecordFilterItem = {
  fieldApiKey: string;
  operator: 'EQ' | 'NOT_EQ' | 'CONTAINS' | 'NOT_CONTAINS' | 'GT' | 'GTE' | 'LT' | 'LTE';
  value: any;
}

type RecordFilterCondition = {
  conditions: (RecordFilterItem | RecordFilterCondition)[];
  connector: 'AND' | 'OR';
};
```

**返回值**

``` ts
type GetRecordByFilterResponse = EntityHttpResponse<{
  records: RecordData[];
  total: number;
}>;
```

### createRecord

**功能：**创建一条记录。

**参数**

- `{CreateRecordParams} params` 创建记录请求参数

**示例**
``` ts
type CreateRecordParams = {
  data: Record<string, any>;
}
```

**返回值**

新增成功将返回 RecordId。

### updateRecord

**功能：**更新记录。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{UpdateRecordParams} params` | 请求参数 |

**示例**
``` ts
type UpdateRecordParams = {
  data: Record<string, any>;
  recordId: string;
}
```

**返回值**
新增成功将返回 RecordId。

### deleteRecord

**功能：**删除单条记录。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
|`{string} recordId` | 记录 ID |

**返回值**
当删除成功时，返回为空；当删除失败时，会返回`error`。


### getFields

**功能：**获取所有的字段信息。

**返回值**

返回对象字段的数组。

**示例**
``` ts
// 字段类型
type Field = {
  apiKey: string;
  code: string;
  name: string; // 字段名称
  entityCode: string;
  linkEntityCode?: string;
  linkFieldCode?: string;
  mainField: number; // 是否是主字段
  maxLength: number;
  minLength: number;
  requireFlag: number; // 是否必填
  type: number; // 字段类型
  uniqueFlag: string; // 是否唯一
  customFlag: number; // 是否为自定义字段
  description: string; // 描述文本
  editFlag: number;
  fieldLink: any;
  layoutFlag: number;
};
```

### getFieldPermissions

**功能：**获取所有的字段的读写权限。

**返回值**

字段权限，`writable`表示可读，`readable`表示可写；

**示例**
``` ts
// 字段权限响应数据
type FieldPermissionResponse =
  Record<string, { writeable: boolean, readable: boolean }>;

```

### getReadableFields

获取所有可读的字段信息, 与`getFields`返回数据格式相同。返回的字段信息，经过`getFieldPermissions`过滤，只返回`readable`为true的数据。

### invokeDataSourceMethod

**功能：**调用对象实体的自定义动作

**参数**

|参数名 | 参数说明 | 
|---------|---------|
|`{InvokeDataSourceMethodRequestParams}` | params 对象自定义动作请求参数 | 

**示例**
``` ts
// 对象自定义动作的入参
type DataSourceMethodParams<T = any> = {
  paramKey: string;
  fieldType: string;
  value: T;
}

// 对象自定义动作请求参数
type InvokeDataSourceMethodRequestParams = {
  methodName: string;
  params: DataSourceMethodParams[];
}

```

### getFieldByApiKeySync

**功能：**根据字段的apiKey 同步获取字段信息。

本质是获取本地已经缓存的字段信息，在调用此方法之前，可以先调用`getFields`方法，从请求中获取到全部字段信息。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string}apiKey`  | 字段的 apiKey |



### convertApiKeyToCode

**功能：**将 apiKey 转换为 code。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
|`{string} apiKey` | 字段编码 apiKey |

### convertCodeToApiKey

**功能：**将 code 转换为 apiKey。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} code` | 字段编码 code |


### convertApiKeyValuesToCodeValues

**功能：**将 Record 数据由 apiKey 转换为 code。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{Record<string, any>} apiKeyValues`  | apiKey 格式数据 |

### convertCodeValuesToApiKeyValues

**功能：**将 Record 数据由 code 转换为 apiKey。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
|`{Record<string, any>}codeValues`  | code 格式数据 |
