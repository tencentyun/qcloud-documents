<style>
table th:nth-of-type(1) {
width: 40%        
}
</style>

GlobalService 全局服务作用于整个应用范围内的前端服务，全局唯一。

## 使用指引

### 原生获取

``` ts
const globalService = SDK.getGlobalService();
```

### React Hooks 中获取

``` ts
function HelloWorld () {
  const globalService = SDK.useGlobalService();

  return <div></div>;
}

```

## API 参考

### getPageService

**功能：**根据传入的页面编码，返回对应页面的前端页面服务。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} pageCode` | 页面编码 |

**示例**

``` ts
const pageService = globalService.getPageService('1479794208557621306');
```

### getGlobalVariable

**功能：**根据传入的变量名，获取**全局变量**的值

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} variableKey`  | 全局变量名称 |

**示例**

``` ts
const myToken = globalService.getGlobalVariable('myToken');
```

### setGlobalVariable

**功能：**为指定名称的**全局变量**设置值

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} variableKey`  | 指定的全局变量名称 |
| `{any} variableValue`  | 要设置的值 |

**示例**

``` ts
globalService.setGlobalVariable('myToken', 'abc');
```

### getSystemVariable

**功能：**根据传入的变量名，获取**系统变量**的值。系统变量只读， 不可修改

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} variableKey`  | 指定的系统变量名称 | 

**示例**

``` ts
globalService.getSystemVariable('CurrentUser');
```

### getEnumOptionsByCode

**功能：**获取枚举选项集。枚举选项集的编码可以从**对象的枚举字段**中获取.例如属性面板的字段绑定或者`EntityService.getFields`都可以获取到**对象字段数据**

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} optionSetCode`  | 枚举选项集编码 |

**返回值**

|参数名 | 参数说明 | 
|---------|---------|
| `{Promise<EnumItem[]>}` | 异步返回的枚举选项集 |

`EnumItem` 格式如下：

| 属性        | 说明               | 类型     |
| ----------- | ------------------ | -------- |
| OptionCode  | 枚举选项的编码     | string |
| OptionLabel | 枚举选项的展示文本 | string   |

**示例**

``` ts
globalService.getEnumOptionsByCode('1460804025002848293').then((res) => {
  // [{
  //   OptionCode: 'xxx',
  //   OptionLabel: 'xxx'
  // }]
});
```
