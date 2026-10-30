PRAGMA foreign_keys = ON;
CREATE TABLE student_accounts(student_id TEXT PRIMARY KEY,name TEXT NOT NULL,eligible INTEGER NOT NULL,active INTEGER NOT NULL);
CREATE TABLE listings(listing_id TEXT PRIMARY KEY,seller_id TEXT NOT NULL,title TEXT NOT NULL,status TEXT NOT NULL,approved INTEGER NOT NULL,FOREIGN KEY(seller_id) REFERENCES student_accounts(student_id));
CREATE TABLE orders(order_reference TEXT PRIMARY KEY,listing_id TEXT NOT NULL,buyer_id TEXT NOT NULL,placed_at TEXT NOT NULL,response_deadline TEXT NOT NULL,status TEXT NOT NULL,buyer_note TEXT,FOREIGN KEY(listing_id) REFERENCES listings(listing_id),FOREIGN KEY(buyer_id) REFERENCES student_accounts(student_id));
CREATE UNIQUE INDEX one_live_order_per_listing ON orders(listing_id) WHERE status IN ('Pending','Accepted','Delivered');
CREATE TABLE order_status_changes(id INTEGER PRIMARY KEY AUTOINCREMENT,order_reference TEXT NOT NULL,from_status TEXT,to_status TEXT NOT NULL,changed_at TEXT NOT NULL,actor_type TEXT NOT NULL,FOREIGN KEY(order_reference) REFERENCES orders(order_reference));
CREATE TABLE notifications(id INTEGER PRIMARY KEY AUTOINCREMENT,order_reference TEXT NOT NULL,recipient_id TEXT NOT NULL,raised_at TEXT NOT NULL,delivery_outcome TEXT NOT NULL,FOREIGN KEY(order_reference) REFERENCES orders(order_reference));
