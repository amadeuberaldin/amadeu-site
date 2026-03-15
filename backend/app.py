from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Amadeu Beraldin - Projetos")


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.get('/', response_class=HTMLResponse)
def root():
    return """
    <!doctype html>
    <html lang='pt-BR'>
      <head>
        <meta charset='utf-8' />
        <meta name='viewport' content='width=device-width, initial-scale=1' />
        <title>Amadeu Beraldin</title>
        <style>
          body {
            margin: 0;
            font-family: Inter, system-ui, sans-serif;
            background: #0B0F19;
            color: #e5eefb;
            display: grid;
            place-items: center;
            min-height: 100vh;
          }
          main {
            max-width: 720px;
            padding: 32px;
            text-align: center;
          }
          a {
            color: #60A5FA;
            text-decoration: none;
          }
        </style>
      </head>
      <body>
        <main>
          <h1>Amadeu Beraldin</h1>
          <p>Aplicação FastAPI ativa.</p>
          <p><a href='/health'>Ver health check</a></p>
        </main>
      </body>
    </html>
    """