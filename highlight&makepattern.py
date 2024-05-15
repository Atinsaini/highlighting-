import re
import fitz






pattern=re.compile(r'\b{}\b'.format(re.escape("indemnify")), re.IGNORECASE)






if __name__ == '__main__':
        document = fitz.Document('E:/Python/pdfproject/Contract 4 - Unreviewed.pdf')
        for page in document.pages():
                page_text=page.get_text()
                for sentence in page_text.split("."):
                       for match in re.findall(pattern,sentence):
                               if match:
                                       rect=page.search_for(sentence)
                                       page.add_highlight_annot(rect)
                               else:
                                      print("not found")

        document.save('E:/Python/pdfproject/exactrect.pdf')
            
