## 激活系统Python虚拟环境

执行这个命令时，shell会话将被配置为使用虚拟环境中的Python解释器和库，而不是系统默认的Python版本。任何Python相关的命令都会使用虚拟环境中的Python解释器和库。可以安装、升级和卸载包，而不会影响系统级别的Python环境。e.g.

创建并激活当前项目虚拟环境
~~~
python3 -m venv /path/to/your/project/venv  #创建
source /Users/Waiting/PycharmProjects/TubeSavely/venv/bin/python/bin/activate #激活
~~~

查看当前虚拟环境路径

~~~
echo $PYTHONPATH
~~~

退出虚拟环境

~~~
deactivate
~~~

生成当前虚拟环境所有依赖库列表文件

~~~
pip freeze > requirements.txt
~~~

安装requirements.txt

~~~
pip install -r requirements.txt
