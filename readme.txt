git-tag op:

*添加文件/文件夹/所有：  
 git add AndroidManifest.xml //添加单个文件
 git add src //添加文件夹
 git add . //添加所有
*提交：  
 git commit -m "First commit"
*clone仓库 (假设远程版本库的Git地址是： https://github.com/exmaple/test.git)                         
 git clone  https://github.com/exmaple/test.git
*如果要推送到GitHub，使用命令：
 git push github master
 如果要推送到码云，使用命令：
 git push gitee master
*用命令git clone克隆一个本地库：
 $ git clone git@github.com:michaelliao/gitskills.git
*查看远程仓库信息
 git remote -V
 关联仓库
 git remote add github git@github.com:michaelliao/learngit.git
               /gitee git@gitee.com:liaoxuefeng/learngit.git

