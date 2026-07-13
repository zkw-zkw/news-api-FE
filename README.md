# 新闻资讯前端

> 基于 Vue 3 + Vant 的新闻资讯移动端前端，支持 AI Agent 智能问答。

🎯 在线演示：[http://118.195.129.25/](http://118.195.129.25/)

---

## 技术栈

| 类别 | 技术 |
|------|------|
| 框架 | Vue |
| 构建工具 | Vite |
| UI 组件库 | Vant |
| 状态管理 | Pinia |
| 路由 | Vue Router |
| 国际化 | vue-i18n |
| Markdown | marked + DOMPurify |

---

## 核心功能

- 🤖 **AI Agent 智能问答** — 自然语言搜索新闻、热度排行
- 新闻分类浏览（头条、社会、国内、国际等 9 个分类）
- 新闻列表（列表/网格两种排版切换）
- 新闻详情（浏览实时统计、相关推荐）
- 新闻搜索（全局关键词搜索）
- 用户登录/注册
- 新闻收藏 / 浏览历史
- 多语言支持（中文 / English）

---

## 项目结构

```
news-api-FE/
├── index.html
├── vite.config.js
├── package.json
│
├── src/
│   ├── main.js                 # 入口
│   ├── App.vue                 # 根组件
│   ├── router/
│   │   └── index.js            # 路由配置
│   ├── store/                  # Pinia 状态
│   ├── i18n/                   # 国际化配置
│   └── views/
│       ├── Home.vue            # 首页（分类标签 + 新闻列表）
│       ├── NewsDetail.vue      # 新闻详情
│       ├── AIChat.vue          # AI Agent 对话页
│       ├── Search.vue          # 搜索页
│       ├── Login.vue / Register.vue
│       ├── My.vue              # 个人中心
│       ├── Favorite.vue        # 收藏
│       ├── History.vue         # 浏览历史
│       ├── Settings.vue        # 设置
│       └── Profile.vue         # 个人信息
```

---

## 快速启动

```bash
# 安装依赖
npm install

# 开发模式
npm run dev

# 生产构建
npm run build
```

底部 Tab：🏠 首页 · 🤖 AI Agent · 👤 我的

---

## License

MIT
