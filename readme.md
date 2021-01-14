将imagenet数据集下载并且导入
====
一、首先将数据集从官网下载下来
----
这里给出官网下载的链接：http://www.image-net.org/download-images \
如果想要下载原始图片，需要注册一个账号，注册邮箱需要带有 edu，即学校邮箱。

本代码的操作主要针对原始图片的下载及分类任务数据集的处理，点击进入下载原图的页面后，\
可以看到一系列内容，一般我们会下载 `ILSVRC 2012` 作为实验数据。

## 1、关于 Images

>>`Training images (Task 1 & 2). 138GB.` 

>>`Training images (Task 3). 728MB.`

>>`Validation images (all tasks). 6.3GB.`

>>`Test images (all tasks). 13GB.` 

>>#### 其中
>>训练集图片：1,281,167 张，每个类含有图片数量 732-1300；\
>>验证集图片：50,000 张， 每个类含有图片数量 50 张； \
>>测试集图片：100,000 张，每个类含有图片数量 100 张。\

>>`Task 1 & 2` 代表分别代表分类和定位任务；  

>>`Task 3 ` 代表目标检测任务，一般如果只是分类，下载 `Task 1 & 2` 即可。

### 3 、关于Development Kit
>>`Development kit (Task 1 & 2). 2.5MB.` 里面包含了 `Task 1 & 2` 中训练集的标签，需要其中的 `meta.mat` 和 `ILSVRC2012_validation_ground_truth.txt` 文件对 val数据集进行处理。

>>`Development kit (Task 3). 22MB.` 里面包含了 `Task 3` 中训练集的标签文件.


### 4、下载建议
imagenet 数据集很大，常规浏览器下载很慢。以下建议：

（1）、采用 `Internet Download Manager` 下载器帮助下载；

（2）、去网上找网友提供的网盘下载，或许开个会员会快点。

二、数据解压，并归档(sh 脚本针对 Linux， windows 请手动解压)
----
### 1、解压
在pre_data文件夹中，有写好的脚本来处理压缩文件：
>>关于训练集

运行 ```bash trainprep.sh```
处理过程：\
（1）在当前文件夹中新建 train 文件夹，将当前文件夹中的压缩包复制到 train 文件中;\
（2）进入 train 文件夹中，解压压缩包并且删除;\
（3）解压之后得到多个压缩文件，继续解压，创建对应的文件夹来保存解压出来的图片。

>>关于验证集(`valprep.sh` + `valprep.py`)

处理过程：\
运行 ```bash valprep.sh```\
（1）在当前文件夹中新建 val 文件夹，将当前文件夹中的压缩包复制到 val 文件中;\
（2）进入 val 文件夹中，解压压缩包并且删除;\
（3）解压出来全部图片; \
运行 `python valprep.py` \
（4）根据 `Development kit(Task 1 & 2)` 中的文件对 val 数据集图片进行归档.
>>关于测试机 `bash testprep.sh`

处理过程：\
运行 ```bash testprep.sh```\
（1）在当前文件夹中新建 test 文件夹，将当前文件夹中的压缩包复制到 test 文件中;\
（2）进入 test 文件夹中，解压压缩包并且删除；\
（3）解压出来全部图片。

三、使用 `pytorch` 将图片导入
----
处理过程：\
运行 ```bash valprep.sh```\
此时代码中，使用 `datasets.ImageFolder` 导入数据集，将 `path` 改为 imagenet 所在路径即可，imagenet 文件夹中需要含有 train、val 和 test 三个数据文件。

`datasets.ImageFolder`需要从子文件夹中读取数据，所以每个类别的数据需要放在一个文件夹中。

四、资料参考
----
### 1、代码来源
https://blog.csdn.net/weixin_43002433/article/details/106225771\
我对其中某些部分代码进行了小修

### 2、资料参考
https://www.cnblogs.com/zjutzz/p/6083201.html \
https://blog.csdn.net/fengbingchun/article/details/88606621 \
https://blog.csdn.net/qq_43205738/article/details/86543766
