# A new version of md-to-html.py, which converts Markdown content
# into more types of elements with a necessarily complex structure.

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


def clear_markdown(markdown: str):
    return markdown.strip().replace(
        '’', "'").replace('“', '"').replace('”', '"')


class Tokenizer:
    def __init__(self, string):
        self.string = string
        self.tokens = []

        self._current_index = 0

    def _is_next_character(self, character):
        return (not self._current_index + 1 >= len(self.string)) and self.string[self._current_index + 1] == character

    def tokenize(self):
        while self._current_index < len(self.string):
            current_character = self.string[self._current_index]
            current_element = Element('', '')

            if current_character == '#':
                # TODO ...
                pass
