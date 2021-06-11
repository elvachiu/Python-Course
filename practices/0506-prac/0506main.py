import json
import webbrowser
import csv

with open('animal.json', encoding='utf8') as a_json:
    content = json.load(a_json)
cnt = 0
for data in content:
    if not data.get('animal_colour'):
        continue
    if not data.get('animal_kind'):
        continue
    if not data.get('album_file'):
        continue
    if data['animal_colour'] == '黑色' and data['animal_kind'] == '狗':
        webbrowser.open(data['album_file'])
        cnt += 1
    if cnt >= 5:
        break

# csv.reader
with open('animal.csv', 'r', encoding='utf8') as FILE:
    rd = csv.reader(FILE)
    rows = [row for row in rd]

for row in rows[:10]:
    print(row)

# csv.writer
with open('test.csv', 'w') as FILE:
    # wt = csv.writer(FILE)
    # wt.writerow(*['Name', 'Height', 'Weight'])
    # wt.writerow(['EC', 162, 46])
    print(*['Name', 'Height', 'Weight'], sep=',', file=FILE)
    print(['EC', 162, 46], sep=',', file=FILE)

with open('test.csv', 'r') as FILE:
    rd = csv.DictReader(FILE)
    rows = [row for row in rd]

print(rows)
