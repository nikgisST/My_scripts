import pandas as pd

#one transformer can be associated with multiple transformerunits and one transformerunit can be associated with multiple transformers
#transformers = {'transformer_guid_1': ['transformerunit_guid_1', ['transformerunit_guid_2', .......,]}
#transformers = {'transformer_guid_2': ['transformerunit_guid_11', ['transformerunit_guid_12', .......,]}
transformers = {
    '{2827C9C0-8A3C-4246-94E4-03DD6557A6DC}': ['{51A73D6C-03B4-475E-BF90-51CFC5092899}', '{090015B8-AA75-44FC-A9E4-F9A1D48D061E}'],
    '{70FB278D-4CB6-4B61-9AF7-C3FCCD35CB28}': ['{090015B8-AA75-44FC-A9E4-F9A1D48D061E}', '{0ED783C9-C5C4-4894-9526-818EE735D6A4}'],
    '{8AB007D1-B7B9-467B-9A8B-F15DAE5D18B4}': ['{51A73D6C-03B4-475E-BF90-51CFC5092899}', '{0ED783C9-C5C4-4894-9526-818EE735D6A4}', '{890FFF4D-9A5B-4E5E-B07C-230D2251A9F8}']
    # more key with list of values pairs
}

#transformer_units = {'transformer_units_guid_1': ['transformer_guid_1', ['transformer_guid_2', .......,]}
#transformer_units = {'transformer_units_guid_2': ['transformer_guid_11', [ .......,]}
#transformer_units = {'transformer_units_guid_3': ['transformer_guid_111', [ .......,]}
transformer_units = {
    '{51A73D6C-03B4-475E-BF90-51CFC5092899}': ['{2827C9C0-8A3C-4246-94E4-03DD6557A6DC}', '{8AB007D1-B7B9-467B-9A8B-F15DAE5D18B4}'],
    '{090015B8-AA75-44FC-A9E4-F9A1D48D061E}': ['{2827C9C0-8A3C-4246-94E4-03DD6557A6DC}', '{70FB278D-4CB6-4B61-9AF7-C3FCCD35CB28}'],
    '{0ED783C9-C5C4-4894-9526-818EE735D6A4}': ['{70FB278D-4CB6-4B61-9AF7-C3FCCD35CB28}', '{8AB007D1-B7B9-467B-9A8B-F15DAE5D18B4}'],
    '{890FFF4D-9A5B-4E5E-B07C-230D2251A9F8}': ['{8AB007D1-B7B9-467B-9A8B-F15DAE5D18B4}'],
    # more key with list of values pairs
}

data = []

# MANY-TO-MANY RELATIONSHIPS
for transformer, transformerunit in transformers.items():
    for each_unit in transformerunit:
        if transformer in transformer_units[each_unit]:  # check that the association is valid both ways
            data.append({
                'ASSOCIATIONTYPE': 'Containment',
                'FROMFEATURECLASS': 'ElectricDevice',
                'FROMASSETGROUP': 'Medium Voltage Transformer',
                'FROMASSETTYPE': 'Station - MV->LV',
                'FROMGLOBALID': transformer,
                'FROMTERMINAL': '',
                'TOFEATURECLASS': 'ElectricJunctionObject',
                'TOASSETGROUP': 'Medium Voltage Line End',
                'TOASSETTYPE': 'Line End Type',
                'TOGLOBALID': each_unit,
                'TOTERMINAL': '',
                'ISCONTENTVISIBLE': 'TRUE',
                'PERCENTALONG': ''
            })

df = pd.DataFrame(data)
df.to_csv(r'D:\scripts\UN task 2\transformer_to_unit_associations_MANY-TO-MANY.csv', index=False)
print("Successful output!")