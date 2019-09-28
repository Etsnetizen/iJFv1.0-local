/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 5.7.24-log : Database - jfbz
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`jfbz` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `jfbz`;

/*Data for the table `user` */

insert  into `user`(`uid`,`nickname`,`mobile`,`login_name`,`login_pwd`,`login_salt`,`status`,`updated_time`,`created_time`) values (1,'root','11012345679','root','816440c40b7a9d55ff9eb7b20760862c','cF3JfH5FJfQ8B2Ba',1,'2017-03-15 14:08:48','2017-03-15 14:08:48');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
