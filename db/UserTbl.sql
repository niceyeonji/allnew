CREATE TABLE userTBL -- ȸ�� ���̺�
(userID CHAR(8) NOT NULL PRIMARY KEY, -- ����� ���̵�(PK)
userName NVARCHAR2(10) NOT NULL, -- �̸�
birthYear NUMBER(4) NOT NULL, --����⵵
addr NCHAR(2) NOT NULL, -- ����(���, ����, �泲 ������ 2���ڸ� �Է�)
mobile1 CHAR(3), -- �޴����� ����(010, 011, 016, 017, 018, 019 ��)
mobile2 CHAR(8), -- �޴����� ������ ��ȭ��ȣ(������ ����)
height NUMBER(3), -- Ű
mDate DATE -- ȸ�� ������
);

INSERT INTO userTBL VALUES('LSG', '�̽±�', 1987, '����', '011', '11111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES('KBS', '�����', 1979, '�泲', '011', '22222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES('KKH', '���ȣ', 1971, '����', '019', '33333333', 177, '2007-7-7');
INSERT INTO userTBL VALUES('JYP', '������', 1950, '���', '011', '44444444', 166, '2009-4-4');
INSERT INTO userTBL VALUES('SSK', '���ð�', 1979, '����', NULL , NULL , 186, '2013-12-12');
INSERT INTO userTBL VALUES('LJB', '�����', 1963, '����', '016', '66666666', 182, '2009-9-9');
INSERT INTO userTBL VALUES('YJS', '������', 1969, '�泲', NULL , NULL , 170, '2005-5-5');
INSERT INTO userTBL VALUES('EJW', '������', 1972, '���', '011', '88888888', 174, '2014-3-3');
INSERT INTO userTBL VALUES('JKW', '������', 1965, '���', '018', '99999999', 172, '2010-10-10');
INSERT INTO userTBL VALUES('BBK', '�ٺ�Ŵ', 1973, '����', '010', '00000000', 176, '2013-5-5');

