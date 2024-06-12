/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS `project_prakpemdas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `project_prakpemdas`;

CREATE TABLE IF NOT EXISTS `mahasiswa` (
  `nim` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `alamat` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `no_telp` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`nim`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT IGNORE INTO `mahasiswa` (`nim`, `nama`, `alamat`, `no_telp`, `email`, `tanggal_lahir`, `password`) VALUES
	(1, 'Daffa', 'Bandung', '087770605879', 'daffa@email.com', '2004-01-01', 'daffa'),
	(3, 'Deli', 'Karawang', '081221324312', 'deli@email.com', '2004-12-03', 'deli'),
	(4, 'Junior', 'Bandun', '08121233123', 'junior@roin.com', '2004-12-12', 'junior');

CREATE TABLE IF NOT EXISTS `matkul` (
  `kode` int NOT NULL AUTO_INCREMENT,
  `nama` varchar(50) NOT NULL DEFAULT '',
  `sks` int NOT NULL,
  PRIMARY KEY (`kode`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT IGNORE INTO `matkul` (`kode`, `nama`, `sks`) VALUES
	(1, 'Pemrograman Dasar', 4),
	(2, 'Pemrograman Bassist Data', 3);

CREATE TABLE IF NOT EXISTS `nilai` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nim` int NOT NULL,
  `kode_matkul` int NOT NULL DEFAULT '0',
  `nilai` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `nim_mahasiswa` (`nim`),
  KEY `kode_matkul` (`kode_matkul`),
  CONSTRAINT `kode_matkul` FOREIGN KEY (`kode_matkul`) REFERENCES `matkul` (`kode`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `nim_mahasiswa` FOREIGN KEY (`nim`) REFERENCES `mahasiswa` (`nim`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT IGNORE INTO `nilai` (`id`, `nim`, `kode_matkul`, `nilai`) VALUES
	(1, 3, 2, 50),
	(3, 1, 1, 1),
	(4, 1, 2, 1),
	(5, 4, 2, 80);

CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(50) NOT NULL DEFAULT '',
  `role` enum('d','a') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT IGNORE INTO `user` (`id`, `username`, `password`, `role`) VALUES
	(1, 'd', 'd', 'd'),
	(2, 'deli', 'deli', 'd'),
	(3, 'a', 'a', 'a');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
