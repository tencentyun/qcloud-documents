   
## 适用场景

根据表格数据的不同，显示不同颜色

## 关键字

<font color ="#0abf5b">表格字体&nbsp;&nbsp;</font>
<font color ="#ff7200">JSX&nbsp;&nbsp;</font>

## 示例

>1.根据枚举值的不同显示颜色
>
>2.字段1根据「状态」字段的不同值显示不同颜色
>![img](https://qcloudimg.tencent-cloud.cn/raw/0ff451ac5244cf253d6a323b9472bfb0.png)
### 数据模型

对象结构如下所示：

>     对象名称：表格色块JSX
>     字段描述：
>       ①状态：status，枚举，包括状态1，状态2，状态3
>       ②字段1：field1，文本
>       ③字段2：field2，文本
>       ④字段3：field3，文本
>     ![img](https://qcloudimg.tencent-cloud.cn/raw/d1c85d2744ad3589df19043b8bffc292.png)
### 示例1：根据枚举值的不同显示颜色

#### 页面配置

##### 1.设置基础页面

> 根据对象「表格色块JSX」自动创建「表格色块JSX列表」和「表格色块JSX信息」页面，效果如下：
> ![img](https://qcloudimg.tencent-cloud.cn/raw/72eaf3a568602b4c594ef3c7f1cb535b.png)
>
> 「表格色块JSX列表」页面
> ![img](https://qcloudimg.tencent-cloud.cn/raw/ce17253c52ab13ed19e6e79d18a98e47.png)
>
> 「表格色块JSX信息」页面
> ![img](https://qcloudimg.tencent-cloud.cn/raw/936aad1d397073ba8d148d9c8baf83da.png)
##### 2.设置「状态枚举」值字体颜色

> ① 设置表格「状态」列，选中自定义代码，如下所示：
> ![img](https://qcloudimg.tencent-cloud.cn/raw/86a2d7b3f139548ac4a730fed8eceaf8.png)
> ② 编辑自定义代码，如下所示：
> ![img](https://qcloudimg.tencent-cloud.cn/raw/8439731530127fa6f2f6cc00bee94c48.png)
``` jsx
// 目前可选的导入包括 'react', '@tencent/tea-component', '@tencent/apaas-component-sdk'
import React, { useEffect, useContext } from 'react';
import {Tag} from  '@tencent/tea-component';
import { SDK, JsxDesignModeComponentProps, JsxRunModeComponentProps } from '@tencent/apaas-component-sdk';
import { Text } from "@tencent/tea-component";
/**
 * 运行态组件
 * props
 */
export default (props: JsxRunModeComponentProps) => {
  if (!props.value || !props.value[0]) {
       return (
   <Text theme="success">状态1</Text> // 成功绿
  );
  }
  // 获取当前列枚举值数据
  const data = props.value[0];
  const key = Object.keys(data)[0];
  const val = data[key];  // val 指向当前枚举值
  // 设置枚举值和颜色样式映射关系
  const themes = {
    '状态1': <Text theme="danger">{val}</Text>, // 异常红
    '状态2': <Text theme="warning">{val}</Text>, // 告警黄
    '状态3': <Text theme="success">{val}</Text> // 成功绿
  };
  // 设置枚举值颜色
  return themes[val]
}
```

#### 运行态效果

先通过「表格色块JSX列表」和「表格色块JSX信息」添加数据进去，如下所示：

>![img](https://qcloudimg.tencent-cloud.cn/raw/4d339e4072372a5a6d97ce1b4405e07c.png)
添加数据后效果，如下所示：

>![img](https://qcloudimg.tencent-cloud.cn/raw/2f7240afed05c157368b04ef32b26953.png)
### 示例2：字段1根据「状态」字段的不同值显示不同颜色

#### 页面配置

##### 设置「字段1」值字体颜色

> ① 设置表格「字段1」列，选中自定义代码，如下所示：
> ![img](https://qcloudimg.tencent-cloud.cn/raw/852eb97c3afedf9d6951b8beefbc835d.png)
> ② 编辑自定义代码，如下所示：
> ![img](https://qcloudimg.tencent-cloud.cn/raw/b4383c6183a86c9b9eb5037559430cfa.png)
``` jsx
// 目前可选的导入包括 'react', '@tencent/tea-component', '@tencent/apaas-component-sdk'
import React, { useEffect, useContext } from 'react';
import {Tag} from  '@tencent/tea-component';
import { SDK, JsxDesignModeComponentProps, JsxRunModeComponentProps } from '@tencent/apaas-component-sdk';
import { Text } from "@tencent/tea-component";
/**
 * 运行态组件
 * props
 */
export default (props: JsxRunModeComponentProps) => {
  if (!props.value || !props.value[0]) {
       return (
   <Text theme="success">空白</Text> // 成功绿
  );
  }
  // 获取当前「字段1」值
  const data = props.value;
  // 获取枚举字段值
  const statusData = props.record['status'][0]
  const key = Object.keys(statusData)[0];
  const status = statusData[key]; // 枚举字段值
  const themes = {
    '状态1': <Text theme="danger">{data}</Text>, // 异常红
    '状态2': <Text theme="warning">{data}</Text>, // 告警黄
    '状态3': <Text theme="success">{data}</Text> // 成功绿
  };
  return themes[status]  // 设置字体颜色
}
```

#### 运行态效果

>![img](https://qcloudimg.tencent-cloud.cn/raw/ac5c8d6729e218d93991f763a021e509.png)
##其他
字体样式效果可参考[Tea组件库](http://tea.tencent.com/component/text)，这里会有丰富的样式提供
