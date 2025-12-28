import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "HJY's NOTES",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "quartz.jzhao.xyz",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
  colors: {
        lightMode: {
          light: "#fdfcf0",       // 背景：温暖的奶油白
          lightgray: "#e5e5e5",   // 搜索框边框等小组件
          gray: "#b8b8b8",        // 时间、字数等辅助文字
          darkgray: "#4e4e4e",    // 正文颜色
          dark: "#2b2b2b",        // 标题颜色
          secondary: "#a63d40",   // 链接和侧边栏选中的颜色（圣诞红）
          tertiary: "#4a5d23",    // 鼠标悬停时的链接颜色（森林绿）
          highlight: "rgba(166, 61, 64, 0.1)", // 选中背景色
          textHighlight: "#a63d40",            // 补上这一行：选中文字的颜色
        },
        darkMode: {
          light: "#1a1b1e",       // 背景：深灰近黑
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#e67e22",   // 暖橙色（烛光感）
          tertiary: "#f1c40f",    // 明黄色
          highlight: "rgba(230, 126, 34, 0.15)",
          textHighlight: "#e67e22",            // 补上这一行：选中文字的颜色
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
