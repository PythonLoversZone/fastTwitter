# 使用步骤1
在 [application manager](https://apps.twitter.com/app/new) 上创建一个app, 你将会得到我们所需要的相关信息
![](screen/key.png)

# 使用步骤 2
打开 'cfg.json'文件, 修改成你自己账号的配置

![](screen/config.png)

# 使用步骤 3
- 功能1: 批量关注
> 打开文件 'follow.py',右键,选择 `run` 命令。
- 功能2: 批量取关
> 打开文件 'unfollow.py', 右键,选择`run` 命令。 这是个危险的操作,所以会在`config`目录生成一个名为`unfollow.txt`的备份文件，以便随时加回来。
![](screen/run.png)

# 修改你要关注的人
如果你想添加或修改想要follow的人, 你可修改 `follow.txt`这个文件

![](screen/followers.png)

# 祝你好运
如果在使用过程中有任何问题请随时联系

# 相关链接
- 名单来自于[知乎](https://www.zhihu.com/question/26499017)
- 日志配置参考:[Python 日志功能详解](https://blog.igevin.info/posts/python-log/)
- 使用的库:[tweepy](http://docs.tweepy.org/en/latest/getting_started.html)

# license
```
MIT License

Copyright (c) 2018 Peng Hu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
```