from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFPage
from pdfminer.pdfparser import PDFException
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

"""
PDFのページオブジェクトを取得するメソッド
"""
def getPdfPages(filename):
    # PDFファイルを開く
    # r：読込モード、b：バイナリモード
    fp = open(filename, 'rb')

    # PDF解析オブジェクトを生成
    parser = PDFParser(fp)
    document = PDFDocument()
    parser.set_document(document) # set document to parser

    # PDFのオブジェクトを生成
    password="" # pdfを開くときのパスワード
    document.set_parser(parser) # set parser to document
    document.initialize(password)

    # Check if the document allows text extraction. If not, abort.
    if not document.is_extractable:
        raise PDFException
    return document.get_pages()

def getPdfLayout(filename):
    # ファイルを開く
    fp = open(filename, 'rb')
    # parser生成
    parser = PDFParser(fp)
    # ドキュメントオブジェクト生成
    document = PDFDocument()
    # parserにドキュメントを設定
    parser.set_document(document)

    document.set_parser(parser)

    # PDFリソース管理オブジェクト生成
    manager = PDFResourceManager()
    rettxt = StringIO()
    # 解析のパラメータオブジェくを生成
    laparams = LAParams()

    # アグリゲーターの生成
    device = TextConverter(manager, rettxt, code='utf-8', laparams=laparams)
    # インタプリタの生成
    interpreter = PDFPageInterpreter(manager, device)

    # PDFページを取得
    pages = list(document.get_pages())
    page1 = pages[0]

    interpreter.process_page(page1)

    layout = device.get_result()

    for l in layout:
        print(l.get_text())

