import re
import string

# Load the consolidated text from the file
with open("demo.txt", "r", encoding="utf-8") as file:
    consolidated_text = file.read()

# Remove headers and footers (if any)
consolidated_text = re.sub(r".*Header.*\n", "", consolidated_text, flags=re.DOTALL)
print(consolidated_text)

# Remove page numbers and section numbers
consolidated_text = re.sub(r"\d+\n", "", consolidated_text)

# Remove special characters excluding certain punctuations
printable = set(string.printable)
keep_punct = set(string.punctuation) - set(r'!@#$%^&*()_+{}[]|\\:;"<>?,./`~')
consolidated_text = "".join(
    filter(
        lambda x: x in printable and (x.isalnum() or x in keep_punct), consolidated_text
    )
)

# Convert to lowercase
consolidated_text = consolidated_text.lower()

# Split the text into sections or topics based on specific headings or keywords
section_pattern = r"(?:section|topic|heading)\s*:\s*(.+?)\n"
sections = re.split(section_pattern, consolidated_text, flags=re.IGNORECASE)
sections = [section.strip() for section in sections if section.strip()]

# Add newline characters between sections
cleaned_text = "\n\n".join(sections)

# Save the cleaned data to a file
with open("cleaned_data.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)
