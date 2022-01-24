/*==============================================================*/
/* DBMS name:            MySQL 5.7                              */
/* 陈小龙 Created on:     2021/05/15                             */
/* 陈小龙 Updated on:     2021/12/12															*/
/*==============================================================*/

/* 创建盒子的数据库 */
CREATE DATABASE IF NOT EXISTS iot_hezi CHARACTER SET utf8;

USE iot_hezi;

/* vpn2证书表 */
CREATE TABLE IF NOT EXISTS vpn2(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,          -- VPN2证书的ID
	name VARCHAR(20) NOT NULL,                                    -- VPN2证书的名字
	owner VARCHAR(20) NOT NULL,                                   -- VPN2证书对应的用户名称
	issu_time DATETIME                                            -- 发布时间
	);


/* 用户表 */
CREATE TABLE IF NOT EXISTS users(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,          -- 用户ID
	username VARCHAR(10) NOT NULL,  														  -- 用户名
	phone VARCHAR(20) NOT NULL,  																  -- 电话号码
	password VARCHAR(20) NOT NULL, 															  -- 用户密码
	is_admin enum('管理员','普通用户') default '普通用户',       			-- 用户权限
	is_online TINYINT DEFAULT 0,                                  -- 用户在线状态：0不在线，1在线
-- 	group VARCHAR(10) NOT NULL,                                   -- 用户属于哪个分组
  vpn2_name VARCHAR(20)                                         -- 关联vpn2表的name字段
	);


/* 盒子表 */
CREATE TABLE IF NOT EXISTS hezi(
	serial_number VARCHAR(20) PRIMARY KEY,                         -- 盒子的序列号
	password VARCHAR(20) NOT NULL, 								   -- 盒子密码
	category TINYINT UNSIGNED DEFAULT 0,                           -- 盒子的分组信息
	user_id INT UNSIGNED,                                          -- 盒子对应的用户ID
	status TINYINT DEFAULT 0,                                      -- 盒子的状态，0表示不在线，1表示在线无报警，2表示在线报警
	vpn1_address VARCHAR(20),                                      -- VPN1虚拟地址
	is_bind TINYINT default 0,                                     -- 盒子是否被用户绑定，0表示未被绑定，1表示已绑定
	vpn2_name VARCHAR(20),                                         -- 关联vpn2表的name字段
	vpn2_ip VARCHAR(20),                                           -- vpn2的虚拟地址
	comments VARCHAR(20),                                          -- 备注
	FOREIGN KEY(user_id) REFERENCES users(id)                      -- 外键，关联users表的user_id字段
)