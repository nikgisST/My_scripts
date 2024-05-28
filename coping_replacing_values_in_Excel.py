import pandas as pd

substitution_dicts = {
    'Стълб': {'Подтип': {0: 'Стълб - недиференцирано', 1: 'Дървен', 2: 'Композитен', 3: 'Стоманорешетъчен',
                         4: 'Стоманотръбен', 5: 'Стоманобетонен'}},
    'Оборудване на стълб': {
        'Вид оборудване': {1: 'Изолатор', 2: 'Конзола', 3: 'Обтяжка/подпора', 4: 'Заземителен контур'}},
    'РОМ - РОС': {'Експлоатационно състояние': {0: 'Изключено', 1: 'Включено', 2: 'НЯМА ИНФОРМАЦИЯ'},
                  'Вид': {0: 'Секциониращ разединител', 1: 'Товаров разединител с ДУ', 2: 'Реклоузер', 3: 'РОМ',
                          4: 'РОС'}},
    'Вентилен отвод': {'Фази': {0: 'НЯМА ИНФОРМАЦИЯ', 1: 'L3', 2: 'L2', 3: 'L2-L3', 4: 'L1', 5: 'L1-L3', 6: 'L1-L2',
                                7: 'L1-L2-L3'}}
                     }

def add_additional_headers(file_path):
    xls = pd.ExcelFile(file_path)
    header_length = {
        'Стълб': {'start': 1, 'end': -3},
        'Оборудване на стълб': {'start': 1, 'end': None},
        'РОМ - РОС': {'start': 1, 'end': None},
        'Вентилен отвод': {'start': 1, 'end': None},
        'ИЗКС': {'start': 1, 'end': None},
        'Проводник': {'start': 1, 'end': None},
    }
    modified_df = {}   #modified DataFrames for each sheet
    headers_dict = {}  #headers for each sheet

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name, header=None) # Load each sheet into a DataFrame

        indices = header_length.get(sheet_name, {'start': 0, 'end': None})  #start and end indices for the current sheet
        headers = df.iloc[0, indices['start']:indices['end']].dropna().tolist() # Extract headers based on start and end indices
        headers_dict[sheet_name] = headers    # Store the headers in the dictionary
        additional_headers = headers + ['Забележка ЕРМЗ', 'Pontech'] * 3
        new_headers = pd.Series(additional_headers)   # Create a new DataFrame to store the additional headers
        all_headers_df = pd.concat([df, pd.DataFrame([new_headers])], axis=1)
        modified_df[sheet_name] = all_headers_df   # Add the modified DataFrame to the dictionary

    intermediate_result_path = apply_substitutions(source_file_path, result_path, substitution_dicts)
    with pd.ExcelWriter(intermediate_result_path, engine='openpyxl') as result:    # openpyxl is used for writing the .xlsx file; default: xlsxwriter
        for sheet, modified_df in modified_df.items():
            modified_df.to_excel(result, sheet_name=sheet, index=False, header=False)
    return intermediate_result_path


def apply_substitutions(source_file_path, intermediate_result_path, substitution_dicts):
    xls = pd.ExcelFile(source_file_path)
    with pd.ExcelWriter(intermediate_result_path, engine='openpyxl') as result:  # openpyxl is used for writing the .xlsx file; default: xlsxwriter
        for sheet in xls.sheet_names:
            df = pd.read_excel(source_file_path, sheet_name=sheet)
            if sheet == "Стълб":
                df = df.drop(columns=['Линк'])  # , errors='ignore'

            if sheet in substitution_dicts:
                for column, mapping_value in substitution_dicts[sheet].items():
                    df[column] = df[column].map(mapping_value).fillna(df[column])
            df.to_excel(result, index=False, sheet_name=sheet)

        comments_column = pd.DataFrame(columns=['OBJECTID *', 'Текст', 'Забележка ЕРМЗ',
                                                'Pontech', 'Забележка ЕРМЗ', 'Pontech',
                                                'Забележка ЕРМЗ', 'Pontech'])
        comments_column.to_excel(result, index=False, sheet_name='Коментари в ГИС')
    return intermediate_result_path


source_file_path = r"D:\scripts\excel проверки\ВП1057-ВЕЦ Брусен-Искър-VR6401-20 kV-2.1.xlsx"
result_path = r"D:\scripts\excel проверки\ВП1057 Искър - проверка.xlsx"
intermediate_result_path = apply_substitutions(source_file_path, result_path, substitution_dicts)
final_result_path = add_additional_headers(intermediate_result_path)
print(f"Updated file saved to: {final_result_path}")
