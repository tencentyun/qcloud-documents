## 目录

### Variables（变量）
- [default](#default)

### Functions（函数）
- [check](#check)
- [sleep](#sleep)
- [step](#step)

## Variables（变量）

[](id:default)
### default
- **default**: `Object`

```
Defined in typings/pts.d.ts:58
```

#### Type declaration
| Name    | Type                                                         |
| :------ | :----------------------------------------------------------- |
| check | (`name`: `string`, `callback`: () => `boolean`, `interrupt?`: `boolean`) => `boolean` |
| sleep | (`seconds`: `number`) => `void`                              |
| step  | (`name`: `string`, `callback`: () => `void`) => `any`        |


## Functions

[](id:check)
### check
- **check**(`name`, `callback`, `interrupt?`): `boolean`

check 主要针对请求返回的结果做进一步检查，如果检查失败，则代表测试失败。
```
Defined in typings/pts.d.ts:57
```
```js
import http from 'pts/http';
import { check } from 'pts';

export default function () {
    const resp = http.get('http://httpbin.org/get');
    check('statusCode is 200', () => resp.statusCode === 200);
};
```

#### Parameters
| Name         | Type            | Description             |
| :----------- | :-------------- | :---------------------- |
| name       | `string`        | 名字                    |
| callback   | () => `boolean` | 函数，返回 boolean 类型 |
| interrupt? | `boolean`       | 可选。是否中断函数      |

**Returns：**`boolean`
检查结果


[](id:sleep)
### sleep
- **sleep**(`seconds`): `void`

在指定的时间内暂停 VU 执行。
```
Defined in typings/pts.d.ts:18
```
```js
import { sleep } from 'pts';

export default function () {
    sleep(1);
};
```

#### Parameters
| Name      | Type     | Description  |
| :-------- | :------- | :----------- |
| `seconds` | `number` | 时间，单位秒 |

** Returns：**`void`



### step
- **step**(`name`, `callback`): `any`

把压测场景分步骤，在压测报告中可以体现。
```
Defined in typings/pts.d.ts:37
```


```js
import http from 'pts/http';
import { step } from 'pts';

export default function () {
    step('get', function () {
        http.get('http://httpbin.org/get');
    })
};
```

#### Parameters

| Name       | Type         | Description |
| :--------- | :----------- | :---------- |
| name   | `string`     | 名称        |
| callback | () => `void` | 函数        |

**Returns：**`any`
