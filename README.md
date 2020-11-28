# OneKeyDLUT-Eda
一键连接大连理工大学开发区校区的DLUT-Eda网络,vbs和bat适用于win10



## 1使用方法:

#### 1.1文件配置

克隆或下载zip包

`gh repo clone WentaoHao/OneKeyDLUT-Eda`

打开login_sch_net.pyw文件,填入学号密码;
连接dlut-eda wifi;
双击l.vbs文件即可联网 (建议首先使用l.bat调试).

#### 1.2环境配置

需要python3和requests,安装环境必要时需要在全局代理环境下进行.

`pip install requests`

#### 1.3开机自启

`win+r`输入 `shell:shartup` 在文件夹里面放一个`l.vbs`的快捷方式 就可以开机自启动.

如果需要休眠等操作后重新连接,建议为`l.vbs`创建开始菜单快捷方式或创建win+r启动快捷方式,请自行发挥.

## 2 debug

未能成功连接时,请双击l.bat文件查看报错.

pip命令卡住需要挂全局代理或自行寻找其他解决方案.

## 3 鸣谢

感谢DiDong提供的连接脚本  https://github.com/DiDongDongDi/schnet