strings = ["aaaad", "aaaaaad", "aaabd", "aaacd", "abaad"]
strings.sort(key=len)
shortest = strings[0]
shortest_list = list(shortest)
shortest_list.sort()
last_SL_item = ""
main_count_no_repeat = 0
main_count_repeat = 0

for SL_item in shortest_list:
  if last_SL_item == SL_item:
    continue
  count_min = strings[0].count(SL_item)
  for string in strings:

    letter_count = string.count(SL_item)

    if count_min > letter_count:
      count_min = letter_count

  last_SL_item = SL_item

  if count_min > 0:
    main_count_no_repeat += 1
    main_count_repeat += count_min
print (main_count_no_repeat)
print (main_count_repeat)