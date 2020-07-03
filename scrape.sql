use medium_scraper;

create table if not exists `contents`(
              `id` int not null primary key auto_increment,
              `title` varchar(100) not null,
              `subtitle` text ,
              `imageurl` text ,
              `authername` varchar(100),
              `autherbio` varchar(250) ,
              `postdate` date ,
              `content` text ,
              `hashtags` text ,
              `codes` text
              )