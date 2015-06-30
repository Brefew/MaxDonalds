
CREATE DATABASE `maxdonalds` /*!40100 DEFAULT CHARACTER SET latin1 */$$


CREATE TABLE `data` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Type` varchar(45) NOT NULL,
  `Calories` int(11) NOT NULL,
  `TotalFat` int(11) NOT NULL,
  `Carohydrates` int(11) NOT NULL,
  `Protein` int(11) NOT NULL,
  `Sodium` int(11) NOT NULL,
  `Price` int(11) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=latin1$$



/*
-- Query: SELECT * FROM maxdonalds.data
LIMIT 0, 1000

-- Date: 2015-06-30 06:13
*/
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (2,'Side Salad','Salad',15,0,3,1,10,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (3,'Small Iced Coffee','Drink',130,5,22,1,35,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (4,'Small Soda','Drink',140,0,0,0,0,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (5,'Parfait ','Dessert',150,2,30,4,80,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (6,'Small Sweet Tea','Drink',150,0,0,0,10,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (7,'Cookie','Dessert',160,8,21,2,90,0);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (8,'Cone','Dessert',170,5,27,5,70,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (9,'Medium Sweet Tea','Drink',180,0,0,0,10,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (10,'Medium Iced Coffee','Drink',180,7,29,1,50,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (11,'4 Pc. Chicken McNuggets','Chicken',190,12,12,9,360,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (12,'Medium Soda','Drink',200,0,0,0,0,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (13,'Small Fries','Fries',230,11,30,2,130,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (14,'Hamburger','Burger',240,8,32,12,480,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (15,'Apple Pie','Dessert',250,13,32,2,170,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (16,'Large Iced Coffee','Drink',260,9,43,2,65,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (17,'Large Soda','Drink',280,0,0,0,0,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (18,'Cheeseburger','Burger',290,11,33,15,680,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (19,'Ranch Snack Wrap (Grilled)','Chicken',290,13,25,18,810,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (20,'Bacon Ranch Salad with Grilled Chicken','Salad',300,14,9,37,1100,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (21,'Sundae','Dessert',330,9,53,8,170,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (22,'BBQ Ranch Burger','Burger',340,15,37,15,670,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (23,'Small Oreo  McFlurry','Dessert',340,11,53,8,190,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (24,'Medium Fries','Fries',340,16,44,4,190,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (25,'Artisan Grilled Chicken Sandwich','Chicken',360,6,43,32,930,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (26,'Ranch Snack Wrap (Crispy)','Chicken',360,20,32,15,810,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (27,'McChicken','Chicken',370,17,40,14,650,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (28,'McDouble','Burger',380,17,34,22,840,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (29,'Filet-O-Fish','Fish',390,19,39,15,590,4);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (30,'McWrap Sweet Chili Chicken(Grilled)','Chicken ',400,10,47,31,1260,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (31,'Jalapeno Double','Burger',430,23,35,22,1030,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (32,'Double Cheeseburger','Burger',430,21,35,24,1040,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (33,'Small M&M\'s McFlurry','Dessert',430,15,64,9,120,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (34,'Bacon McDouble','Burger',440,22,35,27,1110,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (35,'Bacon McDouble','Burger',440,22,35,27,1110,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (36,'Small Frappe','Drink ',440,18,64,7,125,3);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (37,'Bacon Ranch Salad with Crispy Chicken','Salad',450,26,23,30,1100,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (38,'McWrap Chicken & Ranch (Grilled)','Chicken ',470,19,42,34,1350,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (39,'Southwest Salad with Crispy Chicken','Salad',470,24,40,24,890,6);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (40,'10 Pc. Chicken McNuggets','Chicken',470,30,30,22,900,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (41,'3 Cookies','Dessert',480,24,63,6,270,1);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (42,'McWrap Chicken & Bacon (Grilled)','Chicken',500,19,41,40,1550,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (43,'Oreo McFlurry','Dessert',510,17,80,12,280,3);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (44,'Large Fries','Fries',510,24,67,6,290,2);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (45,'Quarter Pounder with Cheese','Burger',520,26,42,29,1110,4);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (46,'Big Mac','Burger',530,27,47,24,960,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (47,'Crispy Chicken Delux Sandwich','Chicken',530,22,59,25,1000,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (48,'McWrap Sweet Chili Chicken (Crispy)','Chicken',540,23,61,24,1260,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (49,'Medium Frappe','Drink',540,22,79,9,160,3);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (50,'Small Shake','Dessert',550,16,90,12,160,3);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (51,'McWrap Chicken & Bacon (Crispy)','Chicken',640,32,56,33,1550,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (52,'M&M\'s McFlurry','Dessert',650,23,96,13,180,3);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (53,'Large Frappe','Drink',670,26,97,11,190,4);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (54,'Medium Shake','Dessert',700,30,114,15,300,3);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (55,'Double Quarter Pounder with Cheese','Burger',740,40,43,47,1300,6);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (56,'Crispy Chicken Bacon Clubhouse Sandwich','Chicken',750,38,65,36,1720,5);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (57,'Large Shake','Dessert',850,23,141,19,380,3);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (58,'20 Pc. Chicken McNuggets','Chicken',940,59,59,44,1800,6);
INSERT INTO `data` (`Id`,`Name`,`Type`,`Calories`,`TotalFat`,`Carohydrates`,`Protein`,`Sodium`,`Price`) VALUES (59,'40 Pc. Chicken McNuggets','Chicken',1880,118,118,87,3600,10);
