SCF CLI 支持查看云端函数运行统计数据。

## 参数说明

| 参数      | 简写 | 必填 | 描述                                                         | 示例                  |
| --------- | ---- | ---- | ------------------------------------------------------------ | --------------------- |
| name      | -n   | 是   | 函数名                                                       | -n hello                 |
| period    | -p   | 否   | 时间粒度，单位为秒，目前支持60秒和300秒                       |-p 60                    |
| region    | -r   | 否   | 指定函数所在区域，默认为 configure 配置的区域                | -r ap-shanghai       |
| starttime | 无   | 否   | 开始时间，默认为当前时刻                                     | starttime ‘2019-09-03 16:56:00’ |
| endtime   | 无   | 否   | 结束时间，默认当前时间前1小时                           | endtime ‘2019-09-03 17:56:00’ |
| metric    | -m   | 否   | 指定查看统计数据，默认提供指标包括 Invocation，Duration，Mem，Error，FuncErrRate | -m Mem                   |
>?请前往 [指标名称](https://cloud.tencent.com/document/api/248/37207#2.2-.E6.8C.87.E6.A0.87.E5.90.8D.E7.A7.B0) 查看 metric 参数的所有可填写指标。
>

## 使用示例
例如，初始化配置为 ap-shanghai 区域，在 default 命名空间下已运行了 test 函数。

- 执行以下命令 ，查看 `test` 函数的 Invocation ，Duration，Mem，Error，FuncErrRate 统计信息。统计周期为过去一小时，统计粒度为60秒。
```bash
$ scf stat -n test
      Time                Invocation     Duration(ms)      Mem(MB)     Error     FuncErrRate(%)
 190903 16:57:00               7            1.467       28.783         0                  0
 190903 16:58:00               1             0.73       19.398         0                  0
 190903 16:59:00               0                0            0         0                  0
```
- 执行以下命令，查看 `test` 函数的某一个指定的统计数据。
```bash
$ scf stat -n test -m Mem
      Time                    Mem(MB)
 190903 16:56:00             28.992
 190903 16:57:00             19.403
```
- 执行以下命令，查看 `test` 函数的多个指定的统计数据。
>?需查看的函数指标请使用英文逗号分隔，并附加在 -m 参数后。
>
```bash
$ scf stat -n tenc -m Mem,Error
      Time                    Mem(MB)     Error
 190903 16:56:00             27.981        0
 190903 16:57:00             27.891        0
 190903 16:59:00             27.076        0
```
- 执行以下命令，查看自定义时间段内 `test` 函数的统计数据。
```bash
$ scf stat -n tenc --starttime '2019-09-03 16:56:00' --endtime '2019-09-03 17:00:00' 
      Time                    Invocation     Duration(ms)      Mem(MB)     Error     FuncErrRate(%)
 190903 16:56:00               0                0            0              0                  0
 190903 16:57:00               0                1.467        27.783         0                  0
 190903 16:58:00               0                1.567        28.783         0                  0
```

