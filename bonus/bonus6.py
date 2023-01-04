contents = ["all girls are the same", "I admit it, another hoes got me trippin", "broke my heart oh no your didnt"]

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for content, filename in zip(contents, filenames):
    file = open(f'files\{filename}', 'w')
    file.write(content)
