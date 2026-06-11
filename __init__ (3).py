from fastapi import FastAPI

app = FastAPI(title='StarVault Protocol')

@app.get('/')
def health():
    return {'status':'running','protocol':'SVP v0.1'}
