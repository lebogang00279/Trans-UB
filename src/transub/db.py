import sqlite3
from pathlib import Path
DEFAULT_DB = Path('transub.db')
def connect(path=DEFAULT_DB):
    c=sqlite3.connect(path,timeout=5,isolation_level=None,check_same_thread=False); c.row_factory=sqlite3.Row; c.execute('PRAGMA foreign_keys=ON'); return c
def initialize(path=DEFAULT_DB):
    c=connect(path); schema=Path(__file__).resolve().parents[2]/'migrations-or-schema'/'schema.sql'; c.executescript(schema.read_text()); return c
