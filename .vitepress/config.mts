import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Python 入门学习",
  description: "Python 入门教程",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Python 笔记', link: '/python_learning' }
    ],

    sidebar: [
      {
        text: '第一章',
        items: [
          { text: '第1章', link: '第1章/说明.txt' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
