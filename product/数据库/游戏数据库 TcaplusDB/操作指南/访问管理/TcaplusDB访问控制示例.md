## ��������
������ͨ��ʹ�÷��ʹ���Cloud Access Management��CAM���������û�ӵ���� TcaplusDB ����̨�в鿴��ʹ���ض���Դ��Ȩ�ޡ����ĵ��ṩ�˲鿴��ʹ���ض���Դ��Ȩ��ʾ����ָ���û����ʹ�ÿ���̨���ض����ֵĲ��ԡ�


## ��������
### TcaplusDB ��ȫ��д����
�����ϣ���û�ӵ�д����͹��� TcaplusDB ʵ����Ȩ�ޣ������ԶԸ��û�ʹ������Ϊ��QcloudTcaplusDBFullAccess �Ĳ��ԡ�
�ò��Կ����û�ӵ�� TcaplusDB ��������Դ�Ĳ���Ȩ�ޡ���������������£�
�ο� [��Ȩ����](https://cloud.tencent.com/document/product/598/10602)����Ԥ����� QcloudTcaplusDBFullAccess ��Ȩ���û���

### TcaplusDB ��ֻ������
�����ϣ���û�ӵ�в�ѯ TcaplusDB ʵ����Ȩ�ޣ����ǲ����д�����ɾ�����޸ĵ�Ȩ�ޣ������ԶԸ��û�ʹ������Ϊ��QcloudTcaplusDBReadOnlyAccess �Ĳ��ԡ�
�ò��Կ����û�ӵ�� TcaplusDB �������Ե��� ��Describe�� �� ��Inquiry�� ��ͷ�Ĳ�����Ȩ�ޡ���������������£�
�ο� [��Ȩ����](https://cloud.tencent.com/document/product/598/10602)����Ԥ����� TcaplusDB ��Ȩ���û���

### ��Ȩ�û�ӵ���ض���Ⱥ�Ĳ���Ȩ�޲���
�����ϣ����Ȩ�û�ӵ���ض� TcaplusDB ����Ȩ�ޣ��ɽ����²��Թ��������û�����������������£�

1. ���� [����](https://cloud.tencent.com/document/product/598/10601)������һ���Զ�����ԡ�
��ʾ�����������û�ӵ�м�Ⱥ ID Ϊ19168929215�� TcaplusDB ��Ⱥ�����в���Ȩ�ޣ��������ݿɲο����²����﷨�������ã�
```
{
    "version": "2.0",
    "statement": [
        {
            "action": "tcaplusdb:*",
            "resource": "qcs::tcaplusdb:ap-shanghai::cluster/19168929215",
            "effect": "allow"
        }
    ]
}
```
2. �ҵ������Ĳ��ԣ��ڸò����е� �������� ���У������������û�/�顿��
3. �ڵ����� �������û�/�û��顱 �����У�ѡ������Ҫ��Ȩ���û�/�飬������ȷ������


### ��Ȩ�û�ӵ�� TcaplusDB ������Դ�Ĳ���Ȩ�޲���
�����ϣ����Ȩ�û�ӵ�� TcaplusDB ������Դ�Ĳ���Ȩ�ޣ��ɽ����²��Թ��������û�����������������£�

1. ���� [����](https://cloud.tencent.com/document/product/598/10601)������һ���Զ�����ԡ�
��ʾ�����������û�ӵ�ж� TcaplusDB ������Դ�Ĳ���Ȩ�ޣ��������ݿɲο����²����﷨�������ã�
```
{
    "version": "2.0",
    "statement": [
        {
            "action": "tcaplusdb:*",
            "resource": "qcs::tcaplusdb:::*",
            "effect": "allow"
        }
    ]
}
```
2. �ҵ������Ĳ��ԣ��ڸò����е� �������� ���У������������û�/�顿��
3. �ڵ����� �������û�/�û��顱 �����У�ѡ������Ҫ��Ȩ���û�/�飬������ȷ������


### ��ֹ�û�ӵ���ض� TcaplusDB ���ֱ�������Ȩ�޲���
�����ϣ����ֹ�û�ӵ���ض� TcaplusDB ���ֱ��Ĳ���Ȩ�ޣ��ɽ����²��Թ��������û�����������������£�

1. ���� [����](https://cloud.tencent.com/document/product/598/10601)������һ���Զ�����ԡ�
��ʾ�����Խ�ֹ�û�ӵ�жԱ��IDΪtcaplus-c8d1caa4��tcaplus-d8d1cbb4���Ĳ���Ȩ�ޣ��������ݿɲο����²����﷨�������ã�
```
{
    "version": "2.0",
    "statement": [
        {
            "action": "tcaplusdb:*",
            "resource": [
						"qcs::tcaplusdb::uin/16xxx472:table/tcaplus-c8d1caa4",
						"qcs::tcaplusdb::uin/16xxx472:table/tcaplus-d8d1cbb4",
						],
            "effect": "deny"
        }
    ]
}
```
2. �ҵ������Ĳ��ԣ��ڸò����е� �������� ���У������������û�/�顿��
3. �ڵ����� �������û�/�û��顱 �����У�ѡ������Ҫ��Ȩ���û�/�飬������ȷ������

<span id="CAMCustomPolicy"></span>
### �Զ������
���������Ԥ����Բ�����������Ҫ��������ͨ�������Զ�����ԴﵽĿ�ġ�
�������������ο� [����](https://cloud.tencent.com/document/product/598/10601)��
���� TcaplusDB ��صĲ����﷨��ο� [��Ȩ�����﷨](https://cloud.tencent.com/document/product/596/42903)��

