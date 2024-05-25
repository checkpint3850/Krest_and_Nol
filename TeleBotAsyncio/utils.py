async def random_meal(session, comands):
    async with session.get(
            url=f'https://www.themealdb.com/api/json/v1/1/list.php?c=list',
    ) as resp:
        data = await resp.json()
        data_meals = data.get('meals')
        value_meals = []
        for i in data_meals:
            value_meals.append(i.get('strCategory'))
    return value_meals
