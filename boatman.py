import PyPDF2

# List of PDF file paths
pdf_file_paths = [
    r'C:\Users\The Den\Desktop\Dialogflow Project\PDF data\Cummins Onan Generator manual.pdf',
    r'C:\Users\The Den\Desktop\Dialogflow Project\PDF data\Dometic Refrigerator.pdf',
    r'C:\Users\The Den\Desktop\Dialogflow Project\PDF data\Dometic Standup refrigerator.pdf',
    r'C:\Users\The Den\Desktop\Dialogflow Project\PDF data\Onan Generator .pdf'
]

# Create an empty string to store the consolidated text
consolidated_text = ''

# Loop through each PDF file
for file_path in pdf_file_paths:
    try:
        with open(file_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)

            # Loop through each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                consolidated_text += text + '\n'  # Append page text with a newline
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Save the consolidated text to a new file
output_file = r'C:\Users\The Den\Desktop\consolidated_text.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(consolidated_text)

print(f'Text extracted and consolidated into {output_file}')