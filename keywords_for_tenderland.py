import pandas as pd    # by Kirill Kasparov, 2023

# Программа берет выгрузку конкурсов из Тендерленда и генерирует связки ключевых слов.
print('-' * 50)
print('О программе: Программа берет выгрузку конкурсов из Тендерленда и генерирует ключевые слова.')
print('На вход используется:')
print('1. файл import.csv с обязательным наличием колонок "Снимаем" и "Название".')
print('   "Снимаем" - проставляется вручную, где "1" - конкурсы, которые надо снять, а "2" - надо исключить.')
print('   "Название" - это название конкурса из выгрузки Тендерленда.')
print('2. файл ignore_list.csv с обязательным наличием колонки "Игнорировать".')
print('На выход:')
print('3. файл export.csv с комбинацией ключевых слов.')
print('-' * 50)


def cloud(list, data_ignore):
    dict1 = {}
    for text in list:
        text = text.lower().split()
        for word in text:
            word = ending(word.strip('«».,!?:-_\|/"@#$%^&*();-'), ending1, ending2, ending3)
            if word.isdigit():
                continue
            if len(word) < 4:
                continue
            if word not in exception and word not in data_ignore['Игнорировать'].to_list():
                dict1[word] = dict1.setdefault(word, 0) + 1
    return dict1
def cloud_kw(list, data_ignore, kw):
    dict1 = {}
    for text in list:
        text = text.lower().split()
        for word in text:
            word = ending(word.strip('«».,!?:-_\|/"@#$%^&*();-'), ending1, ending2, ending3)
            if word.isdigit():
                continue
            if len(word) < 4:
                continue
            if str(word) == str(kw):
                continue
            if word not in exception and word not in data_ignore['Игнорировать'].to_list():
                dict1[word] = dict1.setdefault(word, 0) + 1
    return dict1
def ending(kw, ending1, ending2, ending3):
    kw = str(kw)
    if len(kw) > 4 and kw[-3:] in ending3:
        kw = kw[:-3]
    elif len(kw) > 4 and kw[-2:] in ending2:
        kw = kw[:-2]
    elif len(kw) > 4 and kw[-1:] in ending1:
        kw = kw[:-1]
    return kw


# Собираем базы
data_import = pd.read_csv('import.csv', sep=';', encoding='windows-1251', dtype='unicode')
data_import['Снимаем'] = data_import['Снимаем'].fillna('2')
data_import['Снимаем'] = data_import['Снимаем'].astype('str')

data_for_acces = data_import[data_import['Снимаем'] == '1']    # Снять с площадки
data_for_trash = data_import[data_import['Снимаем'] == '0']    # Не снимать

# список исключений
exception = ('даром', 'как-то', 'поэтому', 'так', 'да', 'оттого', 'уже', 'едва', 'тех', 'пока', 'покуда', 'исключительно', 'затем', 'подлинно', 'о', 'ли', 'что', 'результате', 'тоже', 'чего', 'всем', 'нежели', 'не', 'значит', 'условии', 'с', 'по', 'вряд', 'скоро', 'сквозь', 'отчего', 'том', 'или', 'вон', 'однако', 'пусть', 'независимо', 'потому', 'без', 'прежде', 'притом', 'кроме', 'до', 'это', 'ни', 'тем', 'из-за', 'чем', 'зачем', 'еще', 'причине', 'вопреки', 'случае', 'особенно', 'хотя', 'поскольку', 'будто', 'даже', 'есть', 'разве', 'коли', 'от', 'пускай', 'из', 'ввиду', 'через', 'только', 'мере', 'тому', 'перед', 'при', 'связи', 'раз',
             'ежели', 'следовательно', 'несмотря', 'словно', 'именно', 'чтобы', 'вот', 'близ', 'причем', 'благо', 'вследствие', 'дабы', 'то', 'после', 'у', 'под', 'лишь', 'когда', 'сочинительный', 'буде', 'чтоб', 'вроде', 'ровно', 'для', 'и', 'либо', 'подобно', 'точно', 'чуть', 'вдобавок', 'над', 'почему', 'также', 'среди', 'в', 'как', 'же', 'ну', 'бы', 'неужели', 'раньше', 'более', 'если', 'ибо', 'на', 'к', 'невзирая', 'благодаря', 'вне', 'ради', 'силу', 'а', 'если…,', 'покамест', 'из-под', 'все-таки', 'Как', 'подчинительный', 'за', 'все', 'прямо', 'просто', 'то-то', 'ведь', 'тогда', 'но', 'всего', 'хоть', 'кабы', 'того', 'зато', 'про', 'между')
ending3 = ('ать', 'оть', 'уть', 'ешь', 'ете', 'ишь', 'ите', 'ала', 'али', 'ола', 'оли', 'ула', 'ули', 'ами', 'еми', 'емя', 'ёте', 'ёшь', 'ими', 'ого', 'ому', 'умя', 'ять', 'еть', 'яла', 'яли', 'ела', 'ели')
ending2 = ('ых', 'ют', 'ее', 'яя', 'ие', 'ая', 'ое', 'ой', 'ые', 'ый', 'ем', 'ет', 'им', 'ит', 'ут', 'ал', 'ол', 'ул', 'ам', 'ас', 'ax', 'её', 'ей', 'ex', 'ею', 'ёт', 'ёх', 'ие', 'ий', 'их', 'ию', 'ми', 'мя', 'ов', 'оё', 'ом', 'ою', 'ум', 'ух', 'ую', 'шь', 'ял', 'ел')
ending1 = ('и', 'а', 'о', 'ь', 'ы', 'у', 'е', 'и', 'м', 'я', 'ю')

data_ignore = pd.read_csv('ignore_list.csv', sep=';', encoding='windows-1251', dtype='unicode')

# Перебираем ключи
list_acces = data_for_acces['Название'].str.lower()
list_trash = data_for_trash['Название'].str.lower()

print('Собираем ключевые слова')

# мудреное преобразование словаря в df через функцию и обработку словаря в списки 2 уровня
df_acces = pd.DataFrame(list(cloud(list_acces, data_ignore).items()), columns=['keywords', 'acces']).sort_values(by='acces', ascending=False)
df_trash = pd.DataFrame(list(cloud(list_trash, data_ignore).items()), columns=['keywords', 'trash']).sort_values(by='trash', ascending=False)

# Слепляем все Датафреймы в один
export_df = df_acces.merge(df_trash, how='outer', on='keywords')


# Добавляем неотсортированные значения
if sum(data_import['Снимаем'] == '2') > 0:
    data_for_sort = data_import[data_import['Снимаем'] == '2']  # Не отсортированный остатой
    list_sort = data_for_sort['Название'].str.lower()
    df_sort = pd.DataFrame(list(cloud(list_sort, data_ignore).items()), columns=['keywords', 'sort']).sort_values(by='sort', ascending=False)
    export_df = export_df.merge(df_sort, how='outer', on='keywords')
    export_df['sort'] = export_df['sort'].fillna(0)
    export_df['sort'] = export_df['sort'].astype('int64')

export_df['acces'] = export_df['acces'].fillna(0)
export_df['acces'] = export_df['acces'].astype('int64')
export_df['trash'] = export_df['trash'].fillna(0)
export_df['trash'] = export_df['trash'].astype('int64')

# Добавляем связанные ключевые слова
keywords = export_df['keywords']

# acces
print('Ищем связки слов для acces')
kw_acces = []
kw_for_tenderland = []
kw_acces_lots = []

for word in keywords:
    mask = list_acces.str.contains(word.strip(), regex=False)
    temp_df = pd.DataFrame(list_acces[mask], columns=['Название']) # список для подсчета кол-ва конкурсовб
    mask2 = temp_df['Название'] == '-=-'  # заглушка False чтобы посчитать количество

    dict_kw = pd.DataFrame(list(cloud_kw(list_acces[mask], data_ignore, word).items()), columns=['keywords', 'sort']).sort_values(by='sort', ascending=False)    # собираем словарь в формате keyword: count
    lst_kw = []    # сюда собираем дополнительные keywords
    lst_kw_for_tenderland = word + '+('    # сюда собираем группу ключей, собранных под формат Тендерленда

    lst1 = dict_kw['keywords'].head().to_list()    # head нужен, чтобы взять только ТОП 5 ключей
    lst2 = dict_kw['sort'].head().to_list()    # head нужен, чтобы взять только ТОП 5 ключей
    for i in range(len(lst1)):
        lst_kw.append(lst1[i] + ' - ' + str(lst2[i]))    # перебор для поля 'kw_acces'
        lst_kw_for_tenderland = lst_kw_for_tenderland + lst1[i] + '/'    # перебор для поля 'kw_acces_tl'
        mask2 += temp_df['Название'].str.contains(lst1[i].strip(), regex=False)  # перебор для общего количества лотов по ключам
    lst_kw_for_tenderland = lst_kw_for_tenderland[:-1] + ')'
    lst_kw_for_tenderland = "".join(lst_kw_for_tenderland)
    kw_for_tenderland.append(lst_kw_for_tenderland)
    lst_kw = "; ".join(lst_kw)
    kw_acces.append(lst_kw)
    kw_acces_lots.append(sum(mask2))
export_df['kw_acces'] = kw_acces
export_df['kw_acces_tl'] = kw_for_tenderland
export_df['kw_acces_lots'] = kw_acces_lots

# trash
print('Ищем связки слов для trash')
kw_trash = []
kw_for_tenderland = []
kw_trash_lots = []
for word in keywords:
    mask = list_trash.str.contains(word.strip(), regex=False)
    temp_df = pd.DataFrame(list_trash[mask], columns=['Название']) # список для подсчета кол-ва конкурсовб
    mask2 = temp_df['Название'] == '-=-'  # заглушка False чтобы посчитать количество
    dict_kw = pd.DataFrame(list(cloud_kw(list_trash[mask], data_ignore, word).items()), columns=['keywords', 'sort']).sort_values(by='sort', ascending=False)
    lst_kw = []
    lst_kw_for_tenderland = word + '+('
    lst1 = dict_kw['keywords'].head().to_list()
    lst2 = dict_kw['sort'].head().to_list()
    for i in range(len(lst1)):
        lst1[i] = str((ending(lst1[i], ending1, ending2, ending3)))
        lst_kw.append(lst1[i] + ' - ' + str(lst2[i]))
        lst_kw_for_tenderland = lst_kw_for_tenderland + lst1[i] + '/'
        mask2 += temp_df['Название'].str.contains(lst1[i].strip(), regex=False)  # перебор для общего количества лотов по ключам
    lst_kw_for_tenderland = lst_kw_for_tenderland[:-1] + ')'
    lst_kw_for_tenderland = "".join(lst_kw_for_tenderland)
    kw_for_tenderland.append(lst_kw_for_tenderland)
    lst_kw = "; ".join(lst_kw)
    kw_trash.append(lst_kw)
    kw_trash_lots.append(sum(mask2))
export_df['kw_trash'] = kw_trash
export_df['kw_trash_tl'] = kw_for_tenderland
export_df['kw_trash_lots'] = kw_trash_lots

# sort
if sum(data_import['Снимаем'] == '2') > 0:
    print('Ищем связки слов для sort')
    kw_sort = []
    kw_for_tenderland = []
    for word in keywords:
        mask = list_sort.str.contains(word.strip(), regex=False)
        dict_kw = pd.DataFrame(list(cloud_kw(list_sort[mask], data_ignore, word).items()),
                               columns=['keywords', 'sort']).sort_values(by='sort', ascending=False)
        lst_kw = []
        lst_kw_for_tenderland = ending(word, ending1, ending2, ending3) + '+('    # собираем ключевые слова без окончаний
        lst1 = dict_kw['keywords'].head().to_list()
        lst2 = dict_kw['sort'].head().to_list()
        for i in range(len(lst1)):
            lst_kw.append(lst1[i] + ' - ' + str(lst2[i]))
            lst_kw_for_tenderland = lst_kw_for_tenderland + str((ending(lst1[i], ending1, ending2, ending3)) + '/')
        lst_kw_for_tenderland = lst_kw_for_tenderland[:-1] + ')'
        lst_kw_for_tenderland = "".join(lst_kw_for_tenderland)
        kw_for_tenderland.append(lst_kw_for_tenderland)
        lst_kw = "; ".join(lst_kw)
        kw_sort.append(lst_kw)
    export_df['kw_sort'] = kw_sort
    export_df['kw_sort_tl'] = kw_for_tenderland



print('Сохраняем в export.csv ...')
while True:  # проверка, если файл открыт
    try:
        export_df.to_csv('export.csv', sep=';', encoding='windows-1251', index=False, header=True)
        break
    except IOError:    # PermissionError
        input('Необходимо закрыть файл inn_list.csv перед сохранением данных')

print('Готово!')
