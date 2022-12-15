通过 `audioContext.on('event-name', callbackFunction)` 方法去监听 AudioContext 的回调事件。例如：
```plaintext
audioContext.on('on-play', (res) => {
    console.info(res);
});
audioContext.on('on-loaded-metadata', (res) => {
    console.info(res);
});
audioContext.on('on-ended', (res) => {
    console.info(res);
});
```
