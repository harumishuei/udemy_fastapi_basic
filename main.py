from fastapi import FastAPI
from routers import contact #パッケージ読み込む
app = FastAPI()

app.include_router(contact.router)
@app.get("/") #このURLにアクセスしたら、下のコードが実行される
async def root():
    return {"message": "Hello World"}