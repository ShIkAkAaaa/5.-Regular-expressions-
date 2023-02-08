from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pattern = r'([+]?)([78])\s?.?(\d{3}).?[-]?\s?(\d{3})[-]?(\d{2})[-]?(\d{2})\s?\(?(доб.)?\s?(\d{4})?'
substitution = r'+7(\3)\4-\5-\6 \7\8'
list_fcs = []
for list_1 in contacts_list:
  for list_info in list_1:
    obj_tel = re.match(pattern, list_info)
    if obj_tel != None:
      obj_tel_tel = obj_tel.group()
      final_phone = re.sub(pattern, substitution, obj_tel_tel)
      list_fcs.append(final_phone)

number1 = 0
list1 = []
list2 = []
for list_2 in contacts_list:
  for t in list_2:
    if number1 > 2:
      if len(list2) < 3:
        list2 = list2 + ['']
      number1 = 0
      list1.append(list2)
      list2 = []
      break
    list_123 = t.split(' ')
    if list_123 != ['']:
      list2 += list_123
    number1 += 1

number2 = 0
for list_3 in contacts_list:
  list1[number2] += list_3[3:7]
  number2 += 1
for list_4 in list1:
  contact1 = list_4[0]
  contact2 = list_4[1]
  for list_5 in list1:
    if contact1 == list_5[0] and contact2 == list_5[1]:
      if list_4[2] == '':
        list_4[2] = list_5[2]
      if list_4[3] == '':
        list_4[3] = list_5[3]
      if list_4[4] == '':
        list_4[4] = list_5[4]
      if list_4[5] == '':
        list_4[5] = list_5[5]
      if list_4[6] == '':
        list_4[6] = list_5[6]
for list_5 in list1:
  if list1.count(list_5) > 1:
    list1.remove(list_5)

number3 = 0
number4 = 0
for list_6 in list1:
  if number4 > 0:
    list_6[5] = list_fcs[number3]
    number3 += 1
  number4 += 1
  if number3 > 5:
    break

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(list1)

