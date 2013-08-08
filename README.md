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
