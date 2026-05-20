#!/usr/bin/env python3
"""
英文单词闪卡生成器
根据两个英文单词生成一张上下布局的闪卡图片
"""

import sys
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_flashcard(word1_data: dict, word2_data: dict, output_path: str, style_ref_path: str = None):
    """
    创建闪卡图片
    
    Args:
        word1_data: 第一个单词的数据，包含 {
            'word': 英文单词,
            'translation': 中文翻译,
            'sentence': 英文例句,
            'sentence_translation': 例句中文翻译
        }
        word2_data: 第二个单词的数据，格式同上
        output_path: 输出图片路径
        style_ref_path: 风格参考图片路径（可选）
    """
    # 图片尺寸 3:4 比例
    width = 900
    height = 1200
    
    # 颜色配置（基于参考图片）
    bg_color = (255, 250, 235)  # 淡黄色背景
    border_color = (255, 140, 100)  # 橙红色边框
    text_color = (50, 50, 50)  # 深灰色文字
    accent_color = (255, 180, 160)  # 粉色强调色
    
    # 创建画布
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 绘制圆角边框
    border_width = 20
    corner_radius = 40
    
    # 外边框
    draw.rounded_rectangle(
        [(10, 10), (width-10, height-10)],
        radius=corner_radius,
        outline=border_color,
        width=border_width
    )
    
    # 中间分隔线
    mid_y = height // 2
    draw.line([(30, mid_y), (width-30, mid_y)], fill=border_color, width=8)
    
    # 尝试加载字体
    try:
        # 尝试使用系统字体
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        font_chinese = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 48)
        font_chinese_small = ImageFont.truetype("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 24)
    except:
        font_large = ImageFont.load_default()
        font_medium = font_large
        font_small = font_large
        font_chinese = font_large
        font_chinese_small = font_large
    
    def draw_word_section(word_data, y_start, y_end, is_top=True):
        """绘制单个单词区域"""
        section_height = y_end - y_start
        center_y = y_start + section_height // 2
        
        # 绘制装饰性圆形背景（模拟卡通角色的位置）
        circle_x = 200 if is_top else 700
        circle_y = y_start + 180
        draw.ellipse(
            [(circle_x-120, circle_y-120), (circle_x+120, circle_y+120)],
            fill=accent_color
        )
        
        # 绘制单词（右侧或左侧，根据上下交替）
        word_x = 480 if is_top else 150
        word = word_data['word'].upper()
        bbox = draw.textbbox((0, 0), word, font=font_large)
        word_width = bbox[2] - bbox[0]
        draw.text((word_x, y_start + 60), word, fill=text_color, font=font_large)
        
        # 绘制中文翻译
        translation = word_data['translation']
        draw.text((word_x, y_start + 150), translation, fill=text_color, font=font_chinese)
        
        # 绘制例句（换行处理）
        sentence = word_data['sentence']
        sentence_trans = word_data['sentence_translation']
        
        # 英文例句换行
        max_width = 500
        words = sentence.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + " " + word if current_line else word
            bbox = draw.textbbox((0, 0), test_line, font=font_small)
            if bbox[2] - bbox[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        
        # 绘制英文例句
        y_offset = y_start + 260
        for line in lines:
            draw.text((60 if is_top else 60, y_offset), line, fill=text_color, font=font_small)
            y_offset += 35
        
        # 绘制中文例句翻译
        y_offset += 10
        draw.text((60 if is_top else 60, y_offset), sentence_trans, fill=text_color, font=font_chinese_small)
    
    # 绘制上半部分（word1）
    draw_word_section(word1_data, 30, mid_y - 10, is_top=True)
    
    # 绘制下半部分（word2）
    draw_word_section(word2_data, mid_y + 10, height - 30, is_top=False)
    
    # 保存图片
    img.save(output_path, quality=95)
    return output_path


if __name__ == "__main__":
    # 示例用法
    if len(sys.argv) < 3:
        print("用法: python generate_flashcard.py <单词1> <单词2> [输出路径]")
        sys.exit(1)
    
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) > 3 else "flashcard_output.png"
    
    # 这里应该调用AI生成例句和翻译
    # 为演示使用简单数据
    word1_data = {
        'word': word1,
        'translation': '单词1翻译',
        'sentence': f'I like to {word1} every day.',
        'sentence_translation': f'我喜欢每天{word1}。'
    }
    word2_data = {
        'word': word2,
        'translation': '单词2翻译',
        'sentence': f'We {word2} together.',
        'sentence_translation': f'我们一起{word2}。'
    }
    
    create_flashcard(word1_data, word2_data, output)
    print(f"闪卡已生成: {output}")
