USE stock;
DROP TABLE IF EXISTS `stockname`;

CREATE TABLE
`stockname` (
'index' varchar(10) ,

`symbol` varchar(10) COMMENT '股票代码',

`name` varchar(10) COMMENT '日期',

PRIMARY KEY (`symbol`)

) ENGINE = InnoDB DEFAULT CHARSET=utf8;
