## 目录
### Interfaces（接口）
- [Metadata](https://cloud.tencent.com/document/product/1484/77617)

### Variables（变量）
- [default](#default)

### Functions（函数）
- [check](#check)
- [sleep](#sleep)
- [step](#step)

## Variables（变量）

[](id:default)
### default

default: { check: ((name: *string*, callback: (() => *boolean*), interrupt?: *boolean*) => *boolean*); metadata: (() => [Metadata](../interfaces/pts.Metadata.html)); sleep: ((seconds: *number*) => *void*); step: ((name: *string*, callback: (() => *void*)) => *any*) }


```
Defined in typings/pts.d.ts:105
```


#### Type declaration

- ##### check: ((name: *string*, callback: (() => *boolean*), interrupt?: *boolean*) => *boolean*)

  - - (name: *string*, callback: (() => *boolean*), interrupt?: *boolean*): *boolean*

    - check 主要针对请求返回的结果做进一步检查，如果检查失败，则代表测试失败。

```js
      import http from 'pts/http';
      import { check } from 'pts';
      
      export default function () {
          const resp = http.get('http://httpbin.org/get');
          check('statusCode is 200', () => resp.statusCode === 200);
      };
  ```

  #### Parameters

  - ##### name: *string*

   名字

  - ##### callback: (() => *boolean*)

    函数，返回 boolean 类型

      - - (): *boolean*

    - #### Returns *boolean*

    - ##### Optional interrupt: *boolean*

        可选。是否中断函数

 #### Returns *boolean*

      检查结果

- ##### metadata: (() => [Metadata](../interfaces/pts.Metadata.html))

  - - (): [Metadata](../interfaces/pts.Metadata.html)

  - metadata 返回压测任务的元数据。

      ```js
      import { metadata } from 'pts';
      
      export default function () {
        let md = metadata();
        console.log(md.userID); // 123456
        console.log(md.appID); // 123456
        console.log(md.scenarioID); // scenario-xxxxxxxx
        console.log(md.region); // ap-guangzhou
        console.log(md.jobID); // job-xxxxxxxx
      }
      ```

  #### Returns [Metadata](../interfaces/pts.Metadata.html)

   元数据

- ##### sleep: ((seconds: *number*) => *void*)

  - - (seconds: *number*): *void*

    - 在指定的时间内暂停 VU 执行。

      ```js
      import { sleep } from 'pts';
      
      export default function () {
          sleep(1);
      };
      ```

  #### Parameters

  - ##### seconds: *number*

    时间，单位秒

#### Returns *void*

- ##### step: ((name: *string*, callback: (() => *void*)) => *any*)

  - - (name: *string*, callback: (() => *void*)): *any*

    - 把压测场景分步骤，在压测报告中可以体现。

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

   - ##### name: *string*

    名称

    - ##### callback: (() => *void*)

      函数

     - - (): *void*

     - #### Returns *void*

    #### Returns *any*

## Functions

### check

- check(name: *string*, callback: (() => *boolean*), interrupt?: *boolean*): *boolean*


```
Defined in typings/pts.d.ts:57
```


check 主要针对请求返回的结果做进一步检查，如果检查失败，则代表测试失败。

  ```js
  import http from 'pts/http';
  import { check } from 'pts';
  
  export default function () {
      const resp = http.get('http://httpbin.org/get');
      check('statusCode is 200', () => resp.statusCode === 200);
  };
  ```

#### Parameters

  - ##### name: *string*

   名字

  - ##### callback: (() => *boolean*)

    函数，返回 boolean 类型

    - - (): *boolean*

      - #### Returns *boolean*

  - ##### Optional interrupt: *boolean*

    可选。是否中断函数

#### Returns *boolean*

 检查结果



### metadata

- metadata(): [Metadata](../interfaces/pts.Metadata.html)
```
Defined in typings/pts.d.ts:103
```

  metadata 返回压测任务的元数据。

  ```js
  import { metadata } from 'pts';
  
  export default function () {
    let md = metadata();
    console.log(md.userID); // 123456
    console.log(md.appID); // 123456
    console.log(md.scenarioID); // scenario-xxxxxxxx
    console.log(md.region); // ap-guangzhou
    console.log(md.jobID); // job-xxxxxxxx
  }
  ```

#### Returns [Metadata](../interfaces/pts.Metadata.html)

 元数据



### sleep

- sleep(seconds: *number*): *void*
 ```
 Defined in typings/pts.d.ts:18
 ```

  在指定的时间内暂停 VU 执行。

  ```js
  import { sleep } from 'pts';
  
  export default function () {
      sleep(1);
  };
  ```

 #### Parameters

  - ##### seconds: *number*

    时间，单位秒

 #### Returns *void*



### step

- step(name: *string*, callback: (() => *void*)): *any*


```
Defined in typings/pts.d.ts:37
```


  把压测场景分步骤，在压测报告中可以体现。

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

- ##### name: *string*

    名称

- ##### callback: (() => *void*)

    函数

    - - (): *void*

      - #### Returns *void*

 #### Returns *any*
