import pandas as pd
import sqlite3
import matplotlib.backends.backend_pdf
import matplotlib.pyplot as plt


connection = sqlite3.connect('question.db')

sql_query = '''
SELECT Questions.id, Questions.quests, Variants.A, Variants.B, Variants.C, Variants.D
FROM Questions
JOIN Variants ON Questions.id = Variants.id;
'''

# SQL ma'lumotlarini olish va DataFramega joylash
df = pd.read_sql(sql_query, connection)

# PDF faylni yaratish
pdf_file_path = 'maqsud.pdf'
pdf_pages = matplotlib.backends.backend_pdf.PdfPages(pdf_file_path)

# Test savollarni yaratish
for index, row in df.iterrows():
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')
    ax.text(0.1, 0.8, f"Question: {row['quests']}", fontsize=18, wrap=True)
    ax.text(0.1, 0.6, f"{row['A']}.", fontsize=14, wrap=True)
    ax.text(0.1, 0.5, f"{row['B']}.", fontsize=14, wrap=True)
    ax.text(0.1, 0.4, f"{row['C']}.", fontsize=14, wrap=True)
    ax.text(0.1, 0.3, f"{row['D']}.", fontsize=14, wrap=True)
    pdf_pages.savefig(fig, bbox_inches='tight')
    plt.close(fig)

pdf_pages.close()