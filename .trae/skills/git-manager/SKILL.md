---
name: "git-manager"
description: "管理Git版本控制，包括提交代码、切换分支、远程仓库操作和状态查询。当用户需要执行Git相关命令或管理代码版本时调用。"
---

# Git Manager

## 功能概述

这个技能帮助您管理Git版本控制系统，提供以下核心功能：

- **提交管理**：添加文件、提交更改
- **分支管理**：创建、切换、删除分支
- **远程仓库**：推送、拉取、同步远程代码
- **状态查询**：查看工作区状态、提交历史

## 使用场景

当您需要：
- 提交代码更改到本地仓库
- 切换到不同的分支进行开发
- 将代码推送到远程仓库或从远程拉取更新
- 查看当前工作区状态或历史提交记录

## 常用命令示例

### 1. 提交管理

**添加文件**：
```bash
git add <file_path>
# 或添加所有更改
git add .
```

**提交更改**：
```bash
git commit -m "<commit_message>"
# 提交并跳过暂存区
git commit -a -m "<commit_message>"
```

### 2. 分支管理

**查看分支**：
```bash
git branch
# 查看远程分支
git branch -r
```

**创建分支**：
```bash
git branch <branch_name>
# 创建并切换到新分支
git checkout -b <branch_name>
```

**切换分支**：
```bash
git checkout <branch_name>
# 或使用新语法
git switch <branch_name>
```

**删除分支**：
```bash
git branch -d <branch_name>
# 强制删除
git branch -D <branch_name>
```

### 3. 远程仓库

**推送代码**：
```bash
git push <remote> <branch>
# 推送并设置上游分支
git push -u <remote> <branch>
```

**拉取代码**：
```bash
git pull <remote> <branch>
# 拉取并 rebase
git pull --rebase <remote> <branch>
```

**克隆仓库**：
```bash
git clone <repository_url>
```

### 4. 状态查询

**查看状态**：
```bash
git status
```

**查看提交历史**：
```bash
git log
# 简洁查看
git log --oneline
# 查看最近N次提交
git log -n <number>
```

**查看差异**：
```bash
git diff
# 查看暂存区和上次提交的差异
git diff --staged
```

## 工作流程示例

### 基本开发流程
1. 查看当前状态：`git status`
2. 添加更改：`git add .`
3. 提交更改：`git commit -m "feat: 添加新功能"`
4. 推送到远程：`git push origin main`

### 分支开发流程
1. 创建新分支：`git checkout -b feature-branch`
2. 开发并提交更改
3. 切换回主分支：`git checkout main`
4. 拉取最新代码：`git pull origin main`
5. 合并功能分支：`git merge feature-branch`
6. 推送合并结果：`git push origin main`

## 注意事项

- 执行Git命令前，请确保当前目录是Git仓库
- 推送代码前，建议先拉取最新代码以避免冲突
- 分支名称应简洁明了，反映分支的用途
- 提交信息应清晰描述更改内容，遵循团队规范

## 故障排除

**常见问题**：
- 合并冲突：需手动解决冲突文件后重新提交
- 推送失败：可能是权限问题或远程分支已更新，需先拉取
- 提交错误：可使用 `git commit --amend` 修改最后一次提交

**解决方法**：
- 冲突解决：编辑冲突文件，删除冲突标记，保留正确内容后 `git add` 并 `git commit`
- 权限问题：检查SSH密钥或HTTPS凭证是否正确
- 历史修改：使用 `git rebase` 或 `git reset` （谨慎使用）

## 输入输出示例

#### 输入输出示例

**示例1：提交代码**
输入：
```
我需要提交代码，文件已经修改好了
```

输出：
```bash
# 查看当前状态
git status

# 添加所有更改
git add .

# 提交更改
git commit -m "修改文件内容"

# 推送到远程
git push origin main
```

**示例2：切换分支**
输入：
```
我想切换到feature-branch分支
```

输出：
```bash
# 切换到feature-branch分支
git checkout feature-branch

# 验证当前分支
git branch
```

**示例3：查看提交历史**
输入：
```
我想查看最近5次提交记录
```

输出：
```bash
# 查看最近5次提交历史（简洁格式）
git log --oneline -n 5
```