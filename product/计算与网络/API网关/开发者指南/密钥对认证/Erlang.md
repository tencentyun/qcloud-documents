## 操作场景

该任务指导您使用 Erlang 语言，通过密钥对鉴权来对您的 API 进行认证管理。

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“密钥对鉴权”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台密钥管理界面创建密钥对。
4. 在控制台使用计划界面创建使用计划，并将使用计划与已创建的密钥对绑定（参考 [使用计划示例](https://cloud.tencent.com/document/product/628/11816)）。
5. 将使用计划与 API 或 API 所在服务进行绑定。
6. 参考 [示例代码](#example)，使用 Erlang 语言生成签名内容。

## 注意事项

- 最终发送的 HTTP 请求内至少包含两个 Header：Date 和 X-Date 二选一以及 Authorization，可以包含更多 header。如果使用 Date Header，服务端将不会校验时间；如果使用 X-Date Header，服务端将校验时间。
- Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Fri, 09 Oct 2015 00:00:00 GMT。
- X-Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Mon, 19 Mar 2018 12:08:40 GMT。X-Date Header 里的时间和当前时间的差值不能超过15分钟。
- 如果是微服务 API，Header 中需要添加 “X-NameSpace-Code” 和 “X-MicroService-Name” 两个字段，通用 API 不需要添加，Demo 中未添加这两个字段。

<span id="example"></span>

## 示例代码

```erl
-module(apigateway_erlang_demo).

%% API
-export([request_api/0]).

%% request_api()
request_api() ->

%%      启动inets服务，项目如果已启动此服务，去掉这里
        inets:start(),

        Url = "http://service-xxxxxxxx-1234567890.ap-beijing.apigateway.myqcloud.com/release/xxxxx",
        Source = "xxxxxx",
        GMTDate = now_to_utc_string(),
        SecretId = "xxxDf4estwodtdzoke1234567890i3j9jv18wt9u",
        SecretKey = "xxxSNF0CEp3OhN4t91234567890AWrct960X9192",
        Sign = simple_sign(Source, GMTDate, SecretId, SecretKey),
        Header = [
                {"Source", Source},
                {"x-Date", GMTDate},
                {"Authorization", Sign},
                {"Content-Type", "application/x-www-form-urlencoded"}
        ],

        case httpc:request(get, {Url, Header}, [], []) of
                {ok, {_StatusLine, _Header, Result}} ->
                        Result;

%% %%                Result -> need decode

                Error ->
                        Error
        end.

simple_sign(Source, GMTDate, SecretId, SecretKey) ->
        Auth = "hmac id=\"" ++ SecretId ++ "\", algorithm=\"hmac-sha1\", headers=\"x-date source\", signature=\"",
        SecretKey = "xxxSNF0CEp3OhN4t91234567890AWrct960X9192",
        Source = "xxxxxx",
        SignStr = "x-date: " ++ GMTDate ++ "\n" ++ "source: " ++ Source,
        Mac = crypto:hmac(sha, SecretKey, SignStr),
        Sign = base64:encode(Mac),
        Sign2 = binary_to_list(Sign),
        Sign3 = Auth ++ Sign2 ++ "\"",
        Sign3.

%% 获取当前时间并转为  "Mon, 02 Jan 2006 15:04:05 GMT" 格式
now_to_utc_string() ->
        {{Year, Month, Day}, {Hour, Minute, Second}} = calendar:universal_time(),
        WeekNum = week_num(),
        Month1 = month_to_english(Month),
        WeekNum1 = week_to_english(WeekNum),
        Day1 = lists:flatten(io_lib:format("~2..0w", [Day])),
        Date1 = WeekNum1 ++ ", " ++ Day1 ++ " " ++ Month1,
        Date2 = lists:flatten(
                io_lib:format(" ~4..0w ~2..0w:~2..0w:~2..0w GMT",
                        [Year, Hour, Minute, Second])),
        Date1 ++ Date2.

week_num() ->
        {Date, _} = calendar:local_time(),
        calendar:day_of_the_week(Date).

%% day_of_the_week
week_to_english(1) ->
        "Mon";
week_to_english(2) ->
        "Tue";
week_to_english(3) ->
        "Wed";
week_to_english(4) ->
        "Thu";
week_to_english(5) ->
        "Fri";
week_to_english(6) ->
        "Sat";
week_to_english(7) ->
        "Sun".

month_to_english(1) ->
        "Jan";
month_to_english(2) ->
        "Feb";
month_to_english(3) ->
        "Mar";
month_to_english(4) ->
        "Apr";
month_to_english(5) ->
        "May";
month_to_english(6) ->
        "Jun";
month_to_english(7) ->
        "Jul";
month_to_english(8) ->
        "Aug";
month_to_english(9) ->
        "Sept";
month_to_english(10) ->
        "Oct";
month_to_english(11) ->
        "Nov";
month_to_english(12) ->
        "Dec".
```
