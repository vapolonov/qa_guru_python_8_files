from zipfile import ZipFile, PyZipFile

# zip_ = ZipFile('resources/hello.zip')
# print(zip_.namelist())
# # zip_.extract('Hello.txt', 'tmp')
# text = zip_.read('Hello.txt')
# print(text)
# zip_.close()

with ZipFile('resources/hello.zip') as myzip:
    print(*myzip.namelist())
    myzip.extract('Hello.txt', 'resources')  # извлечь указанный файл в директорию
    myzip.extractall('tmp')  # извлечь все файлы в указанную директорию
    text = myzip.read('Hello.txt')
    print(text)

# Прочитать файл не распаковывая
# with ZipFile('resources/hello.zip') as myzip:
#     with myzip.open('Hello.txt') as my_file:
#         print(my_file.read())


with ZipFile('tmp/create.zip', 'w') as myzip:
    myzip.write('resources/sample.csv')
    myzip.write('resources/selenium.png')

# import os
# import zipfile
#
# fantasy_zip = zipfile.ZipFile('C:\\Stories\\Fantasy\\archive.zip', 'w')
#
# for folder, subfolders, files in os.walk('C:\\Stories\\Fantasy'):
#
#     for file in files:
#         if file.endswith('.pdf'):
#             fantasy_zip.write(os.path.join(folder, file),
#                               os.path.relpath(os.path.join(folder, file), 'C:\\Stories\\Fantasy'),
#                               compress_type=zipfile.ZIP_DEFLATED)
#
# fantasy_zip.close()