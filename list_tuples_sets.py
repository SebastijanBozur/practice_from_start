generations_jp = ['gen0','gen1', 'gen2', 'gen3','gen4', 'gen5', 'gen6']
generations_en = ['myth', 'council', 'advent']
nums = [1,4,6,12,5,7,9,99,13,43,23,54,22]

print(generations_jp[:2])
# generations.insert(-1, 'gen7')
# print(generations_jp)
generations_jp.extend(generations_en)
# print(generations_jp)

# generations_jp.remove('gen0')
# print(generations_jp)

# generations_jp.reverse()
# print(generations_jp)

# generations_jp.sort()
print(generations_jp)

# nums.sort(reverse=True)
print(nums)

sorted_numbs = sorted(nums)
print(sorted_numbs)
print(min(nums))
print(max(nums))
print(sum(nums))

print(generations_jp.index('gen2'))

for index, gen in enumerate(generations_jp, start=1):
    print(index,gen)

oneline = ', '.join(generations_jp)
print(oneline)

new_list = oneline.split(', ')

print(new_list)

