# This code converts Markdown content into HTML code and adds the result into the
# 'blogs' directory. It can currently create headings (h1-h6), paragraphs (p),
# ordered and unordered lists (ol, ul, li) within a formatted HTML template.

from datetime import datetime

class Element:
    def __init__(self, element_name: str, content):
        self.element_name = element_name
        self.content = content

    def __repr__(self):
        return f'{self.element_name}: "{self.content}"'

    def to_html_code(self):
        html_code = f'<{self.element_name}>'

        if self.element_name == 'ol' or self.element_name == 'ul':
            for list_item in self.content:
                html_code += list_item.to_html_code()
        else:
            html_code += self.content

        html_code += f'</{self.element_name}>'

        return html_code


class Tokenizer:
    def __init__(self, string):
        self.string = string
        self.tokens = []

        self._string_by_lines = self.string.split('\n')
        self._current_line_index = 0
        self._current_char_index = 0


    # This method checks if there is a next character and if so,
    # checks if it equals to the passed `character`.
    def _is_next_character(self, character):
        current_line = self._string_by_lines[self._current_line_index]

        return (
            not self._current_char_index + 1 >= len(current_line)
        ) and current_line[self._current_char_index + 1] == character

    def tokenize(self):
        for index, line in enumerate(self._string_by_lines):
            self._current_line_index = index
            self._current_char_index = 0

            line_stripped = line.strip()

            if line_stripped == '':
                continue

            line_first_character = line_stripped[0]
            line_is_a_paragraph = True

            if line_first_character == '#':
                while self._is_next_character('#'):
                    self._current_char_index += 1

                if self._is_next_character(' '):
                    line_is_a_paragraph = False
                    self.tokens.append(
                        Element('h' + str(self._current_char_index + 1), line_stripped[self._current_char_index + 2:]))
            elif (line_first_character == '*' or line_first_character == '-') and self._is_next_character(' '):
                last_token = self.tokens[-1]
                list_item_content = line_stripped[2:]

                if list_item_content != '':
                    line_is_a_paragraph = False

                    if last_token.element_name == 'ul':
                        last_token.content.append(
                            Element('li', list_item_content))
                    else:
                        self.tokens.append(
                            Element('ul', [Element('li', list_item_content)]))
            elif line_first_character.isnumeric() and self._is_next_character('.'):
                last_token = self.tokens[-1]
                list_item_content = line_stripped[3:]

                if list_item_content != '':
                    line_is_a_paragraph = False

                    if last_token.element_name == 'ol' and int(line_first_character) == len(last_token.content) + 1:
                        last_token.content.append(
                            Element('li', list_item_content))
                    elif int(line_first_character) == 1:
                        self.tokens.append(
                            Element('ol', [Element('li', list_item_content)]))
                    else:
                        line_is_a_paragraph = True

            if line_is_a_paragraph:
                self.tokens.append(Element('p', line_stripped))

        return self.tokens


def clear_markdown(markdown: str):
    return markdown.strip().replace(
        '’', "'").replace('“', '"').replace('”', '"')


blog_name = 'Example blog post name'
blog_file_name = blog_name.lower().replace(' ', '-')

description = ''
date_posted = datetime.now().strftime('%B %d, %Y')

with open(blog_file_name + '.md') as f:
    markdown_content = clear_markdown(f.read())

elements = Tokenizer(markdown_content).tokenize()
html_content = ''

for element in elements:
    html_content += element.to_html_code()

blog_html_template = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <meta name="description" content="{description}"/>
    <meta name="keywords" content="personal, coding, computer science, feminism, lgbtq+, queer, blogging, blogs, blog"/>
    <meta name="author" content="dancing jovial penguin"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{blog_name} | ♡ dancing jovial penguin's blogs ♡</title>

    <link rel="icon" type="image/png" href="../images/favicon-32.png" sizes="32x32"/>
    <link rel="icon" type="image/png" href="../images/favicon-48.png" sizes="48x48"/>

    <link rel="preconnect" href="https://fonts.googleapis.com"/>
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
    <link href="https://fonts.googleapis.com/css2?family=Ribeye+Marrow&family=Source+Code+Pro:ital,wght@0,200..900;1,200..900&display=swap" rel="stylesheet"/>

    <link rel="stylesheet" href="../styles/style.css"/>
    <link rel="stylesheet" href="../styles/blog-style.css"/>
  </head>

  <body>
    <p>Posted on {date_posted}.</p>
    {html_content}
    <script src="../scripts/blogs.js"></script>
  </body>
</html>
"""

with open('blogs/' + blog_file_name + '.html', 'a') as f:
    f.write(blog_html_template)
