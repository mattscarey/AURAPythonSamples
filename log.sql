SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema alphadata
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table `alphadata`.`log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`log` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`log` (
  `log_id` INT NOT NULL AUTO_INCREMENT,
  `time` TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`log_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`scripting_log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`scripting_log` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`scripting_log` (
  `scripting_log_id` INT NOT NULL AUTO_INCREMENT,
  `message` VARCHAR(256) NULL,
  `time` TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
  `log_id` INT NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`scripting_log_id`),
  INDEX `log_id_idx` (`log_id` ASC),
  CONSTRAINT `log_s_id`
    FOREIGN KEY (`log_id`)
    REFERENCES `alphadata`.`log` (`log_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`configuration_log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`configuration_log` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`configuration_log` (
  `configuration_log_id` INT NOT NULL AUTO_INCREMENT,
  `message` VARCHAR(256) NULL,
  `time` TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
  `log_id` INT NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`configuration_log_id`),
  INDEX `log_id_idx` (`log_id` ASC),
  CONSTRAINT `log_c_id`
    FOREIGN KEY (`log_id`)
    REFERENCES `alphadata`.`log` (`log_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`investor_log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`investor_log` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`investor_log` (
  `investor_log_id` INT NOT NULL AUTO_INCREMENT,
  `message` VARCHAR(256) NULL,
  `time` TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
  `log_id` INT NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`investor_log_id`),
  INDEX `log_id_idx` (`log_id` ASC),
  CONSTRAINT `log_i_id`
    FOREIGN KEY (`log_id`)
    REFERENCES `alphadata`.`log` (`log_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`backtester_log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`backtester_log` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`backtester_log` (
  `backtester_log_id` INT NOT NULL AUTO_INCREMENT,
  `message` VARCHAR(256) NULL,
  `time` TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
  `log_id` INT NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`backtester_log_id`),
  INDEX `log_id_idx` (`log_id` ASC),
  CONSTRAINT `log_b_id`
    FOREIGN KEY (`log_id`)
    REFERENCES `alphadata`.`log` (`log_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`account_log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`account_log` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`account_log` (
  `account_log_id` INT NOT NULL AUTO_INCREMENT,
  `message` VARCHAR(256) NULL,
  `time` TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
  `log_id` INT NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`account_log_id`),
  INDEX `log_id_idx` (`log_id` ASC),
  CONSTRAINT `log_a_id`
    FOREIGN KEY (`log_id`)
    REFERENCES `alphadata`.`log` (`log_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `alphadata`.`error_log`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `alphadata`.`error_log` ;

CREATE TABLE IF NOT EXISTS `alphadata`.`error_log` (
  `error_log_id` INT NOT NULL AUTO_INCREMENT,
  `message` VARCHAR(256) NULL,
  `time` TIMESTAMP(6) DEFAULT CURRENT_TIMESTAMP(6),
  `log_id` INT NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`error_log_id`),
  INDEX `log_id_idx` (`log_id` ASC),
  CONSTRAINT `log_e_id`
    FOREIGN KEY (`log_id`)
    REFERENCES `alphadata`.`log` (`log_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
