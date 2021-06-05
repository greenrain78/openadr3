CREATE TABLE departments (
    `id`            INT          NOT NULL AUTO_INCREMENT,
    `name`          VARCHAR(25)  NOT NULL UNIQUE,
    `priority`      TINYINT      NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE  equipments_info (
    `id`            INT             NOT NULL AUTO_INCREMENT,
    `siteId`        VARCHAR(25)     NOT NULL ,
    `eqpCode`       VARCHAR(100)    NOT NULL,
    `eqpName`       VARCHAR(100)    NOT NULL,
    `eqpType`       VARCHAR(100)    NOT NULL,
    `perfId`        SMALLINT        NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE  power_info (
    `id`            INT             NOT NULL AUTO_INCREMENT,
    `pnName`        VARCHAR(25)     NOT NULL ,
    `eqpName`       VARCHAR(100)    NOT NULL,
    `perfId`        SMALLINT        NOT NULL,
    `ymdms`         VARCHAR(100)    NOT NULL,
    `amPere`        DOUBLE          NOT NULL,
    `arPower`       INT             NOT NULL,
    `atvPower`      INT             NOT NULL,
    `ratPower`      INT             NOT NULL,
    `pwFactor`      INT             NOT NULL,
    `accruePower`   INT             NOT NULL,
    `voltagerS`     DOUBLE          NOT NULL,
    `voltagesT`     DOUBLE          NOT NULL,
    `voltagetR`     DOUBLE          NOT NULL,
    `temperature`   DOUBLE          NOT NULL,
    PRIMARY KEY (id)
);