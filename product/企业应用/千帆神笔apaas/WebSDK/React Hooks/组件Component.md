<style>
table th:nth-of-type(1) {
width: 40%        
}
</style>

## useModel
**使用条件：**运行态

**用法**

`useModel` 用于在输组件内实现状态值的绑定，可以实现与上下文中字段的值的绑定。这个方法会返回一个成对的 `value` 和 `onChange`，可以直接作为 props 传递给输入组件。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{object} options` | 初始化配置项 |

options 对象参数：

|参数名 | 参数说明 | 
|---------|---------|
| `{string} stateKey`  | 绑定的状态名, 默认绑定到 value 状态上 | 
| `{any} defaultValue`  | 默认值| 
| `{string} defaultValueByExpression`  | 表达式默认值 | 
| `{string} dynamicValue`  | 表达式动态值 |
| `{Field} fieldBinding` Field | 字段对象，设置当前字段与组件的值进行绑定：<li>`{Function} formatter` 值的格式化方法，当组件的状态值变化时，会自动格式化值的结果</li><li>`{Function} beforeSubmit` 与表单联动，表单提交之前，自动调用</li> | 

**返回值**

|参数名 | 参数说明 | 
|---------|---------|
|  `{any} value`  | 一个组件 state 值
|  `{Function} onChange`  | 调用 setState 更新组件状态的值 | 

**示例**

``` ts
// 举例一个值为数字类型的组件
const { value, onChange } = SDK.useModel({
  defaultValue: 0,
  defaultValueByExpression: '$system.SystemTime',
  dynamicValue: '$component.InputNumber1.state.value',
  fieldBinding: props.field,
  formatter(val) {
    // 当值类型是时间类型，转化为数字类型
    if (val instanceof Date) {
      return val.getTime();
    }
    return val;
  }
})
```


## useComponentState
**使用条件：**运行态

**用法**

定义组件的状态和初始值，返回一个 state 的值，以及更新 state 值的函数。设置的state的值，可以在表达式、入参等位置获取到。

这个方法可以类比 React 中的`useState`。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} stateKey`  | 状态名 |
| `{any} initialValue`  | 初始值 |

``` ts
const [pageIndex, setPageIndex] = SDK.useComponentState('pageIndex', 1);
```

## useComponentAction

**使用条件：**运行态

**用法**

定义组件的动作，传入一个方法，并返回这个方法的`useCallback`的函数。传入的方法，当动作编辑器中，触发组件动作时可以执行。

这个方法可以类比 React中 的 `useCallback`。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
|  `{string} actionName` | 动作名 |
| `{Function} actionCallback` | 动作的回调函数 | 
| `{Array} deps` | useCallback 的依赖项 | 


**示例**
``` ts
const fetchData = SDK.useComponentAction('fetchData', () => {
  // 这个方法可以在外部调用
});
```


## useComponentSubscriber
**使用条件：**运行态

**用法**

`useComponentSubscriber` 用于监听组件的 state。

**参数**

|参数名 | 参数说明 | 
|---------|---------|
| `{string} compId` | 组件 ID, 希望监听的组件 ID | 
| `{Function} callback`  | 可不传，callback 会在每次 state 值变化时触发，callback 回调参数与 `useComponentSubscriber`的返回值相同 |

**返回值**

componentState 是每个组件的实例上保存的状态，每个组件会有不同。作为输入组件，会有一个 `value` 可以获取到。

**示例**

``` ts
const state = SDK.useComponentSubscriber(props.compId, (state) => {
  // 此处可以执行您的回调
})
```
