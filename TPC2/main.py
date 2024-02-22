import re

def markdown_to_html(markdown_text):
    # Heading
    markdown_text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdown_text, flags=re.M)
    markdown_text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', markdown_text, flags=re.M)
    markdown_text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', markdown_text, flags=re.M)

    # Espaçamento
    markdown_text = re.sub(r'(?m)^\s*$', '<br>', markdown_text)

    # Blockquote
    markdown_text = re.sub(r'^>\s(.*?)$', r'<blockquote>\1</blockquote>', markdown_text, flags=re.MULTILINE)

    # Bold
    markdown_text = re.sub(r'\*{2}(.*?)\*{2}', r'<b>\1</b>', markdown_text)

    # Italic
    markdown_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdown_text)

    # Unordered List
    markdown_text = re.sub(r'^- (.+)', r'<ul>\n<li>\1</li>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'</li>\n<ul>', r'</li>\n</ul>\n<ul>', markdown_text)
    markdown_text += '</ul>'

    # Ordered List
    markdown_text = re.sub(r'(\d+\.\s+.*\n?)+', r'<ol>\g<0></ol>', markdown_text)
    markdown_text = re.sub(r'\d+\.\s+(.*)', r'<li>\1</li>\n', markdown_text)

    # Code
    markdown_text = re.sub(r'`(.+?)`', r'<code>\1</code>', markdown_text)

    # Horizontal Rule
    markdown_text = re.sub(r'---', r'<hr>', markdown_text)

    # Image
    markdown_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown_text)

    # Link
    markdown_text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', markdown_text)

    return markdown_text

def convert_markdown_file_to_html(file_path, output_file_path):
    with open(file_path, 'r') as file:
        markdown_text = file.read()
        html_text = markdown_to_html(markdown_text)
        with open(output_file_path, 'w') as output_file:
            output_file.write(html_text)

if __name__ == "__main__":
    convert_markdown_file_to_html("teste.md", "teste.html")