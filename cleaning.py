import re
import string

# Load the consolidated text from the file
with open('consolidated_text.txt', 'r', encoding='utf-8') as file:
    consolidated_text = file.read()

# Remove headers and footers (if any)
consolidated_text = re.sub(r'HeaderText.*?EndHeaderText', '', consolidated_text, flags=re.DOTALL)
consolidated_text = re.sub(r'FooterText.*?EndFooterText', '', consolidated_text, flags=re.DOTALL)

# Remove page numbers and section numbers
consolidated_text = re.sub(r'\d+\n', '', consolidated_text)

# Remove special characters and convert to lowercase
consolidated_text = consolidated_text.translate(str.maketrans('', '', string.punctuation)).lower()

# Remove stopwords (if needed)
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
consolidated_text = ' '.join([word for word in consolidated_text.split() if word not in stop_words])

# Split the text into sections or topics
sections = re.split(r'\n{2,}', consolidated_text)

# Process each section
cleaned_sections = []
for section in sections:
    if section.strip():
        cleaned_sections.append(section.strip())

# Save the cleaned data to a file
with open('cleaned_data.txt', 'w', encoding='utf-8') as file:
    file.write('\n\n'.join(cleaned_sections))