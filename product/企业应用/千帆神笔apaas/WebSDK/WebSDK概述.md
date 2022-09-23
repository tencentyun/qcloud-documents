
千帆神笔 aPaaS Web SDK 提供给开发者在 Web 端与平台集成的能力。SDK 可应用在 **JSX 组件**、**自定义组件**、**自定义动作**和**自定义页面**的场景。SDK 的内容包括 **组件上下文**、**React Hooks**、**工具方法**、**事件总线**、**数据交互方法**和 **Typescript 类型定义**。

## 安装 Web SDK

使用 CLI 创建的自定义组件项目会自动安装 Web SDK，您也可以使用下面的命令进行安装。JSX 组件可以直接使用。

```
# 使用 npm 安装
npm install @apaas-cloud/web-sdk
# 使用 yarn 安装
yarn add @apaas-cloud/web-sdk
```

## SDK 代码

平台开源了 SDK 的类型定义代码，可以在开发中，根据 typescript 类型提示进行快捷开发。

[SDK 参考代码 >>](https://github.com/qcloud-apaas/web-sdk)

## SDK 示例

您可以参考自定义组件内调用 SDK 的示例，了解 SDK 功能。

[自定义组件常用功能示例 >>](https://github.com/qcloud-apaas/web-examples)

## React Hook

目前 SDK 中主要是以 [React Hooks](https://reactjs.org/docs/hooks-intro.html) 的方式实现，所以需要开发者对 React 函数组件和 Hooks 有一定的了解，后续会开放更多的 SDK 调用方式。

```ts
import React from 'react';
import { SDK } from '@qcloud-apaas/web-sdk';
import { Slider } from 'antd';
import properties from './properties';

const CustomRunComponent = (props) => {
  const { compId, fieldBinding } = props;
  const { value, onChange } = SDK.useModel(compId, {
    fieldBinding,
  });
  return <input value={value} onChange={onChange} />;
};

export default CustomRunComponent;
```
