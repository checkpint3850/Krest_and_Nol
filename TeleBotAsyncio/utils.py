

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


async def choose_by_category(session, meal):
    async with session.get(
            url=f'www.themealdb.com/api/json/v1/1/filter.php?c={meal}',
    ) as resp:
        data = await resp.json()
        data_meals = data.get('meals')
        value_meals = []
        for i in data_meals:
            name_meal = i.get('strMeal')
            id_meal = i.get('idMeal')
            value_meals.append({name_meal: id_meal})
    return value_meals

