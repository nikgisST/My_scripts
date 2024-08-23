import pandas as pd

#one transformer associated with multiple transformerunits
#transformers = {'transformer_guid_1': ['transformerunit_guid_1', ['transformerunit_guid_2', .......,]}
#transformers = {'transformer_guid_2': ['transformerunit_guid_11', ['transformerunit_guid_12', .......,]}
transformers = {
                '{2827C9C0-8A3C-4246-94E4-03DD6557A6DC}': ['{51A73D6C-03B4-475E-BF90-51CFC5092899}', '{090015B8-AA75-44FC-A9E4-F9A1D48D061E}'],
                '{70FB278D-4CB6-4B61-9AF7-C3FCCD35CB28}': ['{890FFF4D-9A5B-4E5E-B07C-230D2251A9F8}', '{0ED783C9-C5C4-4894-9526-818EE735D6A4}'], # More units if needed
                # more key with list of values pairs
               }

data = []

# ONE-TO-MANY RELATIONSHIPS
for transformer, transformerunit in transformers.items():
    for each_unit in transformerunit:
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