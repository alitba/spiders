/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50724
Source Host           : 127.0.0.1:3306
Source Database       : scrappy

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-11-16 18:49:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for scrappy_scrappydata
-- ----------------------------
DROP TABLE IF EXISTS `scrappy_scrappydata`;
CREATE TABLE `scrappy_scrappydata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(800) NOT NULL,
  `url_level` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `keywords` varchar(200) DEFAULT NULL,
  `description` varchar(5000) DEFAULT NULL,
  `flag` tinyint(1) NOT NULL,
  `update_timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5925 DEFAULT CHARSET=utf8;
