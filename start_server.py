#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import threading
import time

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def open_browser():
    time.sleep(1.5)
    webbrowser.open(f'http://localhost:{PORT}')

if __name__ == "__main__":
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 서버가 시작되었습니다!")
        print(f"📱 브라우저에서 http://localhost:{PORT} 로 접속하세요")
        print(f"⏹️  서버를 중지하려면 Ctrl+C를 누르세요\n")
        
        # 브라우저 자동 열기
        browser_thread = threading.Thread(target=open_browser)
        browser_thread.daemon = True
        browser_thread.start()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n서버가 종료되었습니다.")

