from fastapi import FastAPI
from fastapi.responses import HTMLResponse

html = """
<!DOCTYPE html>
<html>
<head>
<title>Test</title>
</head>
<body>
<h1>HALAMAN JALAN!</h1>
</body>
</html>
"""

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(html)
