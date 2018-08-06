# Social_blog

##程序主要功能简单介绍

该社交博客程序用python语言的Flask框架开发， 使用了bootstrap模板， 支持Web表单， 数据库， 电子邮件发送， 用户注册， 用户登陆， 用户认证， 不同用户有不同权限， 用户可以编辑文章， 提交评论， 编辑资料， 用户之间的相互关注（自引用多对多关系）， 支持Rest Web， 程序测试等功能。
还包括简单的的sql注入， xxs攻击， 文件上传攻击， 命令执行漏洞页面展示， 并对漏洞进行了修复。

##程序主要功能页面截图

###1)程序主页
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/1.png)
底部的页面导航
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/1.1.png)

###2)登陆页面
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/2.png)

###3)注册页面
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/3.png)

###4)注册以后提示去邮箱验证账号
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/4.png)

###5)如果未验证， 登陆以后显示提醒页面
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/5.png)

###6)去邮箱点击验证链接
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/6.png)

###7)跳转到登陆页面， 登陆以后提示验证成功
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/7.png)

###8)用户资料页面
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/8.png)

###9)查看自己的专注者和被关注者
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/9.png)

###10)编辑自己的资料
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/10.png)

###11)评论管理员管理评论是否可见
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/11.png)

###12)漏洞导航
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/12.png)

###13)漏洞页面
![Image text](https://github.com/mytail2/Social_blog/blob/master/img/13.png)

##启动方法
###1）安装virtulenv， 进入程序文件夹， 用virtulenv安装虚拟环境， 激活虚拟环境， 在虚拟环境里安装需要的扩展（requirements.txt里面）
###2）启动服务器python manage.py runserver
###2）打开浏览器， 访问shell提示的网址127.0.0.1：5000







