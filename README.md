# 树莓派上git命令行设定
git config --global user.name “Your Name”  
git config --global user.email youremail@whatever.com
# 检查设定
git config --list
# 1小时内免敲密码
git config --global credential.helper 'cache --timeout 3600'
# 克隆本项目
git clone https://github.com/CASTIC2019/Team
# 刷新本项目
git pull
# 提交修改
git commit -a  
git push

# Markdown 转 word
1. 问题描述
用过markdown的朋友都知道，markdown语法简洁，写作效率极高，非常适合网络博客、邮件、笔记等非正式文档的写作。但对于格式复杂的正式报告、论文、项目计划书等正式文档是不适合的，无法满足精细排版的要求。

解决这一矛盾的基本思路是，在markdown中写作完成初稿，之后在word中进行精细化排版设置。这就需要markdown转换word。以前一直没有找到合适的工具，今天终于发现了一个理想的工具：Writage。

2. 技术背景

Writage是一款word插件，下载网址为：http://www.writage.com/
功能：支持markdown与word互相转换

安装：

Writage，word插件

Pandoc，文档转换后台软件

实际上实现文档格式转换的是pandoc软件，Writage作为word插件，将pandoc的功能集成到了word选项中，避免了繁琐的cmd
命令操作。

3. 解决方案

安装Writage和Pandoc软件后，word中不会直接出现选项卡，但在【打开】和【保存】的对话框中会出现相关的选项，如下：

3.1 markdown转换word

通过word软件打开markdown文件实现：


打开原markdown文档后，另存为word格式即可；


