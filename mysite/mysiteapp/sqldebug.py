#coding=utf8
from django.db import connection
class PrintSQL(object):
  def process_response(self, request, response):
    temp = 0
    for x in connection.queries:
      print x
      temp += float(x['time'])
    print 'time count:',temp,'=' * 40
