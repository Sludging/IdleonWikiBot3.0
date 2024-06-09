import { MapInfoModel } from '../model/mapInfoModel';

export class MapInfoBase { constructor(public index: number, public data: MapInfoModel) { } }



export const initMapPortalsRepo = () => {
    return [    
        new MapInfoBase(0, <MapInfoModel>{"id": 0, "portalRequirements": [1, 0], "maxOnScreen": 0}),
        new MapInfoBase(1, <MapInfoModel>{"id": 1, "portalRequirements": [21], "maxOnScreen": 15}),
        new MapInfoBase(2, <MapInfoModel>{"id": 2, "portalRequirements": [30], "maxOnScreen": 34}),
        new MapInfoBase(3, <MapInfoModel>{"id": 3, "portalRequirements": [150, 10], "maxOnScreen": 34}),
        new MapInfoBase(4, <MapInfoModel>{"id": 4, "portalRequirements": [150], "maxOnScreen": 0}),
        new MapInfoBase(5, <MapInfoModel>{"id": 5, "portalRequirements": [150], "maxOnScreen": 0}),
        new MapInfoBase(6, <MapInfoModel>{"id": 6, "portalRequirements": [10], "maxOnScreen": 11}),
        new MapInfoBase(7, <MapInfoModel>{"id": 7, "portalRequirements": [25, 81], "maxOnScreen": 20}),
        new MapInfoBase(8, <MapInfoModel>{"id": 8, "portalRequirements": [20000], "maxOnScreen": 28}),
        new MapInfoBase(9, <MapInfoModel>{"id": 9, "portalRequirements": [0], "maxOnScreen": 7}),
        new MapInfoBase(10, <MapInfoModel>{"id": 10, "portalRequirements": [40], "maxOnScreen": 18}),
        new MapInfoBase(11, <MapInfoModel>{"id": 11, "portalRequirements": [50, 60], "maxOnScreen": 29}),
        new MapInfoBase(12, <MapInfoModel>{"id": 12, "portalRequirements": [60], "maxOnScreen": 16}),
        new MapInfoBase(13, <MapInfoModel>{"id": 13, "portalRequirements": [2500, 50000], "maxOnScreen": 25}),
        new MapInfoBase(14, <MapInfoModel>{"id": 14, "portalRequirements": [40, 1500], "maxOnScreen": 22}),
        new MapInfoBase(15, <MapInfoModel>{"id": 15, "portalRequirements": [35000], "maxOnScreen": 25}),
        new MapInfoBase(16, <MapInfoModel>{"id": 16, "portalRequirements": [60, 3000], "maxOnScreen": 25}),
        new MapInfoBase(17, <MapInfoModel>{"id": 17, "portalRequirements": [0], "maxOnScreen": 15}),
        new MapInfoBase(18, <MapInfoModel>{"id": 18, "portalRequirements": [5000], "maxOnScreen": 25}),
        new MapInfoBase(19, <MapInfoModel>{"id": 19, "portalRequirements": [100], "maxOnScreen": 17}),
        new MapInfoBase(20, <MapInfoModel>{"id": 20, "portalRequirements": [7], "maxOnScreen": 7}),
        new MapInfoBase(21, <MapInfoModel>{"id": 21, "portalRequirements": [5], "maxOnScreen": 6}),
        new MapInfoBase(22, <MapInfoModel>{"id": 22, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(23, <MapInfoModel>{"id": 23, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(24, <MapInfoModel>{"id": 24, "portalRequirements": [125, 2000], "maxOnScreen": 16}),
        new MapInfoBase(25, <MapInfoModel>{"id": 25, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(26, <MapInfoModel>{"id": 26, "portalRequirements": [150], "maxOnScreen": 21}),
        new MapInfoBase(27, <MapInfoModel>{"id": 27, "portalRequirements": [30, 4200], "maxOnScreen": 17}),
        new MapInfoBase(28, <MapInfoModel>{"id": 28, "portalRequirements": [0], "maxOnScreen": 16}),
        new MapInfoBase(29, <MapInfoModel>{"id": 29, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(30, <MapInfoModel>{"id": 30, "portalRequirements": [0], "maxOnScreen": 1}),
        new MapInfoBase(31, <MapInfoModel>{"id": 31, "portalRequirements": [0], "maxOnScreen": 7}),
        new MapInfoBase(32, <MapInfoModel>{"id": 32, "portalRequirements": [0], "maxOnScreen": 15}),
        new MapInfoBase(33, <MapInfoModel>{"id": 33, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(34, <MapInfoModel>{"id": 34, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(35, <MapInfoModel>{"id": 35, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(36, <MapInfoModel>{"id": 36, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(37, <MapInfoModel>{"id": 37, "portalRequirements": [0], "maxOnScreen": 10}),
        new MapInfoBase(38, <MapInfoModel>{"id": 38, "portalRequirements": [0], "maxOnScreen": 30}),
        new MapInfoBase(39, <MapInfoModel>{"id": 39, "portalRequirements": [0], "maxOnScreen": 5}),
        new MapInfoBase(40, <MapInfoModel>{"id": 40, "portalRequirements": [0], "maxOnScreen": 1}),
        new MapInfoBase(41, <MapInfoModel>{"id": 41, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(42, <MapInfoModel>{"id": 42, "portalRequirements": [0], "maxOnScreen": 1}),
        new MapInfoBase(43, <MapInfoModel>{"id": 43, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(44, <MapInfoModel>{"id": 44, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(45, <MapInfoModel>{"id": 45, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(46, <MapInfoModel>{"id": 46, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(47, <MapInfoModel>{"id": 47, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(48, <MapInfoModel>{"id": 48, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(49, <MapInfoModel>{"id": 49, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(50, <MapInfoModel>{"id": 50, "portalRequirements": [1, 0, 0], "maxOnScreen": 0}),
        new MapInfoBase(51, <MapInfoModel>{"id": 51, "portalRequirements": [250], "maxOnScreen": 17}),
        new MapInfoBase(52, <MapInfoModel>{"id": 52, "portalRequirements": [600, 1000], "maxOnScreen": 21}),
        new MapInfoBase(53, <MapInfoModel>{"id": 53, "portalRequirements": [1000], "maxOnScreen": 18}),
        new MapInfoBase(54, <MapInfoModel>{"id": 54, "portalRequirements": [15], "maxOnScreen": 2}),
        new MapInfoBase(55, <MapInfoModel>{"id": 55, "portalRequirements": [30], "maxOnScreen": 3}),
        new MapInfoBase(56, <MapInfoModel>{"id": 56, "portalRequirements": [30], "maxOnScreen": 3}),
        new MapInfoBase(57, <MapInfoModel>{"id": 57, "portalRequirements": [1200], "maxOnScreen": 15}),
        new MapInfoBase(58, <MapInfoModel>{"id": 58, "portalRequirements": [1600], "maxOnScreen": 18}),
        new MapInfoBase(59, <MapInfoModel>{"id": 59, "portalRequirements": [2000], "maxOnScreen": 14}),
        new MapInfoBase(60, <MapInfoModel>{"id": 60, "portalRequirements": [2500, 0], "maxOnScreen": 17}),
        new MapInfoBase(61, <MapInfoModel>{"id": 61, "portalRequirements": [30], "maxOnScreen": 3}),
        new MapInfoBase(62, <MapInfoModel>{"id": 62, "portalRequirements": [3000], "maxOnScreen": 17}),
        new MapInfoBase(63, <MapInfoModel>{"id": 63, "portalRequirements": [4000], "maxOnScreen": 15}),
        new MapInfoBase(64, <MapInfoModel>{"id": 64, "portalRequirements": [5000], "maxOnScreen": 27}),
        new MapInfoBase(65, <MapInfoModel>{"id": 65, "portalRequirements": [1], "maxOnScreen": 13}),
        new MapInfoBase(66, <MapInfoModel>{"id": 66, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(67, <MapInfoModel>{"id": 67, "portalRequirements": [0], "maxOnScreen": 2}),
        new MapInfoBase(68, <MapInfoModel>{"id": 68, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(69, <MapInfoModel>{"id": 69, "portalRequirements": [0], "maxOnScreen": 1}),
        new MapInfoBase(70, <MapInfoModel>{"id": 70, "portalRequirements": [0], "maxOnScreen": 1}),
        new MapInfoBase(71, <MapInfoModel>{"id": 71, "portalRequirements": [0], "maxOnScreen": 1}),
        new MapInfoBase(72, <MapInfoModel>{"id": 72, "portalRequirements": [0], "maxOnScreen": 1}),
        new MapInfoBase(73, <MapInfoModel>{"id": 73, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(74, <MapInfoModel>{"id": 74, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(75, <MapInfoModel>{"id": 75, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(76, <MapInfoModel>{"id": 76, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(77, <MapInfoModel>{"id": 77, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(78, <MapInfoModel>{"id": 78, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(79, <MapInfoModel>{"id": 79, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(80, <MapInfoModel>{"id": 80, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(81, <MapInfoModel>{"id": 81, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(82, <MapInfoModel>{"id": 82, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(83, <MapInfoModel>{"id": 83, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(84, <MapInfoModel>{"id": 84, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(85, <MapInfoModel>{"id": 85, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(86, <MapInfoModel>{"id": 86, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(87, <MapInfoModel>{"id": 87, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(88, <MapInfoModel>{"id": 88, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(89, <MapInfoModel>{"id": 89, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(90, <MapInfoModel>{"id": 90, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(91, <MapInfoModel>{"id": 91, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(92, <MapInfoModel>{"id": 92, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(93, <MapInfoModel>{"id": 93, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(94, <MapInfoModel>{"id": 94, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(95, <MapInfoModel>{"id": 95, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(96, <MapInfoModel>{"id": 96, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(97, <MapInfoModel>{"id": 97, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(98, <MapInfoModel>{"id": 98, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(99, <MapInfoModel>{"id": 99, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(100, <MapInfoModel>{"id": 100, "portalRequirements": [1, 0], "maxOnScreen": 0}),
        new MapInfoBase(101, <MapInfoModel>{"id": 101, "portalRequirements": [1000], "maxOnScreen": 16}),
        new MapInfoBase(102, <MapInfoModel>{"id": 102, "portalRequirements": [4000], "maxOnScreen": 0}),
        new MapInfoBase(103, <MapInfoModel>{"id": 103, "portalRequirements": [2000], "maxOnScreen": 14}),
        new MapInfoBase(104, <MapInfoModel>{"id": 104, "portalRequirements": [3000, 100000], "maxOnScreen": 21}),
        new MapInfoBase(105, <MapInfoModel>{"id": 105, "portalRequirements": [4000], "maxOnScreen": 19}),
        new MapInfoBase(106, <MapInfoModel>{"id": 106, "portalRequirements": [6000], "maxOnScreen": 21}),
        new MapInfoBase(107, <MapInfoModel>{"id": 107, "portalRequirements": [8000], "maxOnScreen": 19}),
        new MapInfoBase(108, <MapInfoModel>{"id": 108, "portalRequirements": [11000], "maxOnScreen": 13}),
        new MapInfoBase(109, <MapInfoModel>{"id": 109, "portalRequirements": [15000], "maxOnScreen": 18}),
        new MapInfoBase(110, <MapInfoModel>{"id": 110, "portalRequirements": [18000], "maxOnScreen": 20}),
        new MapInfoBase(111, <MapInfoModel>{"id": 111, "portalRequirements": [22000], "maxOnScreen": 20}),
        new MapInfoBase(112, <MapInfoModel>{"id": 112, "portalRequirements": [35000], "maxOnScreen": 18}),
        new MapInfoBase(113, <MapInfoModel>{"id": 113, "portalRequirements": [120000], "maxOnScreen": 22}),
        new MapInfoBase(114, <MapInfoModel>{"id": 114, "portalRequirements": [1000], "maxOnScreen": 0}),
        new MapInfoBase(115, <MapInfoModel>{"id": 115, "portalRequirements": [1000], "maxOnScreen": 0}),
        new MapInfoBase(116, <MapInfoModel>{"id": 116, "portalRequirements": [250000], "maxOnScreen": 20}),
        new MapInfoBase(117, <MapInfoModel>{"id": 117, "portalRequirements": [0], "maxOnScreen": 17}),
        new MapInfoBase(118, <MapInfoModel>{"id": 118, "portalRequirements": [0], "maxOnScreen": 5}),
        new MapInfoBase(119, <MapInfoModel>{"id": 119, "portalRequirements": [0], "maxOnScreen": 3}),
        new MapInfoBase(120, <MapInfoModel>{"id": 120, "portalRequirements": [0], "maxOnScreen": 1}),
        new MapInfoBase(121, <MapInfoModel>{"id": 121, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(122, <MapInfoModel>{"id": 122, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(123, <MapInfoModel>{"id": 123, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(124, <MapInfoModel>{"id": 124, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(125, <MapInfoModel>{"id": 125, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(126, <MapInfoModel>{"id": 126, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(127, <MapInfoModel>{"id": 127, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(128, <MapInfoModel>{"id": 128, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(129, <MapInfoModel>{"id": 129, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(130, <MapInfoModel>{"id": 130, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(131, <MapInfoModel>{"id": 131, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(132, <MapInfoModel>{"id": 132, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(133, <MapInfoModel>{"id": 133, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(134, <MapInfoModel>{"id": 134, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(135, <MapInfoModel>{"id": 135, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(136, <MapInfoModel>{"id": 136, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(137, <MapInfoModel>{"id": 137, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(138, <MapInfoModel>{"id": 138, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(139, <MapInfoModel>{"id": 139, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(140, <MapInfoModel>{"id": 140, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(141, <MapInfoModel>{"id": 141, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(142, <MapInfoModel>{"id": 142, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(143, <MapInfoModel>{"id": 143, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(144, <MapInfoModel>{"id": 144, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(145, <MapInfoModel>{"id": 145, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(146, <MapInfoModel>{"id": 146, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(147, <MapInfoModel>{"id": 147, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(148, <MapInfoModel>{"id": 148, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(149, <MapInfoModel>{"id": 149, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(150, <MapInfoModel>{"id": 150, "portalRequirements": [1, 0], "maxOnScreen": 0}),
        new MapInfoBase(151, <MapInfoModel>{"id": 151, "portalRequirements": [5000], "maxOnScreen": 13}),
        new MapInfoBase(152, <MapInfoModel>{"id": 152, "portalRequirements": [12000], "maxOnScreen": 20}),
        new MapInfoBase(153, <MapInfoModel>{"id": 153, "portalRequirements": [18000], "maxOnScreen": 17}),
        new MapInfoBase(154, <MapInfoModel>{"id": 154, "portalRequirements": [25000], "maxOnScreen": 16}),
        new MapInfoBase(155, <MapInfoModel>{"id": 155, "portalRequirements": [40000], "maxOnScreen": 26}),
        new MapInfoBase(156, <MapInfoModel>{"id": 156, "portalRequirements": [60000], "maxOnScreen": 22}),
        new MapInfoBase(157, <MapInfoModel>{"id": 157, "portalRequirements": [90000], "maxOnScreen": 20}),
        new MapInfoBase(158, <MapInfoModel>{"id": 158, "portalRequirements": [120000], "maxOnScreen": 18}),
        new MapInfoBase(159, <MapInfoModel>{"id": 159, "portalRequirements": [150000], "maxOnScreen": 16}),
        new MapInfoBase(160, <MapInfoModel>{"id": 160, "portalRequirements": [190000], "maxOnScreen": 22}),
        new MapInfoBase(161, <MapInfoModel>{"id": 161, "portalRequirements": [250000], "maxOnScreen": 19}),
        new MapInfoBase(162, <MapInfoModel>{"id": 162, "portalRequirements": [300000], "maxOnScreen": 26}),
        new MapInfoBase(163, <MapInfoModel>{"id": 163, "portalRequirements": [350000], "maxOnScreen": 14}),
        new MapInfoBase(164, <MapInfoModel>{"id": 164, "portalRequirements": [250], "maxOnScreen": 0}),
        new MapInfoBase(165, <MapInfoModel>{"id": 165, "portalRequirements": [700], "maxOnScreen": 0}),
        new MapInfoBase(166, <MapInfoModel>{"id": 166, "portalRequirements": [100], "maxOnScreen": 40}),
        new MapInfoBase(167, <MapInfoModel>{"id": 167, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(168, <MapInfoModel>{"id": 168, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(169, <MapInfoModel>{"id": 169, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(170, <MapInfoModel>{"id": 170, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(171, <MapInfoModel>{"id": 171, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(172, <MapInfoModel>{"id": 172, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(173, <MapInfoModel>{"id": 173, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(174, <MapInfoModel>{"id": 174, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(175, <MapInfoModel>{"id": 175, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(176, <MapInfoModel>{"id": 176, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(177, <MapInfoModel>{"id": 177, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(178, <MapInfoModel>{"id": 178, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(179, <MapInfoModel>{"id": 179, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(180, <MapInfoModel>{"id": 180, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(181, <MapInfoModel>{"id": 181, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(182, <MapInfoModel>{"id": 182, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(183, <MapInfoModel>{"id": 183, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(184, <MapInfoModel>{"id": 184, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(185, <MapInfoModel>{"id": 185, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(186, <MapInfoModel>{"id": 186, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(187, <MapInfoModel>{"id": 187, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(188, <MapInfoModel>{"id": 188, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(189, <MapInfoModel>{"id": 189, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(190, <MapInfoModel>{"id": 190, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(191, <MapInfoModel>{"id": 191, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(192, <MapInfoModel>{"id": 192, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(193, <MapInfoModel>{"id": 193, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(194, <MapInfoModel>{"id": 194, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(195, <MapInfoModel>{"id": 195, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(196, <MapInfoModel>{"id": 196, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(197, <MapInfoModel>{"id": 197, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(198, <MapInfoModel>{"id": 198, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(199, <MapInfoModel>{"id": 199, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(200, <MapInfoModel>{"id": 200, "portalRequirements": [1, 0], "maxOnScreen": 0}),
        new MapInfoBase(201, <MapInfoModel>{"id": 201, "portalRequirements": [15000], "maxOnScreen": 16}),
        new MapInfoBase(202, <MapInfoModel>{"id": 202, "portalRequirements": [25000], "maxOnScreen": 25}),
        new MapInfoBase(203, <MapInfoModel>{"id": 203, "portalRequirements": [40000], "maxOnScreen": 25}),
        new MapInfoBase(204, <MapInfoModel>{"id": 204, "portalRequirements": [50000], "maxOnScreen": 25}),
        new MapInfoBase(205, <MapInfoModel>{"id": 205, "portalRequirements": [75000], "maxOnScreen": 30}),
        new MapInfoBase(206, <MapInfoModel>{"id": 206, "portalRequirements": [100000], "maxOnScreen": 21}),
        new MapInfoBase(207, <MapInfoModel>{"id": 207, "portalRequirements": [200000], "maxOnScreen": 26}),
        new MapInfoBase(208, <MapInfoModel>{"id": 208, "portalRequirements": [300000], "maxOnScreen": 27}),
        new MapInfoBase(209, <MapInfoModel>{"id": 209, "portalRequirements": [450000], "maxOnScreen": 19}),
        new MapInfoBase(210, <MapInfoModel>{"id": 210, "portalRequirements": [600000], "maxOnScreen": 23}),
        new MapInfoBase(211, <MapInfoModel>{"id": 211, "portalRequirements": [1000000], "maxOnScreen": 22}),
        new MapInfoBase(212, <MapInfoModel>{"id": 212, "portalRequirements": [3000000], "maxOnScreen": 27}),
        new MapInfoBase(213, <MapInfoModel>{"id": 213, "portalRequirements": [60000], "maxOnScreen": 35}),
        new MapInfoBase(214, <MapInfoModel>{"id": 214, "portalRequirements": [100], "maxOnScreen": 0}),
        new MapInfoBase(215, <MapInfoModel>{"id": 215, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(216, <MapInfoModel>{"id": 216, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(217, <MapInfoModel>{"id": 217, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(218, <MapInfoModel>{"id": 218, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(219, <MapInfoModel>{"id": 219, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(220, <MapInfoModel>{"id": 220, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(221, <MapInfoModel>{"id": 221, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(222, <MapInfoModel>{"id": 222, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(223, <MapInfoModel>{"id": 223, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(224, <MapInfoModel>{"id": 224, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(225, <MapInfoModel>{"id": 225, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(226, <MapInfoModel>{"id": 226, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(227, <MapInfoModel>{"id": 227, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(228, <MapInfoModel>{"id": 228, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(229, <MapInfoModel>{"id": 229, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(230, <MapInfoModel>{"id": 230, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(231, <MapInfoModel>{"id": 231, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(232, <MapInfoModel>{"id": 232, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(233, <MapInfoModel>{"id": 233, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(234, <MapInfoModel>{"id": 234, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(235, <MapInfoModel>{"id": 235, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(236, <MapInfoModel>{"id": 236, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(237, <MapInfoModel>{"id": 237, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(238, <MapInfoModel>{"id": 238, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(239, <MapInfoModel>{"id": 239, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(240, <MapInfoModel>{"id": 240, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(241, <MapInfoModel>{"id": 241, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(242, <MapInfoModel>{"id": 242, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(243, <MapInfoModel>{"id": 243, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(244, <MapInfoModel>{"id": 244, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(245, <MapInfoModel>{"id": 245, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(246, <MapInfoModel>{"id": 246, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(247, <MapInfoModel>{"id": 247, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(248, <MapInfoModel>{"id": 248, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(249, <MapInfoModel>{"id": 249, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(250, <MapInfoModel>{"id": 250, "portalRequirements": [1, 0], "maxOnScreen": 0}),
        new MapInfoBase(251, <MapInfoModel>{"id": 251, "portalRequirements": [30000], "maxOnScreen": 16}),
        new MapInfoBase(252, <MapInfoModel>{"id": 252, "portalRequirements": [50000], "maxOnScreen": 18}),
        new MapInfoBase(253, <MapInfoModel>{"id": 253, "portalRequirements": [100000], "maxOnScreen": 19}),
        new MapInfoBase(254, <MapInfoModel>{"id": 254, "portalRequirements": [250000], "maxOnScreen": 21}),
        new MapInfoBase(255, <MapInfoModel>{"id": 255, "portalRequirements": [400000], "maxOnScreen": 22}),
        new MapInfoBase(256, <MapInfoModel>{"id": 256, "portalRequirements": [1100000], "maxOnScreen": 20}),
        new MapInfoBase(257, <MapInfoModel>{"id": 257, "portalRequirements": [3200000], "maxOnScreen": 21}),
        new MapInfoBase(258, <MapInfoModel>{"id": 258, "portalRequirements": [8000000], "maxOnScreen": 25}),
        new MapInfoBase(259, <MapInfoModel>{"id": 259, "portalRequirements": [12000000], "maxOnScreen": 26}),
        new MapInfoBase(260, <MapInfoModel>{"id": 260, "portalRequirements": [25000000], "maxOnScreen": 22}),
        new MapInfoBase(261, <MapInfoModel>{"id": 261, "portalRequirements": [70000000], "maxOnScreen": 24}),
        new MapInfoBase(262, <MapInfoModel>{"id": 262, "portalRequirements": [100000000], "maxOnScreen": 27}),
        new MapInfoBase(263, <MapInfoModel>{"id": 263, "portalRequirements": [150000000], "maxOnScreen": 31}),
        new MapInfoBase(264, <MapInfoModel>{"id": 264, "portalRequirements": [100], "maxOnScreen": 36}),
        new MapInfoBase(265, <MapInfoModel>{"id": 265, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(266, <MapInfoModel>{"id": 266, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(267, <MapInfoModel>{"id": 267, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(268, <MapInfoModel>{"id": 268, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(269, <MapInfoModel>{"id": 269, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(270, <MapInfoModel>{"id": 270, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(271, <MapInfoModel>{"id": 271, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(272, <MapInfoModel>{"id": 272, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(273, <MapInfoModel>{"id": 273, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(274, <MapInfoModel>{"id": 274, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(275, <MapInfoModel>{"id": 275, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(276, <MapInfoModel>{"id": 276, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(277, <MapInfoModel>{"id": 277, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(278, <MapInfoModel>{"id": 278, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(279, <MapInfoModel>{"id": 279, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(280, <MapInfoModel>{"id": 280, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(281, <MapInfoModel>{"id": 281, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(282, <MapInfoModel>{"id": 282, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(283, <MapInfoModel>{"id": 283, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(284, <MapInfoModel>{"id": 284, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(285, <MapInfoModel>{"id": 285, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(286, <MapInfoModel>{"id": 286, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(287, <MapInfoModel>{"id": 287, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(288, <MapInfoModel>{"id": 288, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(289, <MapInfoModel>{"id": 289, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(290, <MapInfoModel>{"id": 290, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(291, <MapInfoModel>{"id": 291, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(292, <MapInfoModel>{"id": 292, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(293, <MapInfoModel>{"id": 293, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(294, <MapInfoModel>{"id": 294, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(295, <MapInfoModel>{"id": 295, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(296, <MapInfoModel>{"id": 296, "portalRequirements": [0], "maxOnScreen": 0}),
        new MapInfoBase(297, <MapInfoModel>{"id": 297, "portalRequirements": [0], "maxOnScreen": 0})    
]
}
