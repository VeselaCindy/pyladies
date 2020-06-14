barvy = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

barvy_ovoce_po_tydnu = barvy

for klic, hodnota in barvy.items():
    barvy_ovoce_po_tydnu[klic] = 'cerno-hnedo-' + hodnota

print(barvy_ovoce_po_tydnu)