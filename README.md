To use just run the colab notebook main.ipynb and run all cells.
#@title Playground
INPUT_TEXT = """

achieve act direction advance apply focus evaluate assign help attack automate reward drive build calculate change choose clarify classify train collaborate communicate compete fulfill compose

"""

dict_to_pdf({
    "input_text": INPUT_TEXT,
    "file name": "OUTPUT.pdf",
    "amount of pages": 4,
    "empty space": 0.8
})


The important functions are:

Function: insert_text_into_table

Inputs:

    text (string): the text to be inserted into the table.
    tag (string): the tag to be associated with the text.
    database_default_name (string): the default name of the database.
    table_default_name (string): the default name of the table.

Example usage:

python

insert_text_into_table(long_text="example text", tag="example tag", database_default_name="example_db", table_default_name="example_table")

Function: db_to_pdf

Inputs:

    base_name (string): the name of the base to be used.
    table_name (string): the name of the table to be used.
    tags_to_include (list of strings): the tags to include in the PDF.
    num_pages (integer): the number of pages to include in the PDF.
    pdf_filename (string): the name of the PDF file to be created.
    word_space_ratio (float): the percentage of words to be replaced with spacebars.

Example usage:

python

db_to_pdf(base_name="example_base", table_name="example_table", tags_to_include=["example_tag"], num_pages=3, pdf_filename="example_file.pdf", word_space_ratio=0.6)

