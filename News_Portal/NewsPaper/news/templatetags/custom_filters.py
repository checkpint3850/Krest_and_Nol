from django import template


register = template.Library()

bad_words = ['Нехорошие', 'слова', 'пример', 'люди', 'инопланетной']


@register.filter()
def censor(value):
    for w in bad_words:
        value = value.replace(w[1:], '*' * len(w[1:]))
    return value
