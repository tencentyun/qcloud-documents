**Websocket 代码示例：**

```js
// Websocket API

import ws from 'pts/ws';
import { check, sleep } from 'pts';
export default function () {
    const res = ws.connect("ws://localhost:8080/echo", function (socket) {
        socket.on('open', () => console.log('connected'));
        socket.on('message', (data) => console.log('Message received: ', data));
        socket.on('close', () => console.log('disconnected'));
        socket.send("message");
        socket.setTimeout(function () {
            console.log('3 seconds passed, closing the socket');
            socket.close();
        }, 3000);
        socket.setInterval(function () {
            socket.ping();
        }, 500);
        socket.setLoop(function () {
            sleep(0.1)
            socket.send("loop message")
        });
    });
    check("status is 101", () => res.status === 101);
}
```

