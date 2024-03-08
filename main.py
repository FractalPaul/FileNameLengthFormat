import pyperclip

# Read the clipboard for any text and check to see if the length of the text is greater than the max length of the file name for Windows 10.

# Max file Name length
maxFileName = 210

# Read text from clipboard
text = pyperclip.paste()

# Remove any new line characters at the end of the string.
text = text.strip()

# Remove periods and commas
text = text.replace('.', '')
text = text.replace(',', '')

# Remove everything after any HTTPS links
httpsIndex = text.index('https')
if httpsIndex > 0:
    text = text[0: httpsIndex]

# Remove any 'and'
if len(text) >= maxFileName:
    text = text.replace('and ', '').replace('And ','')

# Remove any 'The' if length is still greater than max file name length.
if len(text) >= maxFileName:
    text = text.replace('the ', '').replace('The ', '')
# Remove any 'A ' if length is still greater.
if len(text) >= maxFileName:
    text = text.replace(' a ', ' ').replace('A ', '')

# Remove any ' as '
if len(text) >= maxFileName:
    text = text.replace(' as ', ' ').replace('As ', '')
# Remove any ' is '
if len(text) >= maxFileName:
    text = text.replace(' is ', ' ').replace('Is ', '')
# Remove any 'in '
if len(text) >= maxFileName:
    text= text.replace(' in ', ' ').replace('In ', '')
# Remove any ' with '
if len(text) >= maxFileName:
    text = text.replace(' with ', ' ')

# Remove any ' to '
if len(text) >= maxFileName:
    text = text.replace(' to ', ' ')
# Remove any ' up '
if len(text) >= maxFileName:
    text = text.replace(' up ', ' ')

# Remove any ' has '
if len(text) >= maxFileName:
    text = text.replace(' has ', ' ')
    
# Replace Image x of t with 'Ix-f'
if len(text) >= maxFileName:
    imageStr ='Image ? of ?'
    indImage = text.index(' Image ')
    imageText = text[indImage+1: indImage + 1 + len(imageStr)]
    newImageText = imageText.replace('Image ', 'I').replace(' of ', 'of')
    text = text.replace(imageText,newImageText)
    
# Remove any double spaces and replace with a single space.
text= text.replace('  ', ' ')
text = text.strip()

# Write the modified text back to clipboard
pyperclip.copy(text)