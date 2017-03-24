CREATE TABLE `xo_db`.`stat_player_registration` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `target_date` DATE NOT NULL COMMENT '',
  `register_count` INT NOT NULL COMMENT '',
  `created` DATETIME NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '');


INSERT INTO `xo_db`.`stat_player_registration` (`id`, `target_date`, `register_count`, `created`) VALUES ('1', '2016-01-06 10:59:59', '3', '2016-01-28 20:18:49');
INSERT INTO `xo_db`.`stat_player_registration` (`id`, `target_date`, `register_count`, `created`) VALUES ('2', '2016-01-09 21:59:59', '2', '2016-01-28 20:18:49');
INSERT INTO `xo_db`.`stat_player_registration` (`id`, `target_date`, `register_count`, `created`) VALUES ('3', '2016-01-10 22:59:59', '4', '2016-01-28 20:18:49');