-- MySQL Script generated by MySQL Workbench
-- Sun Sep  9 00:38:35 2018
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema alphadata
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema alphadata
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `alphadata` DEFAULT CHARACTER SET utf8 ;
USE `alphadata` ;


-- -----------------------------------------------------
-- Table `alphadata`.`sma7`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`sma7` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`sma7` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `sma` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_sma7`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`apo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`apo` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`apo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `apo` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_apo`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`cmo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`cmo` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`cmo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `cmo` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_cmo`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`aroon`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`aroon` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`aroon` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `aroon_up` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `aroon_down` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_aroon`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`mfi`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`mfi` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`mfi` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `mfi` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_mfi`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`dx`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`dx` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`dx` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `dx` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_dx`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`bbands`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`bbands` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`bbands` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `real_upper_band` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `real_middle_band` VARCHAR(45) NOT NULL,
  `real_lower_band` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_bbands`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`ad`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`ad` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`ad` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `chaikin_ad` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_ad`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`obv`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`obv` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`obv` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `obv` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_obv`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`ema12`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`ema12` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`ema12` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `ema` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_ema12`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`wma`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`wma` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`wma` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `wma` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_wma`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`t3`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`t3` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`t3` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `t3` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_t3`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`macd`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`macd` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`macd` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `macd_hist` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `macd` VARCHAR(45) NOT NULL,
  `macd_signal` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_macd`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`stoch`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`stoch` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`stoch` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `slowd` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `slowk` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_stoch`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`rsi`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`rsi` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`rsi` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `rsi` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_rsi`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`stochrsi`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`stochrsi` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`stochrsi` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `fastd` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `fastk` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_stochrsi`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`willr`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`willr` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`willr` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `willr` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_willr`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`adx`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`adx` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`adx` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `adx` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_adx`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`mom`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`mom` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`mom` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `mom` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_mom`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`cci`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`cci` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`cci` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `cci` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_cci`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`ht_trendline`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`ht_trendline` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`ht_trendline` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `ht_trendline` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_ht_trendline`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`macdext`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`macdext` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`macdext` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `macd_hist` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `macd` VARCHAR(45) NOT NULL,
  `macd_signal` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_macdext`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`basic`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`basic` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`basic` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `open` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `close` VARCHAR(45) NOT NULL,
  `high` VARCHAR(45) NOT NULL,
  `low` VARCHAR(45) NOT NULL,
  `volume` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_basic`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`ema24`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`ema26` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`ema26` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `ema` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_ema26`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`sma30`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`sma30` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`sma30` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `sma` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_sma30`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`sma180`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`sma180` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`sma180` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `stock_id` INT NOT NULL,
  `sma` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `stock_id_idx` (`stock_id` ASC),
  CONSTRAINT `stock_id_sma180`
    FOREIGN KEY (`stock_id`)
    REFERENCES `alphadata`.`stocks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
