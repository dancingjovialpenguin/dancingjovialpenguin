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

        self._current_element = Element('p', '')
        self._current_index = 0

    # This method checks if there is a next character and if so,
    # checks if it equals to the passed `character`.
    def _is_next_character(self, character):
        return (not self._current_index + 1 >= len(self.string)) and self.string[self._current_index + 1] == character

    def tokenize(self):
        while self._current_index < len(self.string):
            current_character = self.string[self._current_index]

            if current_character == '#':
                hash_count = 1

                while self._is_next_character('#'):
                    hash_count += 1
                    self._current_index += 1

                self._current_element.element_name = 'h' + str(hash_count)

                print(self._current_element)
            
            elif current_character.isnumeric() and self._is_next_character('.'):
                self._current_element.element_name = 'ol_li'
            elif (current_character == '*' or current_character == '-') and self._is_next_character(' '):
                self._current_element.element_name = 'ul_li'
            elif current_character == '\n':
                print(self._current_element)
                self.tokens.append(self._current_element)

                self._current_element.element_name = 'p'
                self._current_element.content = ''
            else:
                self._current_element.content += current_character

            self._current_index += 1

        return self.tokens
    
string = """
# test
"""

tokenizer = Tokenizer(string)
print(tokenizer.tokenize())
