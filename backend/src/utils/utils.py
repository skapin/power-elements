import pandas as pd
import pdfkit as pdf
import requests
import logging

from config.settings import SETTINGS

LOG = logging.getLogger(__name__)


def pad(num, size):
    s = str(num) + ''
    while (len(s) < size):
        s = '0' + s
    return s


def is_status_ok(status):
    return 200 <= status < 300


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def convert_mvt_stock(mvt_stock):
    if mvt_stock == 1:
        return '+'
    elif mvt_stock == 3:
        return '-'
    else:
        return ''


def translate_boolean(boolean):
    return 'oui' if boolean else 'non'


def format_code(code, size):
    list_code = [code[i:i+size] for i in range(0, len(code), size)]
    return ' '.join(list_code)


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def generate_pdf_from_csv(fabrication_order_ref, items):
    html_header = "<!DOCTYPE html>\
                    <html>\
                    <head>\
                        <meta charset=\"utf-8\">\
                        <link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css\" integrity=\"sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T\" crossorigin=\"anonymous\">\
                        <script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\" integrity=\"sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo\" crossorigin=\"anonymous\"></script>\
                        <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js\" integrity=\"sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1\" crossorigin=\"anonymous\"></script>\
                        <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js\" integrity=\"sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM\" crossorigin=\"anonymous\"></script>\
                    </head>\
                    <h1> Ordre de fabrication </h1>\
                    <table border=\"0\" class=\"dataframe table table-striped table-bordered table-sm\">\
                    <thead>\
                        <tr style=\"text-align: center;\">\
                            <th>N de mouvement</th>\
                            <th>Référence</th>\
                            <th>Date</th>\
                            <th>Qui</th>\
                        </tr>\
                    </thead>\
                    <tbody>\
                        <tr>\
                            <td>" + fabrication_order_ref + "</td>\
                            <td></td>\
                            <td>" + items[0]['DO_DATE'] + "</td>\
                            <td></td>\
                        </tr>\
                    </tbody>\
                    <style>\
                        table.table-fit {\
                            font-size: 11px;\
                        }\
                        td {\
                            text-align: center;\
                        }\
                        @media print {\
                            tr:nth-child(even) td {\
                                background-color: #CCCCCC !important;\
                                -webkit-print-color-adjust: exact;\
                            }\
                        }\
                    </style>\
                    <br/>\
                    <br/>"
    csv_file = SETTINGS['EXPORT_FOLDER'] + '/OF/' + fabrication_order_ref+'.csv'
    html_file = csv_file[:-3]+'html'
    pdf_path = csv_file[:-3]+'pdf'
    df = pd.read_csv(csv_file, sep=',')
    df.fillna(value='', inplace=True)
    df.to_html(html_file, classes=['table', 'table-striped', 'table-bordered',
                                   'table-sm', 'table-fit'], border=0, index=False, justify='center')
    line_prepender(html_file, html_header)
    pdf.from_file(html_file, pdf_path)
    return pdf_path


def call(method, url, params=None, headers=None, **kwargs):
    req_headers = dict()
    if headers:
        req_headers.update(headers)
    return requests.request(method=method, url=url, params=params, headers=req_headers, **kwargs)
