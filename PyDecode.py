import base64
filename = input('FileName: ')
with open(filename, 'rb') as f:
    data = f.read()
with open(filename, 'wb') as f:
    f.write(base64.decodebytes(data))