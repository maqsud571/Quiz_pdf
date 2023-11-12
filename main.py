# boshladik
import sqlite3
import time
import random

connection = sqlite3.connect("question.db")
sql = connection.cursor()
#
# PRIMARY TABLE QUESTIONS
sql.execute(
    """CREATE TABLE IF NOT EXISTS Questions(

        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        quests VARCHAR(200) NOT NULL UNIQUE,
        FOREIGN KEY (id) REFERENCES Variants(id) 
        );"""
)
#
# variants table & foreign key bilan ulanga Questions tablega
sql.execute(
    """CREATE TABLE IF NOT EXISTS Variants(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        A VARCHAR(255) NOT NULL,
        B VARCHAR(255) NOT NULL,
        C VARCHAR(255) NOT NULL,
        D VARCHAR(255) NOT NULL
        );"""
)


# QUEST UCHUN INSERT QILADIGAN FUNCTIA ARGUMENTLARIGA ADD PRODUCTSDAN MALUOT OLADI


def Table_quest(quest):
    sql.execute(
        f"""INSERT INTO Questions(id,quests) VALUES (NULL, '{quest}');"""
    )


# VARIANT UCHUN INSERT QILADIGAN FUNCTIA ARGUMENTLARIGA ADD PRODUCTSDAN MALUOT OLADI


def Table_variant(A, B, C, D):
    sql.execute(
        f"""INSERT INTO Variants(id,A,B,C,D) VALUES (NULL,'A) {A}','B) {B}','C) {C}','D) {D}');"""
    )


# TABLELAGE ADD QILADI FOREIGN KEY BILAN ULANGAN QUEST BILAN VARIANT
def Add_Prudcts():
    # QUESTGA ADD QILADI
    while True:
        inp_choose = input("Do you want to add a question (Y/N): ")
        if inp_choose.lower() == "y" or inp_choose.upper() == "Y":
            inp_quest = input("Enter the question: ").capitalize()
            if inp_quest.endswith("?"):
                Table_quest(inp_quest)
                print("question is successfuly!")
                time.sleep(1)
                print("Add an option to the question!")
                inp_A = input("A: ").title()
                inp_B = input("B: ").title()
                inp_C = input("C: ").title()
                inp_D = input("D: ").title()
                Table_variant(inp_A, inp_B, inp_C, inp_D)
            else:
                print("togri yoz gandon")
                time.sleep(0.5)
                continue
        else:
            break
Add_Prudcts()


def show_products():
    # SELECT TABLE KORSATIB BERADIGAN SELECT FOREIGN UCHUN
    sql.execute(
        "SELECT quests,A,B,C,D FROM Questions INNER JOIN Variants ON Questions.id = Variants.id"
    )
    result = sql.fetchall()
    # datadegi questlani randomni chiqarib beradi
    # ENDI SHU CODNI PDFGA TIQIB CHIQARIB BERISH KERAK
    random.shuffle(result)
    a = 0
    for i in result:
        a += 1
        print(f'{a}:{i}')


show_products()

connection.commit()
connection.close()

# INFO FOR FERIGN KEYS SHOWS
# cursor.execute("SELECT Questions.id, Questions.quests, Variants.A, Variants.B, Variants.C, Variants.D FROM Questions INNER JOIN Variants ON Questions.var_id = Variants.id")

# manimcha tugattim