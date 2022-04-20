<style>
table th:nth-of-type(1) {
width: 40%        
}
</style>

ComponentService 组件服务作用于特定组件范围内的前端服务，每个组件内唯一。

## 使用指引

### 原生获取
``` ts
// 直接获取
const componentService = SDK.getComponentService('1479794208557621306', 'Input1');
// 或
// 从上级服务（全局服务）获取
const pageService = SDK.getGlobalService().getPageService('1479794208557621306');
const componentService = pageService.getComponentService('Input1');
```

### React Hooks 中获取

React Hooks 中的 `useComponentService` 不需要输入参数, 可以直接根据组件 [上下文](https://zh-hans.reactjs.org/docs/context.html) 获取到当前所在的组件中的组件服务。

``` ts
function HelloWorld () {
  const componentService = SDK.useComponentService();

  return <div></div>;
}
```

## API 参考

### getState
**功能：**用于获取当前组件的状态。

**示例**
``` ts
const state = componentService.getState();
```

### setState

**功能：**设置当前组件的状态，可以支持对象的方式或更新函数的方式设置。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{any | Function} statePatcher` | 修改组件状态，这个参数支持对象形式更新，同时支持更新函数的方式更新状态。|

**示例**

``` ts
componentService.setState({ value: 'abc' });
// 或
componentService.setState(s => {
  s.value = 'abc';
  return s;
});
```

### getStateByKey

**功能：**根据输入参数状态名称，获取指定的状态的值。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} stateKey`  | 状态名称。 |

**示例**

``` ts
const state = componentService.getStateByKey('value');
```

### setStateByKey

**功能：**根据输入参数状态名称，设置当前组件的状态值，可以支持值的方式或更新函数的方式设置

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} stateKey`  | 状态名称。 |
| `{any | Function} statePatcher`  | 修改组件状态，这个参数支持对象形式更新，同时支持更新函数的方式更新状态。|


**示例**

``` ts
componentService.setState('value', 'abc');
// 或
componentService.setState('value', val => {
  val += 'efg';
  return val;
});
```

### getProps

**功能：**获取组件的所有属性

**示例**

``` ts
componentService.getProps();
```

### getPropByKey

**功能：**根据输入的属性key，获取组件的所有属性

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} propKey`  | 属性名称。 |

**示例**

``` ts
componentService.getPropByKey('title');
```

### execAction

**功能：**执行组件指定的动作。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} actionName`  | 动作名称。|
| `{any} params`  | 动作的入参。|

**示例**

``` ts
componentService.execAction('fetchData');
```

### forceUpdate

**功能：**强制更新组件，重新执行组件的渲染函数。

**示例**

``` ts
componentService.forceUpdate();
```
