import json,re
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from .db import connect,DEFAULT_DB
from .service import ReservationService,ReservationError
rx=re.compile(r'^/api/listings/([^/]+)/reserve$')
class Handler(BaseHTTPRequestHandler):
    def reply(self,status,p):
        b=json.dumps(p).encode(); self.send_response(status); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_POST(self):
        m=rx.match(self.path)
        if not m:return self.reply(404,{'error':'NOT_FOUND'})
        try:p=json.loads(self.rfile.read(int(self.headers.get('Content-Length','0'))) or b'{}')
        except Exception:return self.reply(400,{'error':'INVALID_REQUEST'})
        try:return self.reply(201,ReservationService(lambda:connect(DEFAULT_DB)).reserve(m.group(1),p.get('buyerId'),p.get('buyerNote')))
        except ReservationError as e:return self.reply(e.status,{'error':e.code,'message':e.message})
    def log_message(self,*a): pass
if __name__=='__main__':
    print('TRANS-UB API on http://127.0.0.1:8000'); ThreadingHTTPServer(('127.0.0.1',8000),Handler).serve_forever()
