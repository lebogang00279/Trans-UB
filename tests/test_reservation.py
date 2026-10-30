import tempfile,threading,unittest
from pathlib import Path
from src.transub.db import initialize,connect
from src.transub.setup_db import seed
from src.transub.service import ReservationService,ReservationError,FailingNotification
class T(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.db=Path(self.tmp.name)/'t.db'; c=initialize(self.db); seed(c); c.close()
    def tearDown(self): self.tmp.cleanup()
    def f(self): return connect(self.db)
    def test_success(self):
        r=ReservationService(self.f).reserve('LIST-104','202302072'); self.assertEqual((r['status'],r['listingStatus']),('Pending','Reserved'))
        c=self.f(); self.assertEqual(c.execute("SELECT status FROM listings WHERE listing_id='LIST-104'").fetchone()['status'],'Reserved'); self.assertEqual(c.execute("SELECT COUNT(*) n FROM orders").fetchone()['n'],1); self.assertEqual(c.execute("SELECT COUNT(*) n FROM order_status_changes").fetchone()['n'],1); c.close()
    def test_invalid(self):
        with self.assertRaises(ReservationError) as x: ReservationService(self.f).reserve('LIST-104',None)
        self.assertEqual(x.exception.code,'INVALID_REQUEST')
    def test_own_listing(self):
        with self.assertRaises(ReservationError) as x: ReservationService(self.f).reserve('LIST-OWN','202302072')
        self.assertEqual(x.exception.code,'OWN_LISTING')
    def test_ineligible(self):
        with self.assertRaises(ReservationError) as x: ReservationService(self.f).reserve('LIST-104','202399999')
        self.assertEqual(x.exception.code,'BUYER_NOT_ELIGIBLE')
    def test_duplicate(self):
        ReservationService(self.f).reserve('LIST-104','202302072')
        with self.assertRaises(ReservationError): ReservationService(self.f).reserve('LIST-104','202300002')
        c=self.f(); self.assertEqual(c.execute("SELECT COUNT(*) n FROM orders WHERE status='Pending'").fetchone()['n'],1); c.close()
    def test_notification_failure(self):
        r=ReservationService(self.f,FailingNotification()).reserve('LIST-104','202302072'); self.assertEqual(r['notificationOutcome'],'FAILED')
        c=self.f(); self.assertEqual(c.execute("SELECT status FROM listings WHERE listing_id='LIST-104'").fetchone()['status'],'Reserved'); self.assertEqual(c.execute("SELECT status FROM orders").fetchone()['status'],'Pending'); c.close()
    def test_concurrent_exactly_one(self):
        b=threading.Barrier(2); results=[]; lock=threading.Lock()
        def w(buyer):
            b.wait()
            try: out=('success',ReservationService(self.f).reserve('LIST-104',buyer)['orderReference'])
            except ReservationError as e: out=('error',e.code)
            with lock: results.append(out)
        a=threading.Thread(target=w,args=('202302072',)); d=threading.Thread(target=w,args=('202300002',)); a.start(); d.start(); a.join(); d.join()
        self.assertEqual(sum(x[0]=='success' for x in results),1); self.assertEqual(sum(x[0]=='error' for x in results),1)
        c=self.f(); self.assertEqual(c.execute("SELECT COUNT(*) n FROM orders WHERE status='Pending'").fetchone()['n'],1); c.close()
if __name__=='__main__': unittest.main()
