```java
import java.util.Random;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

import sun.misc.BASE64Encoder;

public class UgcSign {
	public long m_qwNowTime;

	public String m_strFileName;
	public String m_strFileSha;

	public String m_strFileType;
	public int m_iRandom;

	public String m_strSecId = "AKIDR20GpXsc4fixxxxxxxbuWQCeTpw9ljzt";
	public String m_strSecKey = "wGxKo4cu6WFBWxxxxxxxbH7BTTiUn4bV";

	public int m_isTrans = 0;
	public int m_isScreenShot = 0;
	public int m_isWaterMark = 0;

	public int m_iClassId = 0;
	public int m_iSignValidDuration = 3600 * 24 * 2;

	public String m_strUid;

	private static final String HMAC_ALGORITHM = "HmacSHA1";
	private static final String CONTENT_CHARSET = "UTF-8";

	public static byte[] byteMerger(byte[] byte_1, byte[] byte_2) {
		byte[] byte_3 = new byte[byte_1.length + byte_2.length];
		System.arraycopy(byte_1, 0, byte_3, 0, byte_1.length);
		System.arraycopy(byte_2, 0, byte_3, byte_1.length, byte_2.length);
		return byte_3;
	}

	String GetUgcExSign() {
		String strSign = "";
		String contextStr = "";
		long endTime = (m_qwNowTime + m_iSignValidDuration);
		try {
			contextStr += "f=" + java.net.URLEncoder.encode(m_strFileName, "utf8");
			contextStr += "&fs=" + this.m_strFileSha;
			contextStr += "&ft=" + this.m_strFileType;

			contextStr += "&t=" + this.m_qwNowTime;
			contextStr += "&e=" + endTime;
			contextStr += "&r=" + this.m_iRandom;
			contextStr += "&s=" + java.net.URLEncoder.encode(this.m_strSecId, "utf8");
			contextStr += "&uid=" + m_strUid;
			contextStr += "&tc=" + this.m_isTrans;
			contextStr += "&ss=" + this.m_isScreenShot;
			contextStr += "&wm=" + this.m_isWaterMark;

			if (this.m_iClassId != 0) {
				contextStr += "&cid=" + this.m_iClassId;
			}

			String s = contextStr;
			String sig = null;
			Mac mac = Mac.getInstance(HMAC_ALGORITHM);
			SecretKeySpec secretKey = new SecretKeySpec(m_strSecKey.getBytes(CONTENT_CHARSET), mac.getAlgorithm());
			mac.init(secretKey);
			byte[] hash = mac.doFinal(contextStr.getBytes(CONTENT_CHARSET));
			byte[] sigBuf = byteMerger(hash, contextStr.getBytes("utf8"));
			// base64
			strSign = new String(new BASE64Encoder().encode(sigBuf).getBytes());
			// Echo(strSign);
		} catch (Exception e) {
			System.out.printf(e.toString());
			return "";
		}
		return strSign;
	}
}

class Test {
	public static void main(String[] args) {
		UgcSign sign = new UgcSign();
		//从https://console.cloud.tencent.com/capi获取，分别对应SecretId和SecretKey
		sign.m_strSecId = "AKIDR20GpXsc4fixxxxxxxbuWQCeTpw9ljzt";
		sign.m_strSecKey = "wGxKo4cu6WFBWxxxxxxxbH7BTTiUn4bV";
		
		//当前时间
		sign.m_qwNowTime = System.currentTimeMillis() / 1000;
		sign.m_iRandom = new Random().nextInt(java.lang.Integer.MAX_VALUE);
		
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

		System.out.printf(sign.GetUgcExSign());
	}
}

```