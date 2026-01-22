### 1. 核心同步指令

每当你在 Obsidian 里写完新笔记、修改了内容或添加了图片，在黑色窗口（Terminal）运行这一行即可：
```
npx quartz sync
```
**注意**：如果遇到 `Connection was reset` 等网络报错，请尝试切换手机热点，或者直接使用 Git 原生指令强制推送： `git add .` -> `git commit -m "update"` -> `git push origin v4 --force`。
### 2. 部署“通电”说明书 (`deploy.yml`)

如果以后 GitHub Actions 报错（红叉）或者不自动更新，请检查 `.github/workflows/deploy.yml` 文件内容是否完整：
```
name: Deploy Quartz
on:
  push:
    branches:
      - v4  # 确保分支名是 v4
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - name: Install Dependencies
        run: npm install # 使用 install 比 ci 更兼容
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
```
### 3. 图片显示避坑指南

- **存放位置**：所有图片必须放在 `content` 文件夹内（建议新建 `Z--截图库` 文件夹）。
    
- **本地化**：笔记中的图片链接如果是 `https://secure2.wostatic.cn/...` 这种带密钥的网络图，建议使用 `Local Images Plus` 插件转成本地格式 `![[图片名.png]]`，否则网页端会因密钥过期而不显示。
    
- **激活文件夹**：如果某个文件夹里只有图片没有笔记，请在里面建一个空的 `README.md`，这样 Quartz 才会识别并显示该文件夹。
    

---

### 4. 常见报错自查

- **Nothing to commit**：说明本地文件没变。如果线上报错但本地传不上去，在 `deploy.yml` 开头加一行注释（如 `# v2`）即可强制更新。
    
- **No event triggers**：`deploy.yml` 的格式（空格缩进）错了，直接从本笔记复制覆盖即可。
    
- **Status 128 / Identity unknown**：运行以下指令重新告诉 Git 你是谁： `git config --global user.email "你的邮箱"` `git config --global user.name "你的名字"`