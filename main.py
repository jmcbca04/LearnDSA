from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/lesson/{lesson_id}", response_class=HTMLResponse)
async def read_lesson(request: Request, lesson_id: int):
    lessons = {
        1: "Introduction to Data Structures",
        2: "Understanding Arrays",
        3: "Exploring Linked Lists",
    }
    lesson_content = lessons.get(lesson_id, "Lesson content not found.")
    return templates.TemplateResponse("lesson.html", {"request": request, "lesson_id": lesson_id, "lesson_content": lesson_content})