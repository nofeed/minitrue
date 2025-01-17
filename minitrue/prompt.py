import prompt_toolkit
from prompt_toolkit.validation import Validator, ValidationError


def ask(question):
    answer = prompt_toolkit.prompt(f'{question} ~ ')
    return answer


def yes_no(question):
    validator = Validator.from_callable(
        is_yes_no, error_message='Input should be (y/yes/n/no)')
    answer = prompt_toolkit.prompt(
        f'{question} (y/n) ~ ',
        validator=validator,
        validate_while_typing=False)
    if answer in {'yes', 'y'}:
        return True
    else:
        return False


def is_yes_no(text):
    if text in {'yes', 'no', 'y', 'n'}:
        return text


def say(phrase):
    prompt_toolkit.print_formatted_text(phrase)
