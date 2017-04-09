the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

the_count.extend(fruits)
print the_count

the_count.append('star')
print the_count

the_count.insert(-2, 'light')
print the_count

the_count.insert(-1, 'pig')
print the_count

the_count.insert(0, 'dragon')
print the_count

the_count.insert(3, 'fans')
print the_count

the_count.insert(3, change)
print the_count

the_count.remove(1)
print the_count

the_count.insert(2, 2)
the_count.insert(6, 2)
the_count.insert(4, 2)
print the_count

the_count.remove(2)
print the_count

the_count.pop(9)
print the_count

change_place = the_count.index(change)
print change_place

number_of_two = the_count.count(2)
print number_of_two

the_count.sort()
print the_count

the_count.reverse()
print the_count


