-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: mentalhealth
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_affirmation`
--

DROP TABLE IF EXISTS `myapp_affirmation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_affirmation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  `text` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_appsettings`
--

DROP TABLE IF EXISTS `myapp_appsettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_appsettings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `auto_speak_ai` tinyint(1) NOT NULL,
  `voice_input_enabled` tinyint(1) NOT NULL,
  `high_contrast` tinyint(1) NOT NULL,
  `dyslexia_friendly_font` tinyint(1) NOT NULL,
  `icon_only_navigation` tinyint(1) NOT NULL,
  `font_size` varchar(2) COLLATE utf8mb4_unicode_ci NOT NULL,
  `app_language` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dark_mode` tinyint(1) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `myapp_appsettings_user_id_e49da30b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_bodyscansession`
--

DROP TABLE IF EXISTS `myapp_bodyscansession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_bodyscansession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `started_at` datetime(6) NOT NULL,
  `ended_at` datetime(6) DEFAULT NULL,
  `total_seconds` int unsigned NOT NULL,
  `steps_total` int unsigned NOT NULL,
  `steps_completed` int unsigned NOT NULL,
  `is_completed` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_bodyscansession_user_id_fc5331b9_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_bodyscansession_user_id_fc5331b9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_bodyscansession_chk_1` CHECK ((`total_seconds` >= 0)),
  CONSTRAINT `myapp_bodyscansession_chk_2` CHECK ((`steps_total` >= 0)),
  CONSTRAINT `myapp_bodyscansession_chk_3` CHECK ((`steps_completed` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_bodyscanstep`
--

DROP TABLE IF EXISTS `myapp_bodyscanstep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_bodyscanstep` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  `emoji` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `instructions` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `position_tip` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `order` int unsigned NOT NULL,
  `tense_seconds` int unsigned NOT NULL,
  `hold_seconds` int unsigned NOT NULL,
  `release_seconds` int unsigned NOT NULL,
  `rest_seconds` int unsigned NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `myapp_bodyscanstep_chk_1` CHECK ((`order` >= 0)),
  CONSTRAINT `myapp_bodyscanstep_chk_2` CHECK ((`tense_seconds` >= 0)),
  CONSTRAINT `myapp_bodyscanstep_chk_3` CHECK ((`hold_seconds` >= 0)),
  CONSTRAINT `myapp_bodyscanstep_chk_4` CHECK ((`release_seconds` >= 0)),
  CONSTRAINT `myapp_bodyscanstep_chk_5` CHECK ((`rest_seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_bodyscansteplog`
--

DROP TABLE IF EXISTS `myapp_bodyscansteplog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_bodyscansteplog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phase` varchar(10) NOT NULL,
  `seconds` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `session_id` bigint NOT NULL,
  `step_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_bodyscansteplo_session_id_38a313b8_fk_myapp_bod` (`session_id`),
  KEY `myapp_bodyscansteplog_step_id_a4903b67_fk_myapp_bodyscanstep_id` (`step_id`),
  CONSTRAINT `myapp_bodyscansteplo_session_id_38a313b8_fk_myapp_bod` FOREIGN KEY (`session_id`) REFERENCES `myapp_bodyscansession` (`id`),
  CONSTRAINT `myapp_bodyscansteplog_step_id_a4903b67_fk_myapp_bodyscanstep_id` FOREIGN KEY (`step_id`) REFERENCES `myapp_bodyscanstep` (`id`),
  CONSTRAINT `myapp_bodyscansteplog_chk_1` CHECK ((`seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=369 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_chatmessage`
--

DROP TABLE IF EXISTS `myapp_chatmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_chatmessage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `role` varchar(20) NOT NULL,
  `content` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `session_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chatmessage_session_id_97ce9cf7_fk_myapp_chatsession_id` (`session_id`),
  CONSTRAINT `myapp_chatmessage_session_id_97ce9cf7_fk_myapp_chatsession_id` FOREIGN KEY (`session_id`) REFERENCES `myapp_chatsession` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=271 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_chatsession`
--

DROP TABLE IF EXISTS `myapp_chatsession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_chatsession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `title` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_chatsession_user_id_b1fb3458_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_chatsession_user_id_b1fb3458_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_creativedrawing`
--

DROP TABLE IF EXISTS `myapp_creativedrawing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_creativedrawing` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `prompt_text` varchar(255) NOT NULL,
  `image` varchar(100) NOT NULL,
  `strokes` int unsigned NOT NULL,
  `duration_seconds` int unsigned NOT NULL,
  `brush_size` int unsigned NOT NULL,
  `color_hex` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_creativedrawing_user_id_6141c279_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_creativedrawing_user_id_6141c279_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_creativedrawing_chk_1` CHECK ((`strokes` >= 0)),
  CONSTRAINT `myapp_creativedrawing_chk_2` CHECK ((`duration_seconds` >= 0)),
  CONSTRAINT `myapp_creativedrawing_chk_3` CHECK ((`brush_size` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_dailymotivationquote`
--

DROP TABLE IF EXISTS `myapp_dailymotivationquote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_dailymotivationquote` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_feedback`
--

DROP TABLE IF EXISTS `myapp_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `rating` smallint unsigned DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_user_id_1a72ee6f_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_feedback_user_id_1a72ee6f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_feedback_chk_1` CHECK ((`rating` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_gratitudeentry`
--

DROP TABLE IF EXISTS `myapp_gratitudeentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_gratitudeentry` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category` varchar(20) NOT NULL,
  `text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_gratitudeentry_user_id_a5a0edf9_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_gratitudeentry_user_id_a5a0edf9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_gratitudeprompt`
--

DROP TABLE IF EXISTS `myapp_gratitudeprompt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_gratitudeprompt` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_journalentry`
--

DROP TABLE IF EXISTS `myapp_journalentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_journalentry` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_journalentry_user_id_3625838b_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_journalentry_user_id_3625838b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_meditationprogram`
--

DROP TABLE IF EXISTS `myapp_meditationprogram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_meditationprogram` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(120) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `duration_seconds` int unsigned NOT NULL,
  `audio_url` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `audio` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `myapp_meditationprogram_chk_1` CHECK ((`duration_seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_meditationsession`
--

DROP TABLE IF EXISTS `myapp_meditationsession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_meditationsession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `started_at` datetime(6) NOT NULL,
  `ended_at` datetime(6) DEFAULT NULL,
  `duration_seconds` int unsigned NOT NULL,
  `is_completed` tinyint(1) NOT NULL,
  `program_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_meditationsess_program_id_5740d186_fk_myapp_med` (`program_id`),
  KEY `myapp_meditationsession_user_id_448609ba_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_meditationsess_program_id_5740d186_fk_myapp_med` FOREIGN KEY (`program_id`) REFERENCES `myapp_meditationprogram` (`id`),
  CONSTRAINT `myapp_meditationsession_user_id_448609ba_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_meditationsession_chk_1` CHECK ((`duration_seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_moodanswer`
--

DROP TABLE IF EXISTS `myapp_moodanswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_moodanswer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `answer_text` varchar(255) NOT NULL,
  `checkin_id` bigint NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `question_no` smallint unsigned NOT NULL,
  `question_text` varchar(255) NOT NULL,
  `selected_option_text` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_moodanswer_checkin_id_question_no_cf49a444_uniq` (`checkin_id`,`question_no`),
  KEY `myapp_moodanswer_checkin_id_958ef3c1` (`checkin_id`),
  CONSTRAINT `myapp_moodanswer_checkin_id_958ef3c1_fk_myapp_moodcheckin_id` FOREIGN KEY (`checkin_id`) REFERENCES `myapp_moodcheckin` (`id`),
  CONSTRAINT `myapp_moodanswer_chk_1` CHECK ((`question_no` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_moodcheckin`
--

DROP TABLE IF EXISTS `myapp_moodcheckin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_moodcheckin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mood` varchar(20) NOT NULL,
  `stress_level` smallint unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_moodcheckin_user_id_0f772369_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_moodcheckin_user_id_0f772369_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_moodcheckin_chk_1` CHECK ((`stress_level` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_moodoption`
--

DROP TABLE IF EXISTS `myapp_moodoption`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_moodoption` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `text` varchar(120) NOT NULL,
  `question_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_moodoption_question_id_68d6d496_fk_myapp_moodquestion_id` (`question_id`),
  CONSTRAINT `myapp_moodoption_question_id_68d6d496_fk_myapp_moodquestion_id` FOREIGN KEY (`question_id`) REFERENCES `myapp_moodquestion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_moodquestion`
--

DROP TABLE IF EXISTS `myapp_moodquestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_moodquestion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mood` varchar(20) NOT NULL,
  `order` smallint unsigned NOT NULL,
  `text` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_moodquestion_mood_order_e9d6e524_uniq` (`mood`,`order`),
  CONSTRAINT `myapp_moodquestion_chk_1` CHECK ((`order` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_moodsession`
--

DROP TABLE IF EXISTS `myapp_moodsession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_moodsession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mood` varchar(20) NOT NULL,
  `stress_level` smallint unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_completed` tinyint(1) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_moodsession_user_id_5b06fc8e_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_moodsession_user_id_5b06fc8e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_moodsession_chk_1` CHECK ((`stress_level` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_musictrack`
--

DROP TABLE IF EXISTS `myapp_musictrack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_musictrack` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mood` varchar(20) NOT NULL,
  `title` varchar(120) NOT NULL,
  `description` varchar(255) NOT NULL,
  `duration_seconds` int unsigned NOT NULL,
  `audio` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `audio_url` varchar(200) DEFAULT NULL,
  `category` varchar(20) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `myapp_musictrack_chk_2` CHECK ((`duration_seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=187 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_passwordresetotp`
--

DROP TABLE IF EXISTS `myapp_passwordresetotp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_passwordresetotp` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `otp` varchar(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_verified` tinyint(1) NOT NULL,
  `reset_token` char(32) DEFAULT NULL,
  `reset_token_created_at` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_passwordresetotp_email_292aa744` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_soundplay`
--

DROP TABLE IF EXISTS `myapp_soundplay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_soundplay` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `started_at` datetime(6) NOT NULL,
  `ended_at` datetime(6) DEFAULT NULL,
  `duration_seconds` int unsigned NOT NULL,
  `track_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_soundplay_track_id_ef5f7b8c_fk_myapp_musictrack_id` (`track_id`),
  KEY `myapp_soundplay_user_id_d21e3865_fk_auth_user_id` (`user_id`),
  CONSTRAINT `myapp_soundplay_track_id_ef5f7b8c_fk_myapp_musictrack_id` FOREIGN KEY (`track_id`) REFERENCES `myapp_musictrack` (`id`),
  CONSTRAINT `myapp_soundplay_user_id_d21e3865_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_soundplay_chk_1` CHECK ((`duration_seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=1425 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_useraffirmationstate`
--

DROP TABLE IF EXISTS `myapp_useraffirmationstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_useraffirmationstate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `is_favorite` tinyint(1) NOT NULL,
  `view_count` int unsigned NOT NULL,
  `listened_seconds` int unsigned NOT NULL,
  `last_viewed_at` datetime(6) DEFAULT NULL,
  `affirmation_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_useraffirmationstate_user_id_affirmation_id_4269cde8_uniq` (`user_id`,`affirmation_id`),
  KEY `myapp_useraffirmatio_affirmation_id_5a940cd0_fk_myapp_aff` (`affirmation_id`),
  CONSTRAINT `myapp_useraffirmatio_affirmation_id_5a940cd0_fk_myapp_aff` FOREIGN KEY (`affirmation_id`) REFERENCES `myapp_affirmation` (`id`),
  CONSTRAINT `myapp_useraffirmationstate_user_id_05d25d9a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_useraffirmationstate_chk_1` CHECK ((`view_count` >= 0)),
  CONSTRAINT `myapp_useraffirmationstate_chk_2` CHECK ((`listened_seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_usermusicstats`
--

DROP TABLE IF EXISTS `myapp_usermusicstats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_usermusicstats` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `listening_seconds_total` int unsigned NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `myapp_usermusicstats_user_id_93f45eb8_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_usermusicstats_chk_1` CHECK ((`listening_seconds_total` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_userprofile`
--

DROP TABLE IF EXISTS `myapp_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_userprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `phone` varchar(20) DEFAULT NULL,
  `age` int unsigned DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `user_id` int NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `myapp_userprofile_user_id_8f877d36_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_userprofile_chk_1` CHECK ((`age` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `myapp_userstats`
--

DROP TABLE IF EXISTS `myapp_userstats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `myapp_userstats` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `level` int unsigned NOT NULL,
  `coins` int unsigned NOT NULL,
  `xp_current` int unsigned NOT NULL,
  `xp_target` int unsigned NOT NULL,
  `streak_days` int unsigned NOT NULL,
  `last_streak_date` date DEFAULT NULL,
  `daily_quote_date` date DEFAULT NULL,
  `daily_quote_id` bigint DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `myapp_userstats_daily_quote_id_81be8166_fk_myapp_dai` (`daily_quote_id`),
  CONSTRAINT `myapp_userstats_daily_quote_id_81be8166_fk_myapp_dai` FOREIGN KEY (`daily_quote_id`) REFERENCES `myapp_dailymotivationquote` (`id`),
  CONSTRAINT `myapp_userstats_user_id_54db117b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `myapp_userstats_chk_1` CHECK ((`level` >= 0)),
  CONSTRAINT `myapp_userstats_chk_2` CHECK ((`coins` >= 0)),
  CONSTRAINT `myapp_userstats_chk_3` CHECK ((`xp_current` >= 0)),
  CONSTRAINT `myapp_userstats_chk_4` CHECK ((`xp_target` >= 0)),
  CONSTRAINT `myapp_userstats_chk_5` CHECK ((`streak_days` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-25  8:22:18
