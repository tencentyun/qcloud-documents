# addPhoneRepeatCalendar(Object object)

## 功能描述

向系统日历添加重复事件

## 参数

### Object object

| 属性           | 类型     | 默认值 | 必填 | 说明                                                  |
| :------------- | :------- | :----- | :--- | :---------------------------------------------------- |
| title          | string   |        | 是   | 日历事件标题                                          |
| startTime      | number   |        | 是   | 开始时间的 unix 时间戳 (1970年1月1日开始所经过的秒数) |
| allDay         | boolean  |        | 否   | 是否全天事件，默认 false                              |
| description    | string   |        | 否   | 事件说明                                              |
| location       | string   |        | 否   | 事件位置                                              |
| endTime        | string   |        | 否   | 结束时间的 unix 时间戳，默认与开始时间相同            |
| alarm          | boolean  |        | 否   | 是否提醒，默认 true                                   |
| alarmOffset    | number   |        | 否   | 提醒提前量，单位秒，默认 0 表示开始时提醒             |
| repeatInterval | string   |        | 否   | 重复周期，默认 month 每月重复                         |
| repeatEndTime  | number   |        | 否   | 重复周期结束时间的 unix 时间戳，不填表示一直重复      |
| success        | function |        | 否   | 接口调用成功的回调函数                                |
| fail           | function |        | 否   | 接口调用失败的回调函数                                |
| complete       | function |        | 否   | 接口调用结束的回调函数（调用成功、失败都会执行）      |

**repeatInterval**

| 合法值 | 说明                               |
| :----- | :--------------------------------- |
| day    | 每天重复                           |
| week   | 每周重复                           |
| month  | 每月重复。该模式日期不能大于 28 日 |
| year   | 每年重复                           |