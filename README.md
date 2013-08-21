python-tornado-django
=====================

practice

	sudo apt-get install python-setuptools && sudo easy_install supervisor

	wget https://github.com/bmbouter/supervisord_init_script/raw/master/supervisord

	#sudo apt-get install python-pip && sudo pip install tornado && sudo pip install Django==1.5.1

	wget https://pypi.python.org/packages/source/t/tornado/tornado-3.1.tar.gz

	tar xvzf tornado-3.1.tar.gz
	cd tornado-3.1
	python setup.py build
	sudo python setup.py install

	wget https://www.djangoproject.com/m/releases/1.5/Django-1.5.1.tar.gz

	tar xzvf Django-1.5.1.tar.gz
	cd Django-1.5.1
	python setup.py build
	sudo python setup.py install

运行python输入：
>>>  import django
>>>  django.VERSION
显示： (1, 5, 1, 'final', 0) 则安装成功。


创建Django工程：
django-admin.py startproject djdemo

<http://amazingjxq.com/2013/05/03/djangotornado>

https://github.com/rjdj/django-tornado


supervisord:
子配置文件

举个例子, 我们只需新建一个子配置文件 /etc/supervisor/conf.d/django.conf:

[program:mydjango]
command = /srv/mydjango/ENV/bin/python /srv/mydjango/manage.py runwsgiserver

为了方便管理, 每个后台守护应用对应一个 /etc/supervisor/conf.d/[program-name].conf 子配置文件
program: 后跟随的 mydjango 指明后台守护应用的代号, supervisorctl 需要用该代号控制守护进程的启动/停止.
program 区的更多配置请参考: [program:x] Section Settings
子配置基本上只需关心 program 区
command 字段设置的是后台守护应用的启动命令, 注意: 该命令必须是在前台执行的, 即会独占控制台, 否则会导致 supervisor 无法获得标准输出, 并失去进程的控制权.

控制守护进程

每次 修改主配置文件 或 增改子配置文件 都需要执行 supervisorctl update 使新配置生效:
    sudo supervisorctl update
控制守护进程:
    # 控制所有进程
    sudo supervisorctl start all
    sudo supervisorctl stop all
    sudo supervisorctl restart all

    # 定向控制指定进程
    sudo supervisorctl stop iot-kb
    sudo supervisorctl start iot-kb
    sudo supervisorctl restart iot-kb
supervisorctl 子命令

$ supervisorctl help

add    clear  fg        open  quit    remove  restart   start   stop  update
avail  exit   maintail  pid   reload  reread  shutdown  status  tail  version
