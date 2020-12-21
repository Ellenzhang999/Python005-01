-- 创建3张表

/*
drop table account;
drop table finance;
drop table auditinfo;
*/

--一张为用户表，包含用户 ID 和用户名字，
CREATE TABLE account (
	account_id INTEGER NOT NULL primary key,
	account_name VARCHAR(50),
    created_on DATETIME
);

Create index idx_account_name on account(account_name);

--另一张为用户资产表，包含用户 ID 用户总资产，
CREATE TABLE finance (
    account_id INTEGER primary key,
    balance decimal(11,2),
    created_on DATETIME,
    updated_on DATETIME,
    FOREIGN KEY (account_id)
        REFERENCES account(account_id)
        ON DELETE CASCADE
);

--第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
CREATE TABLE auditinfo (
    audit_id INTEGER auto_increment primary key,
    account_id_from INTEGER,
    account_id_to INTEGER,
    transfer_amt decimal(11,2),
    transfer_time DATETIME,
    created_on DATETIME default now(),
    FOREIGN KEY (account_id_from)
        REFERENCES account(account_id)
        ON DELETE CASCADE,        
    FOREIGN KEY (account_id_to)
        REFERENCES account(account_id)
        ON DELETE CASCADE
);

-- mock data
insert into account values(1, 'user1', now());
insert into account values(2, 'user2', now());

insert into finance values(1, 1000, now(), null);
insert into finance values(2, 500, now(), null);



