## 知鱼财经
一个小型的新闻媒体平台，因所做项目倒闭，现将其代码开源

### 一.项目部署

在部署代码前，你需要安装 python 3.8 以上版本，Mysql 数据库和 Redis

第一步，克隆代码：
```buildoutcfg
git clone git@github.com:guoshijiang/columbus.git
```

第二步，搭建一个 virtualenv：
```buildoutcfg
cd columbus
virtualenv .env
source .env/bin/activate
```

第三步，安装依赖：
```buildoutcfg
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

第四步，数据库migrate：
```buildoutcfg
 python3 manage.py migrate
```
如果你改变数据库结构，请先运行 `python3 manage.py makemigrations`, 然后再运行 `python3 manage.py migrate`

第五步，运行服务：
```buildoutcfg
 python3 manage.py runserver
```

如果你在线上部署，建议使用，supervisor 管理进程，Ng 转发，把静态文件使用 `python3 manage.py collectstatic` 收集到相应的目录。

### 二.有问题联系

如果您使用这套代码，开发搭建过程中有任何问题，可以去问我学院（www.wenwoha.com） 上面找联系方式联系我们，也可以直接加我的微信：LGZAXE


### 三.部分功能截图



