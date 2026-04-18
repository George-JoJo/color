# VS Code 使用指南

> 一份面向初学者与进阶用户的 Visual Studio Code（以下简称 VS Code）完整使用手册，涵盖安装、界面、快捷键、插件、调试、Git、远程开发与常见问题等内容。

---

## 目录

1. [简介](#1-简介)
2. [安装与初次启动](#2-安装与初次启动)
3. [界面概览](#3-界面概览)
4. [常用快捷键](#4-常用快捷键)
5. [文件与工作区管理](#5-文件与工作区管理)
6. [编辑技巧](#6-编辑技巧)
7. [终端与任务](#7-终端与任务)
8. [插件（Extensions）](#8-插件extensions)
9. [调试（Debug）](#9-调试debug)
10. [Git 与版本控制](#10-git-与版本控制)
11. [远程开发](#11-远程开发)
12. [用户设置与主题](#12-用户设置与主题)
13. [代码片段（Snippets）](#13-代码片段snippets)
14. [常见问题（FAQ）](#14-常见问题faq)
15. [参考资源](#15-参考资源)

---

## 1. 简介

Visual Studio Code 是微软发布的一款免费、开源、跨平台（Windows / macOS / Linux）的轻量级代码编辑器。它具有以下特点：

- **轻量快速**：启动与响应速度快，占用资源少。
- **插件生态**：拥有庞大的插件市场，几乎支持所有主流语言和框架。
- **内置 Git**：开箱即用的源代码管理。
- **强大调试**：内置调试器，支持多语言扩展。
- **远程开发**：通过 SSH、WSL、容器等进行远程编辑。
- **IntelliSense**：智能代码补全与类型提示。

---

## 2. 安装与初次启动

### 2.1 下载与安装

从官方网站下载对应平台安装包：<https://code.visualstudio.com/>

- **Windows**：下载 `.exe` 后双击安装，建议勾选"添加到 PATH"与"在右键菜单中打开"选项。
- **macOS**：下载 `.zip` 解压，将 `Visual Studio Code.app` 拖入 `Applications` 目录。
- **Linux**：Debian/Ubuntu 使用 `.deb`，RHEL/Fedora 使用 `.rpm`，或直接使用包管理器：

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install code

# macOS (Homebrew)
brew install --cask visual-studio-code

# Arch Linux
sudo pacman -S code
```

### 2.2 添加命令行启动（macOS / Linux）

在 VS Code 中按 `Cmd/Ctrl + Shift + P` 打开命令面板，输入并执行：

```
Shell Command: Install 'code' command in PATH
```

之后即可在终端使用 `code .` 打开当前目录。

### 2.3 初次启动建议

- 设置界面语言：命令面板 → `Configure Display Language` → 选择 `zh-cn`（需安装 Chinese 语言包插件）。
- 选择主题：`Ctrl/Cmd + K`，再按 `Ctrl/Cmd + T` 切换主题。
- 登录账户以开启设置同步（Settings Sync）。

---

## 3. 界面概览

VS Code 的主要界面由以下区域组成：

| 区域                 | 说明                                                         |
| -------------------- | ------------------------------------------------------------ |
| 活动栏（Activity Bar） | 最左侧竖直栏：资源管理器、搜索、Git、调试、插件等入口。         |
| 侧边栏（Side Bar）     | 显示当前视图（文件、搜索结果等）。                             |
| 编辑器区（Editor）     | 文件编辑主区域，支持多文件分栏。                               |
| 面板（Panel）          | 底部区域：终端、输出、问题、调试控制台。                      |
| 状态栏（Status Bar）   | 底部显示分支、错误、编码、行列等信息。                        |
| 命令面板（Command Palette） | 通过 `Ctrl/Cmd + Shift + P` 打开，几乎所有操作都可在此执行。 |

---

## 4. 常用快捷键

> 以下快捷键以 Windows / Linux 为主，macOS 将 `Ctrl` 替换为 `Cmd`，`Alt` 替换为 `Option`。

### 4.1 通用

| 功能          | 快捷键                 |
| ------------- | ---------------------- |
| 命令面板      | `Ctrl + Shift + P`     |
| 快速打开文件  | `Ctrl + P`             |
| 打开设置      | `Ctrl + ,`             |
| 切换侧边栏    | `Ctrl + B`             |
| 打开终端      | `` Ctrl + ` ``         |
| 新建窗口      | `Ctrl + Shift + N`     |
| 关闭窗口      | `Ctrl + Shift + W`     |

### 4.2 文件与编辑

| 功能          | 快捷键                   |
| ------------- | ------------------------ |
| 新建文件      | `Ctrl + N`               |
| 保存          | `Ctrl + S`               |
| 全部保存      | `Ctrl + K` `S`           |
| 关闭文件      | `Ctrl + W`               |
| 撤销 / 重做   | `Ctrl + Z` / `Ctrl + Y`  |
| 剪切整行      | `Ctrl + X`（未选中时）   |
| 复制整行      | `Ctrl + C`（未选中时）   |
| 向上/下移动行 | `Alt + ↑ / ↓`            |
| 复制行        | `Shift + Alt + ↑ / ↓`    |
| 删除行        | `Ctrl + Shift + K`       |
| 注释行        | `Ctrl + /`               |
| 块注释        | `Shift + Alt + A`        |

### 4.3 多光标与选择

| 功能                 | 快捷键                     |
| -------------------- | -------------------------- |
| 在下一个相同单词处加光标 | `Ctrl + D`                 |
| 选中所有相同单词     | `Ctrl + Shift + L`         |
| 列（块）选择         | `Shift + Alt + 鼠标拖动`   |
| 添加光标到上/下一行   | `Ctrl + Alt + ↑ / ↓`       |
| 扩展 / 收缩选择      | `Shift + Alt + → / ←`      |

### 4.4 导航

| 功能              | 快捷键             |
| ----------------- | ------------------ |
| 跳转到定义        | `F12`              |
| 查看定义          | `Alt + F12`        |
| 返回上一个位置    | `Alt + ←`          |
| 转到指定行        | `Ctrl + G`         |
| 转到符号          | `Ctrl + Shift + O` |
| 在工作区查找符号  | `Ctrl + T`         |

### 4.5 搜索与替换

| 功能          | 快捷键             |
| ------------- | ------------------ |
| 当前文件查找  | `Ctrl + F`         |
| 当前文件替换  | `Ctrl + H`         |
| 全局查找      | `Ctrl + Shift + F` |
| 全局替换      | `Ctrl + Shift + H` |

---

## 5. 文件与工作区管理

### 5.1 打开文件夹

- 菜单：`File > Open Folder`。
- 快捷键：`Ctrl + K` 接 `Ctrl + O`。
- 命令行：`code /path/to/project`。

### 5.2 多根工作区（Multi-root Workspace）

可将多个文件夹加入同一工作区：`File > Add Folder to Workspace`，然后保存为 `.code-workspace` 文件。

示例 `project.code-workspace`：

```json
{
  "folders": [
    { "path": "frontend" },
    { "path": "backend" }
  ],
  "settings": {
    "editor.tabSize": 2
  }
}
```

### 5.3 文件资源管理器

- `Ctrl + Shift + E` 打开资源管理器。
- 右键文件可执行复制路径、在终端中打开、比较等操作。
- 点击文件时默认为"预览模式"（文件名斜体），双击或编辑后变为常驻 Tab。

---

## 6. 编辑技巧

### 6.1 IntelliSense（智能补全）

- 自动弹出补全；也可手动触发：`Ctrl + Space`。
- 参数提示：`Ctrl + Shift + Space`。
- 悬停查看定义：鼠标悬停或 `Ctrl + K Ctrl + I`。

### 6.2 代码格式化

| 功能            | 快捷键                  |
| --------------- | ----------------------- |
| 格式化文档      | `Shift + Alt + F`       |
| 格式化选中代码  | `Ctrl + K` `Ctrl + F`   |
| 保存时自动格式化 | 设置 `editor.formatOnSave: true` |

### 6.3 重构

- `F2`：重命名符号。
- `Ctrl + .`：快速修复 / 代码操作（Quick Fix）。

### 6.4 代码折叠

- 折叠 / 展开：`Ctrl + Shift + [` / `Ctrl + Shift + ]`
- 全部折叠：`Ctrl + K Ctrl + 0`
- 全部展开：`Ctrl + K Ctrl + J`

### 6.5 Emmet

在 HTML/CSS 中输入缩写后按 `Tab` 可展开，例如：

```
ul>li.item$*3
```

展开为：

```html
<ul>
  <li class="item1"></li>
  <li class="item2"></li>
  <li class="item3"></li>
</ul>
```

---

## 7. 终端与任务

### 7.1 集成终端

- 打开：`` Ctrl + ` ``
- 新建：`Ctrl + Shift + ` `
- 分屏：点击终端右上角分屏按钮或 `Ctrl + \`
- 切换 Shell：点击下拉菜单选择 PowerShell / Bash / zsh 等。

### 7.2 任务（Tasks）

在 `.vscode/tasks.json` 中可定义自动化任务，例如构建、测试：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "npm: build",
      "type": "shell",
      "command": "npm run build",
      "group": { "kind": "build", "isDefault": true },
      "problemMatcher": []
    }
  ]
}
```

运行任务：`Ctrl + Shift + B`（默认构建任务）或命令面板 `Tasks: Run Task`。

---

## 8. 插件（Extensions）

### 8.1 管理插件

- 打开插件视图：`Ctrl + Shift + X`。
- 搜索、安装、禁用、卸载。
- 使用 `@installed`、`@recommended`、`@category:"linters"` 等过滤器。

### 8.2 常用推荐插件

**通用**

- Chinese (Simplified) Language Pack — 中文界面
- GitLens — 增强 Git 功能
- Error Lens — 行内显示错误
- Path Intellisense — 路径补全
- Code Spell Checker — 拼写检查
- TODO Tree — TODO 注释聚合
- Better Comments — 彩色注释

**前端**

- ESLint / Prettier — 代码检查与格式化
- Tailwind CSS IntelliSense
- Vue / Vetur / Volar — Vue 支持
- ES7+ React/Redux/React-Native snippets

**后端 / 语言**

- Python（Microsoft 官方）
- Pylance
- C/C++
- Go
- Java Extension Pack
- Rust-analyzer

**DevOps / 其他**

- Docker
- Remote - SSH / WSL / Dev Containers
- REST Client — 在编辑器内发送 HTTP 请求
- Live Server — 启动静态网页服务器

### 8.3 通过命令行安装

```bash
code --install-extension dbaeumer.vscode-eslint
code --install-extension esbenp.prettier-vscode
```

---

## 9. 调试（Debug）

### 9.1 启动调试

- 打开调试视图：`Ctrl + Shift + D`。
- 点击"创建 launch.json 文件"，选择对应的环境（Node.js、Python、Chrome 等）。
- 设置断点：单击行号左侧。
- 启动：`F5`。

### 9.2 `launch.json` 示例（Node.js）

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "启动程序",
      "skipFiles": ["<node_internals>/**"],
      "program": "${workspaceFolder}/index.js"
    }
  ]
}
```

### 9.3 调试快捷键

| 功能      | 快捷键          |
| --------- | --------------- |
| 开始/继续 | `F5`            |
| 停止      | `Shift + F5`    |
| 单步跳过  | `F10`           |
| 单步进入  | `F11`           |
| 单步跳出  | `Shift + F11`   |
| 切换断点  | `F9`            |

---

## 10. Git 与版本控制

### 10.1 内置 Git 视图

- 打开源代码管理：`Ctrl + Shift + G`。
- 查看修改、暂存文件、填写提交信息、提交。
- 支持拉取、推送、分支切换、合并等操作。

### 10.2 常用操作

- 比较文件差异：点击已修改文件即可。
- 查看历史：使用 GitLens 插件可查看行级 blame 与提交历史。
- 处理冲突：VS Code 会在冲突文件中显示"Accept Current / Incoming / Both"按钮。

### 10.3 分支工作流建议

```bash
# 创建并切换到新分支
git checkout -b feature/my-feature
# 开发后提交
git add .
git commit -m "feat: 添加新功能"
# 推送
git push -u origin feature/my-feature
```

---

## 11. 远程开发

安装 **Remote Development** 扩展包（`ms-vscode-remote.vscode-remote-extensionpack`）后可获得：

- **Remote - SSH**：通过 SSH 连接远程服务器开发。
- **Dev Containers**：在 Docker 容器中开发。
- **WSL**：在 Windows Subsystem for Linux 中开发。

### 11.1 Remote - SSH 使用

1. `Ctrl + Shift + P` → `Remote-SSH: Connect to Host`。
2. 添加 SSH 主机（支持 `~/.ssh/config`）。
3. 连接后，VS Code 会在远程主机安装 VS Code Server，之后所有编辑、终端、调试都运行在远程。

SSH 配置示例（`~/.ssh/config`）：

```
Host myserver
    HostName 192.168.1.10
    User ubuntu
    IdentityFile ~/.ssh/id_rsa
```

### 11.2 Dev Containers

在项目中添加 `.devcontainer/devcontainer.json`，即可一键在容器中打开：

```json
{
  "name": "Node 20",
  "image": "mcr.microsoft.com/devcontainers/javascript-node:20",
  "postCreateCommand": "npm install",
  "customizations": {
    "vscode": {
      "extensions": ["dbaeumer.vscode-eslint"]
    }
  }
}
```

---

## 12. 用户设置与主题

### 12.1 设置界面

- `Ctrl + ,` 打开设置。
- 左上可切换 **用户 / 工作区 / 文件夹** 范围。
- 右上角 `{}` 图标可直接编辑 JSON。

### 12.2 常用设置

```json
{
  "editor.fontSize": 14,
  "editor.fontFamily": "JetBrains Mono, Consolas, monospace",
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "editor.minimap.enabled": false,
  "editor.wordWrap": "on",
  "files.autoSave": "onFocusChange",
  "files.trimTrailingWhitespace": true,
  "terminal.integrated.fontSize": 13,
  "workbench.colorTheme": "Default Dark Modern",
  "workbench.iconTheme": "material-icon-theme",
  "git.autofetch": true
}
```

### 12.3 设置同步（Settings Sync）

登录 GitHub 或 Microsoft 账号，通过 `Ctrl + Shift + P` → `Settings Sync: Turn On`，即可在多台设备间同步设置、快捷键、插件、代码片段等。

---

## 13. 代码片段（Snippets）

### 13.1 创建用户片段

`Ctrl + Shift + P` → `Snippets: Configure User Snippets` → 选择语言（如 `javascript.json`）。

示例：

```json
{
  "Console log": {
    "prefix": "clg",
    "body": ["console.log('$1', $1);"],
    "description": "快捷 console.log"
  }
}
```

输入 `clg` 后按 `Tab` 即可展开。

### 13.2 片段语法

- `$1`、`$2`：按 Tab 跳转的占位符。
- `${1:default}`：带默认值的占位符。
- `$0`：最终光标位置。
- `$TM_FILENAME`、`$CURRENT_YEAR` 等内置变量。

---

## 14. 常见问题（FAQ）

**Q1：VS Code 与 Visual Studio 有什么区别？**
A：Visual Studio 是重型 IDE，主要用于 .NET、C++ 的 Windows 开发；VS Code 是轻量编辑器，跨平台并通过插件支持多语言。

**Q2：如何解决中文乱码？**
A：点击状态栏右下的编码（如 UTF-8）→ `Reopen with Encoding` → 选择正确编码（常见 `GB2312` / `GBK`）。

**Q3：启动很慢怎么办？**
A：

- 使用 `Developer: Startup Performance` 命令分析。
- 禁用不常用插件（`--disable-extensions` 启动）。
- 关闭大文件的语义高亮：`"editor.semanticHighlighting.enabled": false`。

**Q4：如何恢复默认设置？**
A：打开设置 JSON，删除自定义项；或命令面板搜索 `Preferences: Reset Settings`。

**Q5：如何重置快捷键？**
A：`Ctrl + K Ctrl + S` 打开键盘快捷方式 → 右键某一项 → `Reset Keybinding`。

**Q6：如何让 VS Code 支持某种新语言？**
A：在扩展市场搜索对应语言插件（如 `Rust`、`Go`、`Kotlin`），安装后重启即可。

---

## 15. 参考资源

- 官方文档：<https://code.visualstudio.com/docs>
- 快捷键参考（PDF）：<https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf>
- 扩展市场：<https://marketplace.visualstudio.com/vscode>
- GitHub 仓库：<https://github.com/microsoft/vscode>
- 官方博客：<https://code.visualstudio.com/blogs>

---

> 本指南会持续更新。如果你有补充或建议，欢迎提交 PR 或 Issue。
