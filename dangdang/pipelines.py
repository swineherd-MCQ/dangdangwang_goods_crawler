# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host='127.0.0.1',user="root",passwd="123456",db="dangdang")
        cursor = conn.cursor()
        for i in range(len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i]
            # print(title+":"+link+":"+comment)
            sql="insert into goods(title,link,comment) values('%s','%s','%s')"%(title,link,comment)
            # print(sql)
            try:
                cursor.execute(sql)
                conn.commit()
            except Exception as e:
                print(e)
        conn.close()
        return item
