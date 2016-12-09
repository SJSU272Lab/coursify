-- MySQL dump 10.13  Distrib 5.7.16, for Linux (x86_64)
--
-- Host: localhost    Database: college_courses
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


 CREATE DATABASE `college_courses`;
USE college_courses;
--
-- Table structure for table `corequisite`
--

DROP TABLE IF EXISTS `corequisite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `corequisite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(80) NOT NULL,
  `coreq_course` varchar(80) NOT NULL,
  `primary_course` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corequisite`
--

LOCK TABLES `corequisite` WRITE;
/*!40000 ALTER TABLE `corequisite` DISABLE KEYS */;
INSERT INTO `corequisite` VALUES (1,'Software engineering','CMPE 130','CMPE 142'),(2,'Software engineering','CMPE 125','CMPE 127'),(3,'Software engineering','CMPE 110','CMPE 124'),(4,'Software engineering','CMPE 275','CMPE 276'),(5,'Software engineering','CMPE 272','CMPE 273'),(6,'Software engineering','CMPE 220','CMPE 225'),(7,'Mathematics and Statistics Department','MATH 030','CMPE 030'),(8,'Software engineering','CMPE 125','CMPE 127'),(9,'Software engineering','CMPE 242','CMPE 262'),(10,'Software engineering','CMPE 272','CMPE 281'),(11,'Software engineering','CMPE 202','CMPE 285'),(12,'Software engineering','CMPE 220','CMPE 285');
/*!40000 ALTER TABLE `corequisite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(80) NOT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Software Engineering'),(2,'Computer Engineering'),(3,'Electrical Engineering'),(4,'Computer Science');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `majorcourse`
--

DROP TABLE IF EXISTS `majorcourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `majorcourse` (
  `dept_name` varchar(80) NOT NULL,
  `major_course` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `majorcourse`
--

LOCK TABLES `majorcourse` WRITE;
/*!40000 ALTER TABLE `majorcourse` DISABLE KEYS */;
INSERT INTO `majorcourse` VALUES ('Software Engineering','Cloud computing and virtualization'),('Software Engineering','Software systems engineering'),('Software Engineering','Enterprise software technology'),('Software Engineering','Networking software');
/*!40000 ALTER TABLE `majorcourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `minorcourse`
--

DROP TABLE IF EXISTS `minorcourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `minorcourse` (
  `dept_name` varchar(80) NOT NULL,
  `minor_course` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minorcourse`
--

LOCK TABLES `minorcourse` WRITE;
/*!40000 ALTER TABLE `minorcourse` DISABLE KEYS */;
INSERT INTO `minorcourse` VALUES ('Software Engineering','Networking software'),('Software Engineering','Cloud computing and virtualization'),('Software Engineering','Enterprise software technology'),('Software Engineering','Software systems Engineering');
/*!40000 ALTER TABLE `minorcourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prerequisite`
--

DROP TABLE IF EXISTS `prerequisite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prerequisite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dept_name` varchar(80) NOT NULL,
  `prereq_course` varchar(80) NOT NULL,
  `primary_course` varchar(80) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prerequisite`
--

LOCK TABLES `prerequisite` WRITE;
/*!40000 ALTER TABLE `prerequisite` DISABLE KEYS */;
INSERT INTO `prerequisite` VALUES (1,'Software engineering','CMPE 131','CMPE 133'),(2,'Software engineering','CMPE 126','CMPE 132'),(3,'Software engineering','CMPE 126','CMPE 138'),(4,'Software engineering','CMPE 102','CMPE 142'),(5,'Software engineering','CMPE 126','CMPE 142'),(6,'Software engineering','CMPE 131','CMPE 137'),(7,'Software engineering','CMPE 125','CMPE 140'),(8,'Software engineering','CMPE 131','CMPE 136'),(9,'Software engineering','CMPE 135','CMPE 136'),(10,'Software engineering','CMPE 126','CMPE 130'),(11,'Software engineering','SE 130','CMPE 130'),(12,'Software engineering','CMPE 050','CMPE 126'),(13,'Software engineering','CMPE 124','CMPE 125'),(14,'Software engineering','CMPE 299A','CMPE 299B'),(15,'Software engineering','CMPE 295A','CMPE 295B'),(16,'Software engineering','CMPE 295W','CMPE 295B'),(17,'Software engineering','CMPE 200','CMPE 290'),(18,'Software engineering','CMPE 272','CMPE 289'),(19,'Software engineering','CMPE 202','CMPE 287'),(20,'Software engineering','CMPE 285','CMPE 286'),(21,'Software engineering','CMPE 272','CMPE 283'),(22,'Software engineering','CMPE 283','CMPE 284'),(23,'Software engineering','CMPE 281','CMPE 282'),(24,'Software engineering','CMPE 202','CMPE 279'),(25,'Software engineering','CMPE 220','CMPE 279'),(26,'Software engineering','CMPE 272','CMPE 274'),(27,'Software engineering','CMPE 275','CMPE 278'),(28,'Software engineering','CMPE 273','CMPE 276'),(29,'Software engineering','CMPE 273','CMPE 275'),(30,'Software engineering','CMPE 200','CMPE 265'),(31,'Software engineering','CMPE 200','CMPE 264'),(32,'Software engineering','CMPE 240','CMPE 261'),(33,'Software engineering','CMPE 250','CMPE 251'),(34,'Software engineering','CMPE 240','CMPE 245'),(35,'Software engineering','CMPE 200','CMPE 244'),(36,'Software engineering','CMPE 220','CMPE 244'),(37,'Software engineering','CMPE 242','CMPE 243'),(38,'Software engineering','CMPE 200','CMPE 242'),(39,'Software engineering','CMPE 240','CMPE 241'),(40,'Software engineering','CMPE 127','CMPE 240'),(41,'Software engineering','CMPE 272','CMPE 239'),(42,'Software engineering','CMPE 220','CMPE 238'),(43,'Software engineering','CMPE 221','CMPE 238'),(44,'Software engineering','CMPE 202','CMPE 237'),(45,'Software engineering','CMPE 220','CMPE 237'),(46,'Software engineering','CMPE 271','CMPE 237'),(47,'Software engineering','CMPE 202','CMPE 236'),(48,'Software engineering','CMPE 202','CMPE 235'),(49,'Software engineering','CMPE 220','CMPE 235'),(50,'Software engineering','CMPE 142','CMPE 234'),(51,'Software engineering','CMPE 220','CMPE 234'),(52,'Software engineering','CMPE 220','CMPE 232'),(53,'Software engineering','CMPE 221','CMPE 232'),(54,'Software engineering','CMPE 271','CMPE 232'),(55,'Software engineering','CMPE 220','CMPE 227'),(56,'Software engineering','CMPE 272','CMPE 226'),(57,'Software engineering','CMPE 142','CMPE 225'),(58,'Software engineering','CMPE 275','CMPE 221'),(59,'Software engineering','CMPE 200','CMPE 212'),(60,'Software engineering','CMPE 264','CMPE 212'),(61,'Software engineering','CMPE 206','CMPE 210'),(62,'Software engineering','CMPE 206','CMPE 209'),(63,'Software engineering','CMPE 206','CMPE 208'),(64,'Software engineering','CMPE 206','CMPE 207'),(65,'Software engineering','CMPE 195A','CMPE 195B'),(66,'Software engineering','CMPE 131','CMPE 187'),(67,'Software engineering','CMPE 142','CMPE 172'),(68,'Software engineering','CMPE 104','CMPE 168'),(69,'Software engineering','CMPE 133','CMPE 168'),(70,'Software engineering','CMPE 138','CMPE 168'),(71,'Software engineering','CMPE 133','CMPE 165'),(72,'Software engineering','CMPE 127','CMPE 164'),(73,'Software engineering','CMPE 140','CMPE 164'),(74,'Software engineering','CMPE 127','CMPE 163'),(75,'Software engineering','CMPE 102','CMPE 152'),(76,'Software engineering','CMPE 126','CMPE 152'),(77,'Software engineering','CMPE 110','CMPE 150'),(78,'Software engineering','CMPE 124','CMPE 150'),(79,'Software engineering','CMPE 148','CMPE 149'),(80,'Software engineering','CMPE 125','CMPE 147'),(81,'Software engineering','CMPE 110','CMPE 146'),(82,'Software engineering','CMPE 127','CMPE 146'),(83,'Software engineering','CMPE 127','CMPE 143'),(84,'Software engineering','CMPE 050','CMPE 120'),(85,'Software engineering','CMPE 050','CMPE 104'),(86,'Software engineering','CMPE 050','CMPE 102'),(87,'Software engineering','CMPE 030','CMPE 050'),(88,'Software engineering','CMPE 126','CMPE 135'),(89,'Software engineering','CMPE 124','CMPE 148'),(90,'Software engineering','CMPE 126','CMPE 148'),(91,'Software engineering','CMPE 127','CMPE 195A'),(92,'Software engineering','CMPE 046','CMPE 101'),(93,'Electric engineering','EE 98','CMPE 110'),(94,'Mathematics and Statistics Department','MATH 123','CMPE 110'),(95,'Electric engineering','EE 98','CMPE 124'),(96,'Electric engineering','EE 97','CMPE 124'),(97,'Software engineering','CMPE 126','CMPE 131'),(98,'Software engineering','CMPE 126','CMPE 139'),(99,'Software engineering','CMPE 126','CMPE 188'),(100,'Software engineering','CMPE 130','CMPE 195A'),(101,'Software engineering','CMPE 131','CMPE 195A');
/*!40000 ALTER TABLE `prerequisite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `technology`
--

DROP TABLE IF EXISTS `technology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `technology` (
  `dept_name` varchar(80) NOT NULL,
  `interest_tech` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `technology`
--

LOCK TABLES `technology` WRITE;
/*!40000 ALTER TABLE `technology` DISABLE KEYS */;
INSERT INTO `technology` VALUES ('Software Engineering','Apache Spark'),('Software Engineering','Restful web services'),('Software Engineering','Python programming'),('Software Engineering','IBM Bluemix Services'),('Software Engineering','Hadoop architecture'),('Software Engineering','AWS Services'),('Software Engineering','Google Appengine'),('Software Engineering','Big Data analysis'),('Software Engineering','Web UI development'),('Software Engineering','Mobile application development');
/*!40000 ALTER TABLE `technology` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-08  2:42:52
