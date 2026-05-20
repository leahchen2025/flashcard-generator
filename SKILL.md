---
name: flashcard-generator
description: 英文单词闪卡生成器。根据用户提供的两个英文单词，生成一张3:4比例的可爱风格闪卡图片。使用场景包括：(1) 儿童英语启蒙学习，(2) 制作教学用单词卡片，(3) 记忆单词的图文卡片。当用户请求"生成闪卡"、"制作单词卡片"、"创建英文单词卡"或类似需求时触发此技能。
---

# Flashcard Generator - 英文单词闪卡生成器

## 概述

根据用户提供的两个英文单词，生成一张包含中英文、例句和插图的可爱风格闪卡图片。

## 工作流程

### 1. 解析用户输入
- 识别用户提供的两个英文单词
- 确认图片比例要求（默认 3:4）

### 2. 生成单词内容
对于每个单词，需要生成：
- **英文单词**：用户提供的小写形式（**必须用小写字母**，如 sleep, eat）
- **中文翻译**：准确的中文释义
- **英文例句**：简单、常用的英文句子，包含该单词
- **例句中文翻译**：对应的中文翻译

### 3. 生成闪卡图片

使用 `generate_image` 工具生成闪卡图片，要求：

**整体布局**：
- 图片比例：3:4（宽:高）
- 上下两部分，中间有橙红色分隔线
- 整体采用可爱卡通风格，适合儿童学习

**风格参考图片**（本仓库 `assets/style_reference.png`）：

**参考图片风格特征**：
- **背景**：淡黄色/奶油色背景
- **边框**：橙红色圆角边框
- **角色**：可爱的粉色云朵状卡通角色，脸颊有腮红，表情可爱
- **分隔**：上下两部分之间有橙红色横线分隔

**上半部分（第一个单词）**：
- **左侧**：卡通角色插图（体现单词含义）
- **右侧**：英文单词（**小写**、大号粗体黑色）、中文翻译（大号黑色）
- **下方**：英文例句 + 中文翻译

**下半部分（第二个单词）**：
- **左侧**：英文单词（**小写**、大号粗体黑色）、中文翻译（大号黑色）
- **右侧**：卡通角色插图（体现单词含义）
- **下方**：英文例句 + 中文翻译
- （注意：上下两部分布局左右镜像，与参考图片一致）

**文字要求**：
- 英文单词：**小写字母**、大号、粗体、黑色
- 中文翻译：大号、黑色
- 英文例句：中等字号、黑色
- 例句翻译：中等字号、黑色

### 4. 图片生成提示词模板

```
A cute educational English flashcard in vertical 3:4 ratio. 
Light cream/yellow background with coral orange rounded border and rounded corners.
A horizontal coral orange dividing line separates the top and bottom halves.

Top half (Word: [word1] in lowercase):
- Left side: Cute kawaii-style pink fluffy cloud-shaped cartoon character with blush on cheeks, [doing action related to word1], simple clean illustration style like the reference
- Right side: Large bold black lowercase text "[word1]" with Chinese translation "[中文]" below it in large black text
- Bottom area: English sentence "[sentence]" with Chinese translation "[句子翻译]"

Bottom half (Word: [word2] in lowercase):
- Left side: Large bold black lowercase text "[word2]" with Chinese translation "[中文]" below it in large black text  
- Right side: Cute kawaii-style pink fluffy cloud-shaped cartoon character with blush on cheeks, [doing action related to word2], simple clean illustration style like the reference
- Bottom area: English sentence "[sentence]" with Chinese translation "[句子翻译]"

Style: EXACTLY match the reference image style - soft pink cartoon characters with cloud-like fluffy appearance, warm cream background, coral orange accents, simple and cute educational card design, child-friendly, rounded corners everywhere.
The cartoon characters should look like fluffy pink clouds with cute faces, blush marks on cheeks, minimal details, very kawaii style.
Text layout must match reference: top half has image left + text right, bottom half has text left + image right.
```

### 5. 使用参考图片生成

在调用 `generate_image` 时，**必须**添加 `references` 参数引用风格图片：

```json
{
  "references": [
    "assets/style_reference.png"
  ]
}
```

> **注意**：安装此技能后，请将 `references` 路径调整为本地实际路径。

## 示例

**用户输入**：`dance` 和 `sing`

**生成内容**：
- Word 1: dance / 跳舞 / I like to dance. / 我喜欢跳舞。
- Word 2: sing / 唱歌 / She can sing well. / 她唱歌很好听。

**输出**：一张3:4比例的闪卡图片，严格按照参考图片风格：
- 上半部分左侧：跳舞的粉色卡通角色，右侧：dance 跳舞
- 下半部分左侧：sing 唱歌，右侧：唱歌的粉色卡通角色

## 参考图片

本仓库 `assets/style_reference.png`，或在线查看：
```
https://raw.githubusercontent.com/leahchen2025/flashcard-generator/main/assets/style_reference.png
```

## 注意事项

1. **英文单词必须用小写字母**，如 "sleep" 而非 "SLEEP"
2. **必须**在 `generate_image` 中使用 `references` 参数引用参考图片 URL
3. 图片布局必须严格遵循参考图片：上半部分左图右词，下半部分左词右图
4. 卡通角色必须是粉色、云朵状、有腮红的可爱风格
5. 确保例句简单易懂，适合英语学习者
6. 整体风格保持可爱、温馨，适合儿童使用
7. 背景使用淡黄色/奶油色，边框使用橙红色
