import os

# from src.ingestion.pdf_loader import load_pdf
# from src.ingestion.text_splitter import split_text
# from src.ingestion.create_embeddings import get_embedding

# from src.vectordb.chroma_manager import collection

# PDF_FOLDER = "data/pdfs"

# doc_id = 0

# for file in os.listdir(PDF_FOLDER):

#     if not file.endswith(".pdf"):
#         continue

#     pdf_path = os.path.join(
#         PDF_FOLDER,
#         file
#     )

#     text = load_pdf(pdf_path)

#     chunks = split_text(text)

#     for chunk in chunks:

#         embedding = get_embedding(chunk)

#         collection.add(
#             ids=[str(doc_id)],
#             documents=[chunk],
#             embeddings=[embedding],
#             metadatas=[
#                 {
#                     "source": file
#                 }
#             ]
#         )

#         doc_id += 1

# print("Documents indexed successfully.")


from src.ingestion.create_embeddings import create_embeddings

create_embeddings()