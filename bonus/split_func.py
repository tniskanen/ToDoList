def count_names(all_names):
    items = all_names.split(',')
    return len(items)


names = input('Enter names seperated by commas(no spaces): ')

num_names = count_names(names)
print(num_names)
