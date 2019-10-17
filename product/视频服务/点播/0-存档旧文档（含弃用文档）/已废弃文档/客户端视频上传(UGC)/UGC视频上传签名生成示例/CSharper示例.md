```csharper
using System;
using System.Security.Cryptography;
using System.Text;
using System.Threading;

namespace GetUgcSign
{
    class UgcSign
    {
        public string m_strSecId;
        public string m_strSecKey;

        public string m_strFileName;
        public string m_strFileSha;

        public string m_strFileType;

        public string m_strUid;
        public int m_iRandom;

        public int m_isTrans = 0;
        public int m_isScreenShot = 0;
        public int m_isWaterMark = 0;

        public int m_iClassId;

        public long m_qwNowTime;
        public int m_iSignValidDuration;
        public static long GetIntTimeStamp()
        {
            TimeSpan ts = DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, 0);
            return Convert.ToInt64(ts.TotalSeconds);
        }
        private byte[] hash_hmac_byte(string signatureString, string secretKey)
        {
            var enc = Encoding.UTF8;
            HMACSHA1 hmac = new HMACSHA1(enc.GetBytes(secretKey));
            hmac.Initialize();

            byte[] buffer = enc.GetBytes(signatureString);
            return hmac.ComputeHash(buffer);
        }
        public string GetSign()
        {
            string strContent = "";
            strContent += ("s=" + Uri.EscapeDataString((m_strSecId)));
            strContent += ("&f=" + Uri.EscapeDataString(m_strFileName));
            strContent += ("&t=" + m_qwNowTime);
            strContent += ("&ft=" + m_strFileType);
            strContent += ("&e=" + m_qwNowTime + m_iSignValidDuration);
            strContent += ("&fs=" + m_strFileSha);
            strContent += ("&uid=" + m_strUid);
            strContent += ("&r=" + m_iRandom);

            strContent += "&tc=" + m_isTrans;
            strContent += "&ss=" + m_isScreenShot;
            strContent += "&wm=" + m_isWaterMark;

            byte[] bytesSign = hash_hmac_byte(strContent, m_strSecKey);
            byte[] byteContent = System.Text.Encoding.Default.GetBytes(strContent);
            byte[] nCon = new byte[bytesSign.Length + byteContent.Length];
            bytesSign.CopyTo(nCon, 0);
            byteContent.CopyTo(nCon, bytesSign.Length);
            return Convert.ToBase64String(nCon);      
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            UgcSign sign = new UgcSign();
            //从https://console.cloud.tencent.com/capi获取，分别对应SecretId和SecretKey
            sign.m_strSecId = "AKIDR20GpXsc4fixxxxxxxbuWQCeTpw9ljzt";
            sign.m_strSecKey = "wGxKo4cu6WFBWxxxxxxxbH7BTTiUn4bV";

            //当前时间
            sign.m_qwNowTime = UgcSign.GetIntTimeStamp();
            sign.m_iRandom = new Random().Next(0, 1000000);

            //上传者在app内的唯一标识，如果不需要，可以保持不变
            sign.m_strUid = "123";

            //文件名
            sign.m_strFileName = "test";
            //文件sha。由客户端算好带到后台
            sign.m_strFileSha = "534928ad7165be24caaaaaf28568be23497f1467";
            //文件类型
            sign.m_strFileType = "mp4";
            //分类id
            sign.m_iClassId = 0;
            //签名有效期
            sign.m_iSignValidDuration = 3600 * 24 * 2;
            //转码/截图/水印开关
            sign.m_isTrans = 1;
            sign.m_isScreenShot = 1;
            sign.m_isWaterMark = 1;

            string strSign = sign.GetSign();
            Console.WriteLine(strSign);
            //Thread.Sleep(1000000);
        }
    }
}


```
