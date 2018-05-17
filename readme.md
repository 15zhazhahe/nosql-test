# 文件结构说明：

```
.
├── clean_data		-- 便于画图以及交互从整体数据集里抽离的数据
│   ├── freq.txt		-- 所有频率，用于构建web交互的select下拉框
│   ├── phi.txt		-- 所有phi，用于构建web交互的select下拉框
│   └── theta.txt		-- 构建画图的x轴所需的参数
├── docs			-- 课设文件描述以及数据
│   ├── angle_data_plot.m
│   ├── export_low_small.txt
│   ├── NoSQL数据库课程报告_模板.docx
│   ├── NoSQL数据库课程考核.docx
│   ├── NoSQL数据库课程考核-数据文件说明.doc
│   └── sample.txt
├── draw					-- web展示的Flask代码
│   ├── __pycache__
│   │   └── server.cpython-36.pyc
│   ├── server.py				-- 后台代码，用于响应请求
│   └── templates				-- 前端代码html模板
│       ├── index.html			-- 主界面，用于数据交互以及画图请求
│       └── pyecharts.html			-- pyecharts画图的渲染界面
├── img					-- 实验结果截图
│   ├── mapreduce查询结果.png
│   ├── mapreduce的python实现.png
│   ├── mapreduce构建.png
│   ├── mongodb存入数据的部分展示.png
│   ├── pandas读取数据部分展示.png
│   ├── web画图结果展示.png
│   ├── 加载绘图所需的参数选择.png
│   ├── 数据处理以及导入.png
│   └── 响应POST请求进行绘图.png
├── insert_data.py				-- 将数据导入至数据库
├── main.ipynb				-- 初步思路的代码构建
├── NoSQL数据库课程报告.docx		-- 实验报告
├── readme.md				-- 部分文档说明
└── vedio.mp4				-- 程序结果录屏展示
```

# 环境：

+ pymongo v3.6.1
+ linux deepin15.5桌面版
+ python v3.6.4
+ mongo v3.6.4
+ flask v0.12.2

# 运行方式

+ main.ipynb 直接用jupyter notebook打开即可

```bash
jupyter notebook
```

+ draw 打开方式为

```bash
cd draw
python3 server.py
```

# 参考文献

+ [MongoDB 教程|菜鸟教程](http://www.runoob.com/mongodb/mongodb-tutorial.html)
+ [HTML 教程 | W3school](http://www.w3school.com.cn/html/index.asp)
+ [AJAX 教程 | W3school](http://www.w3school.com.cn/ajax/index.asp)
+ [Flask 中文文档 | 一译](https://yiyibooks.cn/yiyi/flask_011_ch/index.html)
+ [pyecharts 中文文档](http://pyecharts.org/#/zh-cn/)
+ [博客:MongoDB:MapReduce基础及实例](https://www.cnblogs.com/Joe-T/p/4264910.html)
+ 《NoSQL数据库技术实战》皮雄军 著