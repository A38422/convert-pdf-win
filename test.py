import requests

payload = {'out_folder': r'C:\Users\Tuan Minh\PycharmProjects\report-pdf',
           'sample_doc': r'C:\Users\Tuan Minh\PycharmProjects\report-pdf\download.docx'}
response = requests.post("http://127.0.0.1:5000/upload", data=payload)
