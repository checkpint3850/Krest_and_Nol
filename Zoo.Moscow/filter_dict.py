import random


async def filer_dict_def(answer, dict_, category):
    for key, value in list(dict_.items()):
        try:
            if value[category] == answer:
                None
            else:
                dict_.pop(key)
        except KeyError as e:
            if answer is True:
                dict_.pop(key)


async def filter_final(dict_all):
    new_ = []
    for key_, value_ in list(dict_all.items()):
        new_.append(value_.get('name'))
    random_animals = random.sample(new_, k=1)
    return random_animals
