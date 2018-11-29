
防盗链方案一php demo：

<?php

$origurl="http://200001791.vod.myqcloud.com/200001791_79690ab8cbfb11e6abf34b273b7e30d4.f220.av.m3u8";

$b=strpos($origurl,"http://");

if ($b==0) {
        $b=$b+7;
}else{
        $b=0;
}

$e=strpos($origurl,"/", $b);

$host=substr($origurl,$b,$e-$b);

$pb=$e;
$b=strrpos($origurl, "/");

$file=substr($origurl,$b+1);
if ($b-$pb-1>0){
        $path=substr($origurl,$pb,$b-$pb);
}else {
        $path="";
}
//echo $host . "\n". $file."\n".$path."\n";


$tm=dechex(strtotime("+2 hours")); //expire time 2 hours
$key="f4f2677a252717de91a03f0470a4e46c";

$sigstr=$key.$file.$tm;
$sig=md5($sigstr);
//echo $sigstr . "\n";
$url=$origurl."?t=".$tm."&sign=".$sig;

echo $url . "\n";
?>

防盗链方案二php demo：

<?php

//待加防盗链的原始url
$origurl="http://200001791.vod.myqcloud.com/200001791_79690ab8cbfb11e6abf34b273b7e30d4.f220.av.m3u8";


//从url解析host、path、file
$b=strpos($origurl,"http://");

if ($b==0) {
        $b=$b+7;
}else{
        $b=0;
}

$e=strpos($origurl,"/", $b);

$host=substr($origurl,$b,$e-$b);

$pb=$e;
$b=strrpos($origurl, "/");

$file=substr($origurl,$b+1);
if ($b-$pb-1>0){
        $path=substr($origurl,$pb,$b-$pb);
}else {
        $path="";
}
//echo $host . "\n". $file."\n".$path."\n";

//计算sig
$tm=dechex(strtotime("+2 hours")); //expire time 2 hours

$key="f4f2677a252717de91a03f0470a4e46c";
$random=rand();
$us="douyu";

$sigstr=$path.$tm.$key.$random.$us;
$sig=md5($sigstr);
//echo $sigstr . "\n";

//拼接最终防盗链
$url=$origurl."?txTime=".$tm."&random=".$random."&us=".$us."&txSign=".$sig;

echo $url . "\n";

?>

