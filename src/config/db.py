from sqlalchemy import create_engine, MetaData

password = 'root'
engine = create_engine(f"mysql+pymysql://admin:{password}@localhost:3306/storedb")

meta = MetaData()

conn = engine.connect()
