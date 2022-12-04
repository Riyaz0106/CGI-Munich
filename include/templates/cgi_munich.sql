

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cgi_munich`
--
CREATE DATABASE IF NOT EXISTS `cgi_munich` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `cgi_munich`;

-- --------------------------------------------------------

--
-- Table structure for table `exchange_rate`
--

CREATE TABLE IF NOT EXISTS `exchange_rate` (
  `rate` decimal(50,3) NOT NULL,
  `month` int(2) NOT NULL,
  `year` int(4) NOT NULL,
  `created_date` date NOT NULL,
  `created_time` time NOT NULL,
  PRIMARY KEY (`month`,`year`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `exchange_rate`
--

INSERT IGNORE INTO `exchange_rate` (`rate`, `month`, `year`, `created_date`, `created_time`) VALUES
('81.765', 7, 2021, '2021-12-21', '18:42:43'),
('89.670', 11, 2021, '2021-12-19', '01:52:26'),
('86.064', 12, 2021, '2021-12-19', '01:58:26'),
('84.567', 10, 2021, '2021-12-19', '02:08:20'),
('86.765', 4, 2021, '2021-12-21', '18:42:33'),
('85.000', 2, 2022, '2022-02-08', '22:56:00');
COMMIT;
-- --------------------------------------------------------

--
-- Table structure for table `nationality`
--

CREATE TABLE IF NOT EXISTS `nationality` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB AUTO_INCREMENT=197 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `nationality`
--

INSERT IGNORE INTO `nationality` (`id`, `Name`) VALUES
(1, 'Afghanistan'),
(2, 'Albania'),
(3, 'Algeria'),
(4, 'Andorra'),
(5, 'Angola'),
(6, 'Antigua'),
(7, 'Argentina'),
(8, 'Armenia'),
(9, 'Australia'),
(10, 'Austria'),
(11, 'Azerbaijan'),
(12, 'Bahamas'),
(13, 'Bahrain'),
(14, 'Bangladesh'),
(15, 'Barbados'),
(16, 'Belarus'),
(17, 'Belgium'),
(18, 'Belize'),
(19, 'Benin'),
(20, 'Bhutan'),
(21, 'Bolivia'),
(22, 'Bosnia Herzegovina'),
(23, 'Botswana'),
(24, 'Brazil'),
(25, 'Brunei'),
(26, 'Bulgaria'),
(27, 'Burkina'),
(28, 'Burundi'),
(29, 'Cambodia'),
(30, 'Cameroon'),
(31, 'Canada'),
(32, 'Cape Verde'),
(33, 'Central African Rep'),
(34, 'Chad'),
(35, 'Chile'),
(36, 'China'),
(37, 'Colombia'),
(38, 'Comoros'),
(39, 'Congo'),
(40, 'Costa Rica'),
(41, 'Croatia'),
(42, 'Cuba'),
(43, 'Cyprus'),
(44, 'Czech Republic'),
(45, 'Denmark'),
(46, 'Djibouti'),
(47, 'Dominica'),
(48, 'Dominican Republic'),
(49, 'East Timor'),
(50, 'Ecuador'),
(51, 'Egypt'),
(52, 'El Salvador'),
(53, 'Equatorial Guinea'),
(54, 'Eritrea'),
(55, 'Estonia'),
(56, 'Ethiopia'),
(57, 'Fiji'),
(58, 'Finland'),
(59, 'France'),
(60, 'Gabon'),
(61, 'Gambia'),
(62, 'Georgia'),
(63, 'Germany'),
(64, 'Ghana'),
(65, 'Greece'),
(66, 'Grenada'),
(67, 'Guatemala'),
(68, 'Guinea'),
(69, 'Guinea-Bissau'),
(70, 'Guyana'),
(71, 'Haiti'),
(72, 'Honduras'),
(73, 'Hungary'),
(74, 'Iceland'),
(75, 'India'),
(76, 'Indonesia'),
(77, 'Iran'),
(78, 'Iraq'),
(79, 'Ireland'),
(80, 'Israel'),
(81, 'Italy'),
(82, 'Ivory Coast'),
(83, 'Jamaica'),
(84, 'Japan'),
(85, 'Jordan'),
(86, 'Kazakhstan'),
(87, 'Kenya'),
(88, 'Kiribati'),
(89, 'Korea North'),
(90, 'Korea South'),
(91, 'Kosovo'),
(92, 'Kuwait'),
(93, 'Kyrgyzstan'),
(94, 'Laos'),
(95, 'Latvia'),
(96, 'Lebanon'),
(97, 'Lesotho'),
(98, 'Liberia'),
(99, 'Libya'),
(100, 'Liechtenstein'),
(101, 'Lithuania'),
(102, 'Luxembourg'),
(103, 'Macedonia'),
(104, 'Madagascar'),
(105, 'Malawi'),
(106, 'Malaysia'),
(107, 'Maldives'),
(108, 'Mali'),
(109, 'Malta'),
(110, 'Marshall Islands'),
(111, 'Mauritania'),
(112, 'Mauritius'),
(113, 'Mexico'),
(114, 'Micronesia'),
(115, 'Moldova'),
(116, 'Monaco'),
(117, 'Mongolia'),
(118, 'Montenegro'),
(119, 'Morocco'),
(120, 'Mozambique'),
(121, 'Myanmar'),
(122, 'Namibia'),
(123, 'Nauru'),
(124, 'Nepal'),
(125, 'Netherlands'),
(126, 'New Zealand'),
(127, 'Nicaragua'),
(128, 'Niger'),
(129, 'Nigeria'),
(130, 'Norway'),
(131, 'Oman'),
(196, 'Other'),
(132, 'Pakistan'),
(133, 'Palau'),
(134, 'Panama'),
(135, 'Papua New Guinea'),
(136, 'Paraguay'),
(137, 'Peru'),
(138, 'Philippines'),
(139, 'Poland'),
(140, 'Portugal'),
(141, 'Qatar'),
(142, 'Romania'),
(143, 'Russian Federation'),
(144, 'Rwanda'),
(147, 'Saint Vincent & the Grenadines'),
(148, 'Samoa'),
(149, 'San Marino'),
(150, 'Sao Tome & Principe'),
(151, 'Saudi Arabia'),
(152, 'Senegal'),
(153, 'Serbia'),
(154, 'Seychelles'),
(155, 'Sierra Leone'),
(156, 'Singapore'),
(157, 'Slovakia'),
(158, 'Slovenia'),
(159, 'Solomon Islands'),
(160, 'Somalia'),
(161, 'South Africa'),
(162, 'South Sudan'),
(163, 'Spain'),
(164, 'Sri Lanka'),
(145, 'St Kitts & Nevis'),
(146, 'St Lucia'),
(165, 'Sudan'),
(166, 'Suriname'),
(167, 'Swaziland'),
(168, 'Sweden'),
(169, 'Switzerland'),
(170, 'Syria'),
(171, 'Taiwan'),
(172, 'Tajikistan'),
(173, 'Tanzania'),
(174, 'Thailand'),
(175, 'Togo'),
(176, 'Tonga'),
(177, 'Trinidad & Tobago'),
(178, 'Tunisia'),
(179, 'Turkey'),
(180, 'Turkmenistan'),
(181, 'Tuvalu'),
(182, 'Uganda'),
(183, 'Ukraine'),
(184, 'United Arab Emirates'),
(185, 'United Kingdom'),
(186, 'United States'),
(187, 'Uruguay'),
(188, 'Uzbekistan'),
(189, 'Vanuatu'),
(190, 'Vatican City'),
(191, 'Venezuela'),
(192, 'Vietnam'),
(193, 'Yemen'),
(194, 'Zambia'),
(195, 'Zimbabwe');
COMMIT;
-- --------------------------------------------------------

--
-- Table structure for table `refund_receipt`
--

CREATE TABLE IF NOT EXISTS `refund_receipt` (
  `receipt_no` varchar(100) NOT NULL,
  `receipt_date` date NOT NULL,
  `receipt_time` time NOT NULL,
  `total_refund` int(11) NOT NULL,
  PRIMARY KEY (`receipt_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `refund_receipt`
--

INSERT IGNORE INTO `refund_receipt` (`receipt_no`, `receipt_date`, `receipt_time`, `total_refund`) VALUES
('21121601R', '2021-12-16', '02:17:16', 74),
('21121602R', '2021-12-16', '02:18:07', 39),
('21121701R', '2021-12-17', '12:43:42', 54),
('21122301R', '2021-12-23', '00:58:52', 21);
COMMIT;
-- --------------------------------------------------------

--
-- Table structure for table `receipt`
--

CREATE TABLE IF NOT EXISTS `receipt` (
  `receipt_no` int(100) NOT NULL,
  `receipt_date` date NOT NULL,
  `receipt_time` time NOT NULL,
  `Name` char(200) NOT NULL,
  `Nationality` varchar(100) NOT NULL,
  `service_code` varchar(10) NOT NULL,
  `no_doc` int(10) NOT NULL,
  `trans_type` char(20) NOT NULL,
  `serv_chrg_type` char(10) NOT NULL,
  `gratis_ind` varchar(10) NOT NULL DEFAULT 'Non Gratis',
  `post_express` tinyint(1) NOT NULL DEFAULT '0',
  `wave_icwf` tinyint(1) NOT NULL DEFAULT '0',
  `misc_amt` int(11) NOT NULL,
  `misc_desc` varchar(100) NOT NULL,
  `post_amt` int(11) NOT NULL,
  `fees_amt` int(11) NOT NULL,
  `icwf_amt` int(11) NOT NULL,
  `total_amt` int(11) NOT NULL,
  `refund_receipt_no` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`receipt_no`),
  UNIQUE KEY `refund_receipt_no` (`refund_receipt_no`),
  FOREIGN KEY (`refund_receipt_no`) REFERENCES `refund_receipt` (`receipt_no`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `receipt`
--

INSERT IGNORE INTO `receipt` (`receipt_no`, `receipt_date`, `receipt_time`, `Name`, `Nationality`, `service_code`, `no_doc`, `trans_type`, `serv_chrg_type`, `gratis_ind`, `post_express`, `wave_icwf`, `misc_amt`, `misc_desc`, `post_amt`, `fees_amt`, `icwf_amt`, `total_amt`, `refund_receipt_no`) VALUES
(21111701, '2021-11-17', '15:22:16', 'Riyaz', 'Benin', 'PPTAD100', 1, 'Cash', 'None', 'Non Gratis', 1, 1, 0, '', 4, 60, 0, 64, '21121701R'),
(21111702, '2021-11-17', '15:53:53', 'TestData', 'Australia', 'GVALBU01', 1, 'Cash', 'None', 'Gratis', 0, 0, 0, '', 4, 0, 0, 4, NULL),
(21111703, '2021-11-17', '16:00:52', 'BlueVally', 'Armenia', 'REGBT104', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 0, '', 4, 25, 2, 31, '21122301R'),
(21111704, '2021-11-17', '16:04:08', 'Mohan Patel Test', 'Germany', 'GVALSE01', 1, 'Cash', 'None', 'Non Gratis', 1, 0, 10, 'Other Services', 4, 67, 3, 84, '21121601R'),
(21111705, '2021-11-17', '16:05:22', 'Rahul Test', 'Germany', 'PPTNB103', 1, 'Card', 'R Holiday', 'Non Gratis', 1, 1, 0, '', 4, 40, 0, 44, '21121602R'),
(21111706, '2021-11-17', '16:08:26', 'Mahesh Test', 'Germany', 'ATTAF115', 1, 'Cash', 'None', 'Non Gratis', 1, 1, 0, '', 4, 9, 0, 13, NULL),
(21111707, '2021-11-17', '16:11:59', 'Sameer Test', 'Germany', 'PPTLT105', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 0, '', 4, 111, 2, 117, NULL),
(21111708, '2021-11-17', '16:18:09', 'Christmas', 'Angola', 'CRTBI125', 1, 'Bank Transfer', 'None', 'Gratis', 0, 0, 0, '', 0, 0, 0, 0, NULL),
(21111710, '2021-11-17', '16:23:40', 'Shaik Riyaz', 'Germany', 'GVALME01', 1, 'Cash', 'None', 'Non Gratis', 1, 0, 0, '', 4, 67, 3, 74, NULL),
(21111711, '2021-11-17', '16:24:33', 'Rohan', 'Bosnia Herzegovina', 'REGBT104', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 25, 2, 27, NULL),
(21111712, '2021-11-17', '16:26:32', 'LOLTest', 'Belarus', 'PPTAD100', 1, 'Cash', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(21111713, '2021-11-17', '16:27:35', 'Hello testing', 'Bangladesh', 'REGBT104', 1, 'Card', 'None', 'Non Gratis', 0, 0, 0, '', 0, 25, 2, 27, NULL),
(21111714, '2021-11-17', '16:41:35', 'jkkjhlkh', 'Antigua', 'REGBT104', 1, 'Cash', 'None', 'Non Gratis', 0, 0, 0, '', 0, 25, 2, 27, NULL),
(21112201, '2021-11-22', '00:16:32', 'SirajTest', 'Germany', 'GVALER02', 1, 'Bank Transfer', 'None', 'Gratis', 1, 0, 10, 'TestMisc', 4, 0, 0, 14, NULL),
(21112202, '2021-11-22', '00:19:07', 'SirajTest', 'Germany', 'GVALER02', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 100, 3, 103, NULL),
(21112203, '2021-11-22', '17:48:38', 'ShaikRiyaz', 'Germany', 'GVALER03', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 10, 'Other', 0, 167, 3, 180, NULL),
(21121601, '2021-12-16', '02:05:13', 'Hello World', 'Germany', 'GVALBU02', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 7, 'Extra Costs', 4, 209, 3, 223, NULL),
(21121602, '2021-12-16', '02:06:23', 'OnePlus phone', 'South Africa', 'PPTAD100', 1, 'Card', 'None', 'Non Gratis', 1, 1, 0, '', 4, 60, 0, 64, NULL),
(21122101, '2021-12-21', '03:08:14', 'Michle', 'Germany', 'GVALBU01', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 0, '', 4, 100, 3, 107, NULL),
(22020201, '2022-02-02', '12:13:51', 'Google', 'Germany', 'PPTAD100', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 5, 'Other ', 4, 60, 2, 71, NULL),
(22020202, '2022-02-02', '12:19:17', 'facebook', 'Germany', 'GVALBU01', 1, 'Cash', 'None', 'Non Gratis', 1, 0, 5, 'dummy', 4, 100, 3, 112, NULL),
(22020203, '2022-02-02', '12:20:42', 'Meta', 'Germany', 'OCIAD108', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 5, 'testing', 4, 230, 3, 242, NULL),
(22020204, '2022-02-02', '12:23:26', 'Skullcandy', 'Germany', 'REGBT104', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 5, 'trash', 4, 25, 2, 36, NULL),
(22020205, '2022-02-02', '12:25:06', 'Penguin', 'Germany', 'ATTPO112', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 5, 'test2', 4, 9, 2, 20, NULL),
(22020206, '2022-02-02', '12:38:40', 'Gully Boy', 'Germany', 'GVALER01', 1, 'Cash', 'R Work Day', 'Non Gratis', 1, 0, 5, 'Other', 4, 67, 3, 79, NULL),
(22020207, '2022-02-02', '12:55:17', 'snmanf', 'India', 'OCIAD108', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 230, 3, 233, NULL),
(22020208, '2022-02-02', '12:58:19', 'asmfbadaf', 'Albania', 'CRTBI125', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 20, 2, 22, NULL),
(22020209, '2022-02-02', '13:07:03', 'skgsg', 'Namibia', 'OCIAD108', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 230, 3, 233, NULL),
(22020210, '2022-02-02', '13:14:41', 'sdkjfn', 'India', 'OCIAD108', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 230, 3, 233, NULL),
(22020211, '2022-02-02', '13:15:38', 'smdm', 'Macedonia', 'CRTBI125', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 20, 2, 22, NULL),
(22020212, '2022-02-02', '13:16:34', 'damn', 'Vanuatu', 'REGBT104', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 25, 2, 27, NULL),
(22020213, '2022-02-02', '13:28:43', 'hnerdvd', 'Antigua', 'OCIAD108', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 230, 3, 233, NULL),
(22020214, '2022-02-02', '13:30:01', 'ljljlhlhlh', 'Brazil', 'REGBT104', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 25, 2, 27, NULL),
(22020215, '2022-02-02', '13:35:40', 'gdfhdhf', 'Argentina', 'PPTAD100', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(22020216, '2022-02-02', '13:37:53', 'nmsdbmbs', 'Maldives', 'PPTAD100', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(22020217, '2022-02-02', '13:40:26', 'mbdsf', 'Taiwan', 'PPTAD100', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(22020218, '2022-02-02', '13:41:47', 'mnsdbfmsmbdf', 'Trinidad & Tobago', 'OCIAD108', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 230, 3, 233, NULL),
(22020219, '2022-02-02', '13:44:27', 'dbnfmnnds sjdnv', 'Austria', 'PPTAD100', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(22020220, '2022-02-02', '13:48:11', 'mbjasdbfjh', 'Bulgaria', 'PPTAD100', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(22020221, '2022-02-02', '13:54:28', 'fddhdgdhd', 'Belgium', 'PPTLT106', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 130, 2, 132, NULL),
(22020222, '2022-02-02', '14:36:37', 'judo karate', 'Germany', 'PPTRE107', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(22020223, '2022-02-02', '14:39:50', 'dgsfgsdfg', 'Belgium', 'OCIPI111', 1, 'Bank Transfer', 'None', 'Non Gratis', 1, 0, 0, '', 4, 84, 3, 91, NULL),
(22020224, '2022-02-02', '14:47:55', 'mxnlkfnk', 'Bangladesh', 'CRTNR126', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 20, 2, 22, NULL),
(22020225, '2022-02-02', '14:52:18', 'bnvjbkbj', 'Bolivia', 'OCIAD108', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 230, 3, 233, NULL),
(22020226, '2022-02-02', '14:58:17', 'sjhdfvhsdf', 'El Salvador', 'PPTMI102', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 40, 2, 42, NULL),
(22020227, '2022-02-02', '15:01:55', 'smgsdgdf', 'Canada', 'CRTNR126', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 20, 2, 22, NULL),
(22020228, '2022-02-02', '15:03:53', 'nmbv', 'Bulgaria', 'REGDT127', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 17, 2, 19, NULL),
(22020229, '2022-02-02', '15:07:53', 'ssdmnbd', 'Eritrea', 'CRTBI125', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 20, 2, 22, NULL),
(22020230, '2022-02-02', '15:10:13', 'bdfbsdmf', 'Chile', 'PPTAD100', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(22020231, '2022-02-02', '15:12:10', 'mnnvhgcgvgh', 'Cape Verde', 'CRTTR123', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 0, 0, 0, NULL),
(22020232, '2022-02-02', '15:13:59', 'vvhjhghjgjk', 'Thailand', 'GVALST01', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 67, 3, 70, NULL),
(22020233, '2022-02-02', '15:15:06', 'bmkfkbvk', 'Macedonia', 'PPTNB103', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 40, 2, 42, NULL),
(22020234, '2022-02-02', '15:17:43', 'nmdmncxmnv', 'Bhutan', 'ATTPO113', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 17, 2, 19, NULL),
(22020235, '2022-02-02', '15:20:49', 'mnbdcmnsnbvd', 'Angola', 'OCIAD108', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 230, 3, 233, NULL),
(22020236, '2022-02-02', '15:23:22', 'bdbvsdvfjs', 'Japan', 'PPTRE107', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 60, 2, 62, NULL),
(22020237, '2022-02-02', '15:24:18', 'zbdvbzmnvb', 'Egypt', 'REGBT104', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 25, 2, 27, NULL),
(22020238, '2022-02-02', '15:29:39', 'kjxfxhjkg', 'Burkina', 'CRTBI125', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 20, 2, 22, NULL),
(22020239, '2022-02-02', '15:30:31', 'bhjhkbhjk', 'Algeria', 'OCIMI109', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 230, 3, 233, NULL),
(22020240, '2022-02-02', '16:14:19', 'mndcvmvsdv', 'Angola', 'PPTLT106', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 130, 2, 132, NULL),
(22021101, '2022-02-11', '20:35:34', 'Nesting', 'Germany', 'GVALBU01', 1, 'Bank Transfer', 'None', 'Non Gratis', 0, 0, 0, '', 0, 100, 3, 103, NULL);
COMMIT;
-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE IF NOT EXISTS `services` (
  `code` varchar(10) NOT NULL,
  `description` varchar(200) NOT NULL,
  `charges` decimal(10,0) NOT NULL,
  `icwf` decimal(10,0) NOT NULL,
  `category` varchar(50) NOT NULL,
  `sub_category` varchar(100) NOT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `services`
--

INSERT IGNORE INTO `services` (`code`, `description`, `charges`, `icwf`, `category`, `sub_category`) VALUES
('ATTAF115', 'Sworn Affidavit', '9', '2', 'Attestation', 'AFFIDAVIT'),
('ATTMI117', 'Attestation of educational certificate, passport copy, adoption documents, marriage certificate, sponsorship certificate etc', '9', '2', 'Attestation', 'Miscellaneous'),
('ATTPO112', 'Power of attorney (Civil Documents)', '9', '2', 'Attestation', 'POA CIVIL'),
('ATTPO113', 'Power of attorney (For documents pertaining to sale, purchase, transfer, gift etc. of real estate or moveable properties)', '17', '2', 'Attestation', 'POA REAL ESTATE'),
('ATTPO114', 'Power of attorney Commercial', '42', '2', 'Attestation', 'POA COMMERCIAL'),
('ATTTD116', 'Attestation of Trade/commercial documents', '42', '2', 'Attestation', 'TRADE/COMERCIAL'),
('CRTBI125', 'Issuance of birth Certificate (on the basis of Passport)', '20', '2', 'Certificates', 'BIRTH'),
('CRTCL120', 'Police Clearance Certificate', '20', '2', 'Certificates', 'POLICE CLEARANCE'),
('CRTEM128', 'Emergency Certificates', '12', '2', 'Certificates', 'EMERGENCY'),
('CRTGR124', 'Issue of certificate in respect of name , date of birth etc for the German Authorities', '20', '2', 'Certificates', 'Miscellaneous--GERMAN AUTHORITY'),
('CRTLI121', 'Life certificate for pensioners', '0', '0', 'Certificates', 'LIFE'),
('CRTNO122', 'No Objection certificate for transferring dead bodies to India', '0', '0', 'Certificates', 'NO OBJECTION'),
('CRTNR126', 'NRI Certificate', '20', '2', 'Certificates', 'NRI'),
('CRTRE118', 'Renunciation Certificate-(I) If submitted within three years of acquiring foreign nationality for Adult/Minor', '80', '2', 'Certificates', 'ADULT/MINOR -- before 3Yr'),
('CRTRE119', 'Renunciation Certificate-(II) If submitted after three years of acquiring foreign nationality', '194', '2', 'Certificates', 'ADULT/MINOR -- after 3Yr'),
('CRTTR123', 'Certificate for Transport of Ashes or Human remains', '0', '0', 'Certificates', 'TRANSPORT'),
('GVALBU01', 'Bussiness visa Up to 1 year/Single or Multiple Entry', '100', '3', 'VISA', 'BUSINESS VISA'),
('GVALBU02', 'Bussiness visa More than 1 year and up to 5 years/Multiple Entry', '209', '3', 'VISA', 'BUSINESS VISA'),
('GVALEP01', 'Employment visa Up to 6 months/Single or Multiple Entry', '100', '3', 'VISA', 'EMPLOYMENT VISA'),
('GVALEP02', 'Employment visa More than 6 months and up to 1year/ Multiple Entry', '167', '3', 'VISA', 'EMPLOYMENT VISA'),
('GVALEP03', 'Employment visa More than 1year and up to 5 years/Multiple Entry', '250', '3', 'VISA', 'EMPLOYMENT VISA'),
('GVALER01', 'Entry visa Up to 6 months/Single or Multiple Entry', '67', '3', 'VISA', 'ENTRY VISA'),
('GVALER02', 'Entry visa More than 6 months and up to 1 year/ Multiple Entry', '100', '3', 'VISA', 'ENTRY VISA'),
('GVALER03', 'Entry visa More than 1 year and up to 5 years/Multiple Entry', '167', '3', 'VISA', 'ENTRY VISA'),
('GVALFL01', 'Film visa Up to 1year/Single or Multiple Entry(Maximum duration of the visa will be 1year)', '100', '3', 'VISA', 'FILM VISA'),
('GVALJO01', 'Journalist visa Up to 6 months/Single Entry', '67', '3', 'VISA', 'JOURNALIST VISA'),
('GVALME01', 'Medical visa Up to 6 months/Single or Multiple Entry', '67', '3', 'VISA', 'MEDICAL VISA'),
('GVALME02', 'Medical visa More than 6 months and up to 1year/ Multiple Entry', '100', '3', 'VISA', 'MEDICAL VISA'),
('GVALMI01', 'Missionary visa Up to 6 months/Single or Multiple Entry', '67', '3', 'VISA', 'MISSIONARY VISA'),
('GVALMI02', 'Missionary visa More than 6 months and up to 1year/ Multiple Entry', '100', '3', 'VISA', 'MISSIONARY VISA'),
('GVALMI03', 'Missionary More than 1year and up to 5 years/Multiple Entry', '167', '3', 'VISA', 'MISSIONARY VISA'),
('GVALMO01', 'Mountaineering visa Up to 6 months/Single (or Multiple) Entry', '67', '3', 'VISA', 'MOUNTAINERRING VISA'),
('GVALMO02', 'Mountaineering visa More than 6 months and up to 1year/ Multiple Entry', '100', '3', 'VISA', 'MOUNTAINERRING VISA'),
('GVALSE01', 'Conference/Seminars visa up to 6 months/Single (or multiple) Entry', '67', '3', 'VISA', 'CONFERENCE/SEMINARS VISA'),
('GVALST01', 'Student visa Valid for the duration of the course or 5 years, whichever is less/ Multiple Entry', '67', '3', 'VISA', 'STUDENT VISA'),
('GVALTR01', 'Transit visa Up to 15 days/Single or Double Entry', '17', '3', 'VISA', 'TRANSIT VISA'),
('GVALTU01', 'Tourist visa Up to 1 year/Single or Multiple Entry', '84', '3', 'VISA', 'TOURIST VISA'),
('GVALTU02', 'Tourist visa More than 1 year and up to 5 years/Multiple Entry', '167', '3', 'VISA', 'TOURIST VISA'),
('OCIAD108', 'For issue of Fresh OCI Card for ADULT', '230', '3', 'OCI', 'ADULT'),
('OCILT111', 'OCI Lost/Damage', '84', '3', 'OCI', 'LOST/DAMAGE'),
('OCIMI109', 'Issue of Fresh OCI Card for MINOR', '230', '3', 'OCI', 'MINOR'),
('OCIPI111', 'PIO to OCI', '84', '3', 'OCI', 'PIO'),
('OCIRI110', 'OCI Miscellaneous services(Reissue of OCI in case of new passport/change in personal particulars)', '21', '3', 'OCI', 'REISSUE'),
('PPTAD100', 'Adult passport charges', '60', '2', 'Passport', 'ADULT'),
('PPTJU101', 'Jumbo passport charges', '75', '2', 'Passport', 'JUMBO'),
('PPTLT105', 'Lost/Damage passport charges', '111', '2', 'Passport', 'LOST/DAMAGE'),
('PPTLT106', 'Jumbo lost/Damaged passport charges', '130', '2', 'Passport', 'JUMBO LOST/DAMAGE'),
('PPTMI102', 'Minor passport charges', '40', '2', 'Passport', 'MINOR'),
('PPTNB103', 'Newborn passport charges', '40', '2', 'Passport', 'NEW BORN'),
('PPTRE107', 'Replacement of passport', '60', '2', 'Passport', 'REPLACEMENT'),
('REGBT104', 'Registration of New born child/Birth Certificate', '25', '2', 'Registration', 'BIRTH'),
('REGDT127', 'Registration of Death', '17', '2', 'Registration', 'DEATH'),
('SV000000', 'Special visa fees', '0', '0', 'VISA', 'SPECIAL FEES');
COMMIT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `receipt`
--
-- ALTER TABLE `receipt`
--   ADD CONSTRAINT `fk_refund_receipt_no` FOREIGN KEY (`refund_receipt_no`) REFERENCES `refund_receipt` (`receipt_no`) ON DELETE SET NULL;
-- COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
