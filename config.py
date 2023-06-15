import os

bind = '0.0.0.0:' + str(os.getenv('PORT', 18002))
proc_name = 'gunicorn_step02'
workers = 1
