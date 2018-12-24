USE crypto_db;

SELECT id,user_id,title,score,comms_num,timestamp,source FROM bitcoin_reddit;

SELECT * FROM bitcoin_twitter;

alter table bitcoin_reddit add column id int auto_increment primary key;
alter table bitcoin_twitter add column id int auto_increment primary key;

ALTER TABLE bitcoin_reddit CHANGE COLUMN id id int FIRST;

SELECT * FROM bitcoin_reddit;

SELECT * FROM bitcoin_youtube order by publishAt;

ALTER TABLE bitcoin_twitter CHANGE COLUMN id id int FIRST;
