## 目录

### Interfaces（接口）
- [Response](https://cloud.tencent.com/document/product/1484/75828)
- [Socket](https://cloud.tencent.com/document/product/1484/75829)

### Variables（变量）

### Const default

default: { connect: *any* }


#### Type declaration

- ##### connect:function
  - connect(url: *string*, callback: ((socket: [Socket](https://cloud.tencent.com/document/product/1484/75829)) => *void*), headers?: *Record*<*string*, *string*>): [Response](https://cloud.tencent.com/document/product/1484/75828)
发起 websocket connect 请求。
```js
    import ws from 'pts/ws';
    import { check, sleep } from 'pts';
    
    export default function () {
        const res = ws.connect('ws://localhost:8080/echo', function (socket) {
            socket.on('open', () => console.log('connected'));
            socket.on('message', (data) => console.log('message received: ', data));
            socket.on('close', () => console.log('disconnected'));
            socket.on('ping', () => console.log('ping'));
            socket.on('pong', () => console.log('pong'));
            socket.on('error', (e) => console.log('error happened', e.error()));
            socket.send('message');
            socket.setTimeout(function () {
                console.log('3 seconds passed, closing the socket');
                socket.close();
            }, 3000);
            socket.setInterval(function () {
                socket.ping();
            }, 500);
            socket.setLoop(function () {
                sleep(0.1)
                socket.send('loop message')
            });
        });
        check('status is 101', () => res.status === 101);
    };
```
   #### Parameters

    - ##### url: *string*

   请求地址

   - ##### callback: ((socket: [Socket](https://cloud.tencent.com/document/product/1484/75829)) => *void*)

   回调函数

      - (socket: [Socket](https://cloud.tencent.com/document/product/1484/75829)): *void*

   - #### Parameters

     - ##### socket: [Socket](https://cloud.tencent.com/document/product/1484/75829)

      Returns *void*

 - ##### Optional headers: *Record*<*string*, *string*>

  Returns [Response](https://cloud.tencent.com/document/product/1484/75828)
    响应对象
