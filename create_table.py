import pymysql.cursors

connection = pymysql.connect('localhost', 'root', 'Balchand@123', 'medium_scraper',
                             cursorclass=pymysql.cursors.DictCursor)

create_table = """ create table if not exists `contents`(
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
              )"""


def insert_in_database(dev):
    try:
        with connection.cursor() as cursor:
            get_titles = "select `title` from `contents`"
            cursor.execute(get_titles)
            titles = cursor.fetchall()
            for title in titles:
                if title == {'title': dev['title']}:
                    update = "update `contents` set `title`=%s,`subtitle`=%s,`imageurl`=%s, `authername`=%s, " \
                             "`autherbio`=%s, `postdate`=%s, `content`=%s, `hashtags`=%s,`codes`=%s where `title` = %s"
                    cursor.execute(update, (
                        dev['title'], dev['subtitle'], dev['img_url'], dev['auther_name'], dev['auther_bio'],
                        dev['post_date'], dev['content'], dev['hash_tags'], dev['codes'], dev['title']))
                    connection.commit()
                    break
            else:
                sql = "insert into `contents`(`title`,`subtitle`,`imageurl`,`authername`,`autherbio`,`postdate`," \
                      "`content`,`hashtags`,`codes`) values ( %s,%s,%s,%s,%s,%s,%s,%s,%s ) "
                cursor.execute(sql, (
                    dev['title'], dev['subtitle'], dev['img_url'], dev['auther_name'], dev['auther_bio'],
                    dev['post_date'],
                    dev['content'], dev['hash_tags'], dev['codes']))
                connection.commit()

        with connection.cursor() as cursor:
            get = " select * from `contents`where `title` = %s "
            book = {}
            cursor.execute(get, dev['title'])
            results = cursor.fetchall()
            for result in results:
                book[result['id']] = result

    finally:
        connection.close()
    return book


def get_database_table():
    try:
        with connection.cursor() as cursor:
            get = " select * from `contents`"
            database = {}
            cursor.execute(get)
            results = cursor.fetchall()
            for result in results:
                database[result['id']] = result

    finally:
        connection.close()
    return database
