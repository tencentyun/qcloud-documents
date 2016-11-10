## 1. 说明
本节主要描述PC页面的开发方法

## 2. PC页面开发步骤
### 2.1 页面头部引入JS
```
<script type="text/javascript" src="xxx"></script>
```
[JS地址的获取方法](https://www.qcloud.com/doc/product/295/6620)
### 2.2 添加验证码展示控件
```
<!--显示验证码的地方预留的最小空间，小于该值会导致显示异常-->
<!--触发式：300px*40px（宽*高）-->
<!--嵌入式：300px*270px-->
<!--弹窗式：300px*310px-->
<!--通过width和height设置验证码初始宽高，未设置会导致显示异常，默认触发式-->
<div id="TCaptcha" style="width:300px;height:40px;" ></div>
```
[不同样式体验入口](http://open.captcha.qq.com/cap_web/experience-character.html)
### 2.3 初始化并显示验证码
```
<script type="text/javascript">
    var capOption={callback :cbfn};
    capInit(document.getElementById("TCaptcha"), capOption);
    //回调函数：验证码页面关闭时回调
    function cbfn(retJson)
    {
        if(retJson.ret==0)
        {
            // 用户验证成功,需要校验签名
        }
        else
        {       
            //用户关闭验证码页面，没有验证
        }
    }
</script>
```

## 3. 完整页面代码示例
```
<!DOCTYPE html>
<html>
    <head>
        <script type="text/javascript" src="xxx"></script>
    </head>

    <body>
        <form action="xxx" id="myform" method="post">
            <input type="hidden" id="ticket" name="ticket" value="">
            <div id="TCaptcha" style="width:310px;height:40px;" ></div>
        </form>
        <script type="text/javascript">
            var capOption = {callback:cbfn, themeColor:"a11bbb"};
            capInit(document.getElementById("TCaptcha"), capOption);
            //回调函数：验证码页面关闭时回调
            function cbfn(retJson) {
                if (retJson.ret == 0) {
                    // 用户验证成功
                    document.getElementById("ticket").value = retJson.ticket;
                    document.getElementById("myform").submit();
                }
                else {
                    //用户关闭验证码页面，没有验证
                }
            }
        </script>
    </body>
</html>
```

## 4. javascript接口说明
|函数名         |  描述 |
| ------------- |:-------------|
| capInit(iframe_div, options)|初始化并显示验证码,参数如下：<br> 1. iframe_div（必填）：嵌入验证码iframe的元素。<br> 2. options： {callback:xxx,showheader:xxx, themeColor:xxxxxx,type:"embed"}，json格式对象。<br><blockquote>callback： 验证码页面关闭回调函数。用户验证之后，会调用该函数，传入json格式验证参数。<blockquote>{ret:xxx,ticket:"xxx"}<br> ret=0 表示用户验证完成，业务可以校验ticket；<br>ret=1 表示用户未验证验证码，此时没有ticket参数。<br>参数ticket需要提交给业务后台，具体填哪个字段参考后面后台server开发部分。</blockquote><br>themeColor：设置页面的主题色彩，值为16进制色彩，比如ff572d。设置后页面里的按钮和图标会变成设置的颜色<br>type：PC端可选选项，配置验证码的样式。具体样式表现可以查看[验证码官网](http://open.captcha.qq.com/cap_web/experience-character.html)<br><blockquote>"point"：触发式（默认）<br>"embed"：嵌入式<br>"popup"：弹窗式</blockquote></blockquote>|
| capGetTicket()|获取验证码验证结果<br>返回Josn格式数据{ret: 0, randstr: "xxx"}其中ticket是验证码验证成功票据，如果票据为空表示验证码验证没通过|
| capRefresh()  | 刷新验证码<br>要求用户重新验证当票据验证失败时也可调用该接口刷新验证码 |
| capDestroy()  | 无参数，当dom被销毁需要重新使用capInit的时候，在capInit之前调用 |

## 5. 接入规范
1）请不要使用iframe页面嵌入验证码。验证码弹出的iframe框大小会变化，如果业务使用iframe会导致验证码iframe页面显示不全。

2）PC预留给验证码展示的地方尺寸不能小于300px（宽）*310px（高），否则会导致验证码显示异常而影响用户使用。

3）PC页面必须设置验证码显示页面初始宽高。    
