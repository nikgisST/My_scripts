import pandas as pd

substitution_dicts = {
    'Стълб': {'Подтип': {0: 'Стълб - недиференцирано', 1: 'Дървен', 2: 'Композитен', 3: 'Стоманорешетъчен',  4: 'Стоманотръбен', 5: 'Стоманобетонен'}},
    'Оборудване на стълб': {'Вид оборудване': {1: 'Изолатор', 2: 'Конзола', 3: 'Обтяжка/подпора', 4: 'Заземителен контур'}},
    'РОМ - РОС': {'Експлоатационно състояние': {0: 'Изключено', 1: 'Включено', 2: 'НЯМА ИНФОРМАЦИЯ'},
                  'Вид': {0: 'Секциониращ разединител', 1: 'Товаров разединител с ДУ', 2: 'Реклоузер', 3: 'РОМ', 4: 'РОС'}},
    'Вентилен отвод': {'Фази': {0: 'НЯМА ИНФОРМАЦИЯ', 1: 'L3', 2: 'L2', 3: 'L2-L3', 4: 'L1', 5: 'L1-L3', 6: 'L1-L2', 7: 'L1-L2-L3'}}
}

source_file_path = r"D:\scripts\excel проверки\ВП1057-ВЕЦ Брусен-Искър-VR6401-20 kV-2.1.xlsx"
source_xls = pd.ExcelFile(source_file_path)

# Create a writer object for the new destination file
result_path = r"D:\scripts\excel проверки\ВП1057 Искър - проверка.xlsx"
with pd.ExcelWriter(result_path, engine='openpyxl') as result:    # openpyxl is used for writing the .xlsx file; default: xlsxwriter
    for sheet in source_xls.sheet_names:
        df = pd.read_excel(source_file_path, sheet_name=sheet)
        if sheet == "Стълб":
            df = df.drop(columns=['Линк'])  #, errors='ignore'
            new_columns = ['Функция/Предназначение', 'Подтип', 'Тип', 'Защита на птици', 'Тип на основата',
                           'Забележка ЕРМЗ', 'Pontech', 'Забележка ЕРМЗ', 'Pontech', 'Забележка ЕРМЗ', 'Pontech']

        if sheet in substitution_dicts:
            for column, mapping_value in substitution_dicts[sheet].items():
                df[column] = df[column].map(mapping_value).fillna(df[column])
        df.to_excel(result, index=False, sheet_name=sheet)

    comments_column = pd.DataFrame(columns=['OBJECTID *', 'Текст', 'Забележка ЕРМЗ',
                                            'Забележка Pontech', 'Забележка ЕРМЗ', 'Pontech',
                                            'Забележка ЕРМЗ', 'Pontech'])
    comments_column.to_excel(result, index=False, sheet_name='Коментари в ГИС')

print(f"Updated file saved at: {result_path}")
