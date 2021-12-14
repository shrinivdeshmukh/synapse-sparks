from fastapi import FastAPI, File, UploadFile
from yaml import safe_dump, safe_load
from core.utils import checkdir
from core.pipeline import Pipeline
from pandas import DataFrame
from os import environ

app = FastAPI()


@app.post('/run')
async def run(db_url: str, file: UploadFile = File(...)):
    folder = 'config'
    environ['DB_URL'] = db_url
    checkdir(folder)
    with open(f'{folder}/{file.filename}', 'w') as f:
        safe_dump(safe_load(await file.read()), f)
    p = Pipeline(f'{folder}/{file.filename}')
    df = p.run()
    if isinstance(df, DataFrame):
        df.fillna(0, inplace=True)
        df = df.to_dict("records")
    return {"message": df}
