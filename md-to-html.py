# This code converts Markdown (.md) code into formatted HTML code.
# Currently, it can only convert into h1, h2, p, and ol elements.

blog_name = 'radical-feminism-is-not-inherently-transphobic'

with open(f'{blog_name}.md') as f:
    markdown = f.read()


class ContentUnit:
    def __init__(self, type, content):
        self.type = type
        self.content = content

    def __repr__(self):
        return f'{self.type}: "{self.content}"'


html = ""
content = []
markdown_seperated_by_newlines = markdown.split('\n')

for index, paragraph in enumerate(markdown_seperated_by_newlines):
    trimmed_paragraph = paragraph.strip().replace(
        '’', "'").replace('“', '"').replace('”', '"')
    unit = ContentUnit('', '')

    if trimmed_paragraph == '':
        continue

    if trimmed_paragraph[0] == '#':
        if trimmed_paragraph[1] == "#":
            unit.type = 'H2'
            unit.content = trimmed_paragraph[3:]
        else:
            unit.type = 'H1'
            unit.content = trimmed_paragraph[2:]
    elif trimmed_paragraph[0].isnumeric() and trimmed_paragraph[1] == '.':
        unit.type = 'LIST_ITEM'
        unit.content = trimmed_paragraph[3:]

        if content[-1].type == 'LIST_NUMBERED':
            content[-1].content.append(unit)
            continue
        else:
            list_item_unit = ContentUnit(unit.type, unit.content)

            unit.type = 'LIST_NUMBERED'
            unit.content = [list_item_unit]  # type: ignore
    else:
        unit.type = 'PARAGRAPH'
        unit.content = trimmed_paragraph

    content.append(unit)

for unit in content:
    if unit.type == 'H1' or unit.type == 'H2':
        lowercase_unit_type = unit.type.lower()

        html += f'<{lowercase_unit_type}>'
        html += unit.content
        html += f'</{lowercase_unit_type}>\n'

    if unit.type == 'PARAGRAPH':
        html += '<p>'
        html += unit.content
        html += '</p>\n'

    if unit.type == 'LIST_NUMBERED':
        html += '<ol>\n'

        for list_item in unit.content:
            html += '  <li>'
            html += list_item.content
            html += '  </li>\n'

        html += '</ol>\n'

with open(f'{blog_name}.html', 'a') as f:
    f.write(html)
