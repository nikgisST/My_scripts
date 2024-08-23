import pandas as pd

#one transformer associated with one transformerunit
transformers = [
    '{2827C9C0-8A3C-4246-94E4-03DD6557A6DC}',
    '{70FB278D-4CB6-4B61-9AF7-C3FCCD35CB28}',
    # 66 transformers
]

transformer_units = [
    '{51A73D6C-03B4-475E-BF90-51CFC5092899}',
    '{890FFF4D-9A5B-4E5E-B07C-230D2251A9F8}',
    # 66 transformer units
]

data = []

# ONE-TO-ONE RELATIONSHIPS
for transformer, transformerunit in zip(transformers, transformer_units):     #tuples of corresponding elements from the two lists to create associations between them
    data.append({
        'ASSOCIATIONTYPE': 'Containment',
        'FROMFEATURECLASS': 'ElectricDevice',
        'FROMASSETGROUP': 'Medium Voltage Transformer',
        'FROMASSETTYPE': 'Station - MV->LV',
        'FROMGLOBALID': transformer,
        'FROMTERMINAL': '',
        'TOFEATURECLASS': 'ElectricJunctionObject',
        'TOASSETGROUP': 'Medium Voltage Line End',
        'TOASSETTYPE': 'Overhead Line End MV',        # or 'Underground Terminator MV'  or 'Overhead Line End MV' or 'Underground Terminator MV'
        'TOGLOBALID': transformerunit,
        'TOTERMINAL': '',
        'ISCONTENTVISIBLE': 'TRUE',
        'PERCENTALONG': ''
    })

df = pd.DataFrame(data)
df.to_csv(r'D:\scripts\UN task 2\transformer_to_unit_associations_ONE-TO-ONE.csv', index=False)
print("Successful output!")






























###################################################################################


transformers = ['{0001}', '{0002}', '{0003}']
transformer_units = ['{1001}', '{1002}', '{1003}']
paired = zip(transformers, transformer_units)

paired_list = list(paired)
print(paired_list)          # [('{0001}', '{1001}'), ('{0002}', '{1002}'), ('{0003}', '{1003}')]