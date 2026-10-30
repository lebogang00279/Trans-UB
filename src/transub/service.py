from datetime import datetime,timedelta,timezone
import sqlite3,uuid
class ReservationError(Exception):
    def __init__(self,status,code,message): super().__init__(message); self.status=status; self.code=code; self.message=message
class NotificationPort:
    def notify(self,order_ref,seller_id): return 'DELIVERED'
class FailingNotification(NotificationPort):
    def notify(self,order_ref,seller_id): raise RuntimeError('notification failed')
class ReservationService:
    def __init__(self,conn_factory,notification=None): self.conn_factory=conn_factory; self.notification=notification or NotificationPort()
    def reserve(self,listing_id,buyer_id,note=None):
        if not listing_id or not buyer_id: raise ReservationError(400,'INVALID_REQUEST','listingId and buyerId are required')
        c=self.conn_factory(); now=datetime.now(timezone.utc); deadline=now+timedelta(hours=24); ref='ORD-'+uuid.uuid4().hex[:10].upper()
        try:
            c.execute('BEGIN IMMEDIATE')
            buyer=c.execute('SELECT * FROM student_accounts WHERE student_id=?',(buyer_id,)).fetchone()
            if buyer is None: raise ReservationError(404,'BUYER_NOT_FOUND','Buyer not found')
            if not buyer['eligible'] or not buyer['active']: raise ReservationError(403,'BUYER_NOT_ELIGIBLE','Buyer is not eligible')
            listing=c.execute('SELECT * FROM listings WHERE listing_id=?',(listing_id,)).fetchone()
            if listing is None: raise ReservationError(404,'LISTING_NOT_FOUND','Listing not found')
            if listing['seller_id']==buyer_id: raise ReservationError(403,'OWN_LISTING','Buyer cannot reserve own listing')
            if not listing['approved'] or listing['status']!='Available': raise ReservationError(409,'LISTING_NOT_AVAILABLE','Listing is no longer available')
            c.execute('INSERT INTO orders VALUES (?,?,?,?,?,?,?)',(ref,listing_id,buyer_id,now.isoformat(),deadline.isoformat(),'Pending',note))
            c.execute('INSERT INTO order_status_changes(order_reference,from_status,to_status,changed_at,actor_type) VALUES (?,?,?,?,?)',(ref,None,'Pending',now.isoformat(),'Buyer'))
            if c.execute("UPDATE listings SET status='Reserved' WHERE listing_id=? AND status='Available'",(listing_id,)).rowcount!=1: raise ReservationError(409,'LISTING_NOT_AVAILABLE','Listing is no longer available')
            c.execute('COMMIT')
        except ReservationError:
            try:c.execute('ROLLBACK')
            except sqlite3.OperationalError:pass
            c.close(); raise
        except sqlite3.IntegrityError:
            try:c.execute('ROLLBACK')
            except sqlite3.OperationalError:pass
            c.close(); raise ReservationError(409,'DUPLICATE_RESERVATION','Live reservation already exists')
        seller_id=listing['seller_id']; c.close(); outcome='DELIVERED'
        try: outcome=self.notification.notify(ref,seller_id)
        except Exception: outcome='FAILED'
        c=self.conn_factory(); c.execute('INSERT INTO notifications(order_reference,recipient_id,raised_at,delivery_outcome) VALUES (?,?,?,?)',(ref,seller_id,datetime.now(timezone.utc).isoformat(),outcome)); c.close()
        return {'orderReference':ref,'listingId':listing_id,'buyerId':buyer_id,'status':'Pending','listingStatus':'Reserved','responseDeadline':deadline.isoformat(),'notificationOutcome':outcome}
