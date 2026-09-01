# "안녕" 텍스트와 클릭하면 바뀌는 버튼이 있는 웹페이지를 서빙하는 서버
# 실행: python server.py
# 접속: http://localhost:8000

import http.server
import os

PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(("", PORT), handler) as httpd:
    print(f"서버 실행 중: http://localhost:{PORT}")
    httpd.serve_forever()
