# PageService 页面服务

作用于特定页面范围内的前端服务，每个页面内唯一。

## 使用

### 原生获取

``` ts
// 直接获取
const pageService = SDK.getPageService('1479794208557621306');
// 或
// 从上级服务（全局服务）获取
const globalService = SDK.getGlobalService();
const pageService = globalService.getPageService('1479794208557621306');
```

### React Hooks中获取

React Hooks中的`usePageService`不需要输入参数, 可以直接获取到当前组件[上下文](https://zh-hans.reactjs.org/docs/context.html)中的页面服务。

``` ts
function HelloWorld () {
  const pageService = SDK.usePageService();

  return <div></div>;
}

```

## API参考

### getComponentService

根据传入的组件ID，返回页面中指定组件的前端组件服务。

**参数**

- `{string} compId` 组件ID

**示例**

``` ts
const componentService = pageService.getComponentService('Input1');
```

### getVariable

根据传入的变量名，获取**页面变量**的值

**参数**

- `{string} variableKey` 页面变量名称

**示例**

``` ts
const myTempValue = pageService.getVariable('myTempValue');
```

### setVariable

为指定名称的**页面变量**设置值

**参数**

- `{string} variableKey` 指定的全局变量名称
- `{any} variableValue` 要设置的值

**示例**

``` ts
pageService.setVariable('myTempValue', 'abc');
```

### getParamVariable

根据传入的变量名，获取**入参变量**的值。入参变量只读， 不可修改。（可以获取URL上传递的参数）

**参数**

- `{string} variableKey` 指定的入参变量名称

**示例**

``` ts
pageService.getParamVariable('id');
```

### getComponentState

根据传入的组件ID，返回页面中指定组件的状态。

本方法等同于，先通过组件ID获取组件服务，在运行`getState`

**参数**

- `{string} compId` 组件ID

**示例**

``` ts
const componentState = pageService.getComponentState('Input1');
// componentState -> {
//   value: 'xxx'
// }
// 以上代码等同于
// const componentState = pageService.getComponentService('Input1').getState();
```

### setComponentState

根据传入的组件ID，设置指定组件的状态。

**参数**

- `{string} compId` 组件ID
- `{any | Function} state` 修改组件状态，这个参数支持对象形式更新，同时支持更新函数的方式更新状态。

**示例**

``` ts
pageService.setComponentState('Input1', {
  value: 'abc'
});
```

### execComponentAction

根据传入的组件ID，执行对应组件的动作。

**参数**

- `{string} compId` 组件ID
- `{any | Function} state` 修改组件状态，这个参数支持对象形式更新，同时支持更新函数的方式更新状态。

**示例**

``` ts
pageService.setComponentState('Input1', {
  value: 'abc'
});
```