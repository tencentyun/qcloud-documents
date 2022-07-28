## 注意事项
1. 推荐用户使用 PHPMailer 包：
 - 如果是新项目并且使用 composer 那么只需在 composer.json 加上 `"phpmailer/phpmailer": "^6.5"` ，或者执行 `composer require phpmailer/phpmailer` ，然后使用下面的代码即可。
 - 如果是老项目且没有使用 composer 的，需手动引入 [PHPMailer](https://github.com/PHPMailer/PHPMailer)。
2. 服务地址和端口请参见 [SMTP 服务地址](https://cloud.tencent.com/document/product/1288/65750)。

以下是代码示例：

```php
<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;
require './PHPMailer/src/Exception.php';
require './PHPMailer/src/PHPMailer.php';
require './PHPMailer/src/SMTP.php';

$mail = new PHPMailer(true);

try {
    //Server settings
    $mail->SMTPDebug  = SMTP::DEBUG_SERVER;                     //Enable verbose debug output
    $mail->SMTPAuth   = true;                                   //Enable SMTP authentication
    //$mail->AuthType   = 'LOGIN';                
    $mail->isSMTP();                                            //Send using SMTP
    $mail->Host       = 'smtp.qcloudmail.com';                  //Set the SMTP server to send through
    $mail->Username   = 'abc@qq.aa.com';          //SMTP username
    $mail->Password   = '123456';                  //SMTP password

    $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;            //Enable implicit TLS encryption
    $mail->CharSet 	  = PHPMailer::CHARSET_UTF8;
    $mail->CharSet 	  = 'UTF-8';
    $mail->ContentType = 'text/plain; charset=UTF-8';
    $mail->Encoding   = PHPMailer::ENCODING_BASE64;
    //$mail->Encoding   = '8bit';
    $mail->Port       = 465;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`

    //Recipients
    $mail->setFrom('abc@qq.aa.com', 'fromName');
    $mail->addAddress('test@test.com', 'toName');    //Add a recipient
    //$mail->addAddress('ellen@example.com');                   //Name is optional
    //$mail->addReplyTo('info@example.com', 'Information');
    //$mail->addCC('cc@example.com');
    //$mail->addBCC('bcc@example.com');

    //Attachments
    $mail->addAttachment('./tmp.txt');         	                //Add attachments
    //$mail->addAttachment('/tmp/image.jpg', 'new.jpg');    	//Optional name

    //Content
    //$mail->isHTML(true);                                        //Set email format to HTML
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';
    //$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}

```
