--------------------------------------------------------
--  파일이 생성됨 - 화요일-3월-28-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table MEMBERTBL
--------------------------------------------------------

  CREATE TABLE "HR"."MEMBERTBL" 
   (	"MEMBERID" CHAR(8 BYTE), 
	"MEMBERNAME" NCHAR(5), 
	"MEMBERADDRESS" NCHAR(20)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into HR.MEMBERTBL
SET DEFINE OFF;
Insert into HR.MEMBERTBL (MEMBERID,MEMBERNAME,MEMBERADDRESS) values ('Dang    ','당탕이  ','경기 부천시 중동           ');
Insert into HR.MEMBERTBL (MEMBERID,MEMBERNAME,MEMBERADDRESS) values ('Jee     ','지운이  ','서울 은평구 중산동          ');
Insert into HR.MEMBERTBL (MEMBERID,MEMBERNAME,MEMBERADDRESS) values ('Han     ','한주연  ','인천 남구 주안동           ');
Insert into HR.MEMBERTBL (MEMBERID,MEMBERNAME,MEMBERADDRESS) values ('Sang    ','상길이  ','경기 성남시 분당구          ');
--------------------------------------------------------
--  DDL for Index MEMBERTBL_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."MEMBERTBL_PK" ON "HR"."MEMBERTBL" ("MEMBERID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Trigger TRG_DELETEDMEMBERTBL
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "HR"."TRG_DELETEDMEMBERTBL" 
    after delete
    on membertbl
    for each row
begin
    insert into deletedmembertbl
    values (:old.memberid, :old.membername, :old.memberaddress, SYSDATE());
end ;
/
ALTER TRIGGER "HR"."TRG_DELETEDMEMBERTBL" ENABLE;
--------------------------------------------------------
--  Constraints for Table MEMBERTBL
--------------------------------------------------------

  ALTER TABLE "HR"."MEMBERTBL" ADD CONSTRAINT "MEMBERTBL_PK" PRIMARY KEY ("MEMBERID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HR"."MEMBERTBL" MODIFY ("MEMBERNAME" NOT NULL ENABLE);
  ALTER TABLE "HR"."MEMBERTBL" MODIFY ("MEMBERID" NOT NULL ENABLE);
