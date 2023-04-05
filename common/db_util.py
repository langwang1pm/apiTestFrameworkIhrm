import pymysql


class DBUtils():
    """数据库工具类"""
    conn = None

    @classmethod
    def __conn_create(cls):
        """
        创建连接的方法，单独封装
        多个sql只需要使用一个连接，因此不需要每个实例都创建一个连接，可以创建成类方法
        """
        if cls.conn is None:
            cls.conn = pymysql.connect(host="192.168.32.128",
                                       port=3306,
                                       user="root",
                                       password="123456",
                                       database="prictice",
                                       charset="utf8")
        return cls.conn

    @classmethod
    def __conn_close(cls):
        """关闭连接的方法，单独封装"""
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None

    @classmethod
    def queryone(cls, sql):
        """
        创建一个数据库连接
        :return:
        """
        cursor = None
        result = None
        try:
            # 创建连接，直接调用已经封装好的方法
            cls.conn = cls.__conn_create()
            # 创建游标
            cursor = cls.conn.cursor()
            # 执行sql语句
            cursor.execute(sql)
            result = cursor.fetchone()

        except Exception as err:
            print("查询一条记录报错：", print(err))
        finally:
            # 关闭游标
            cursor.close()
            # 关闭连接
            cls.__conn_close()
            # 返回结果
            return result

    @classmethod
    def querymany(cls, sql, n):
        """
        查询n条记录
        :return:
        """
        cursor = None
        result = None
        try:
            # 创建连接，直接调用已经封装好的方法
            cls.conn = cls.__conn_create()
            # 创建游标
            cursor = cls.conn.cursor()
            # 执行sql语句
            cursor.execute(sql)
            result = cursor.fetchmany(n)

        except Exception as err:
            print("查询n条记录报错：", print(err))
        finally:
            # 关闭游标
            cursor.close()
            # 关闭连接
            cls.__conn_close()
            # 返回结果
            return result

    @classmethod
    def insert_update_delete(cls, sql):
        """
        增删改语句
        :return:
        """
        cursor = None
        try:
            # 创建连接，直接调用已经封装好的方法
            cls.conn = cls.__conn_create()
            # 创建游标
            cursor = cls.conn.cursor()
            # 执行sql语句
            cursor.execute(sql)
            cls.conn.commit()

        except Exception as err:
            cls.conn.rollback()
            print("查询一条记录报错：", print(err))
        finally:
            # 关闭游标
            cursor.close()
            # 关闭连接
            cls.__conn_close()


if __name__ == '__main__':
    sql1 = "select * from prictice.student where SNO = 'S0001'"
    res1 = DBUtils.queryone(sql1)
    print(res1)

    sql2 = "select * from prictice.student"
    res2 = DBUtils.querymany(sql2, 5)
    print(res2)


    sql3 = "insert into prictice.student (SNO ,Sname ,Sage ,Ssex) values ('S0015','张一','18','女')"
    DBUtils.insert_update_delete(sql3)

    sql4 = "update prictice.student set Sage = '29' where Sname = '张二'"
    DBUtils.insert_update_delete(sql4)

    sql5_1 = "insert into prictice.student (SNO ,Sname ,Sage ,Ssex) values ('S0015','张四','18','女')"
    DBUtils.insert_update_delete(sql5_1)
    sql5_2 = "delete from prictice.student where Sname = '张四' ;"

    DBUtils.insert_update_delete(sql5_2)