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



