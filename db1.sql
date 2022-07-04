-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2022 at 01:36 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db1`
--

-- --------------------------------------------------------

--
-- Table structure for table `booklist`
--

CREATE TABLE `booklist` (
  `id` int(200) NOT NULL,
  `bookname` varchar(200) NOT NULL,
  `totalquantity` int(200) NOT NULL,
  `price` int(200) NOT NULL,
  `currentdate` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booklist`
--

INSERT INTO `booklist` (`id`, `bookname`, `totalquantity`, `price`, `currentdate`) VALUES
(1, 'programming in c', 20, 100, '2022-07-04 11:59:44'),
(2, 'programming in python', 20, 200, '2022-07-04 12:00:10'),
(3, 'programming in javascript', 20, 300, '2022-07-04 12:00:32');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `bid` int(200) NOT NULL,
  `bname` varchar(300) NOT NULL,
  `bprice` int(200) NOT NULL,
  `bquantity` int(200) NOT NULL,
  `datetime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`bid`, `bname`, `bprice`, `bquantity`, `datetime`) VALUES
(1, 'programming in c', 200, 1, '2022-07-04 11:31:27');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booklist`
--
ALTER TABLE `booklist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`bid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booklist`
--
ALTER TABLE `booklist`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `bid` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
