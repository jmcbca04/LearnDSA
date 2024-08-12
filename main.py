from fastapi import FastAPI, Request, Form
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
        4: "Stacks and Queues",
        5: "Trees and Graphs",
    }
    lesson_content = lessons.get(lesson_id, "Lesson content not found.")
    return templates.TemplateResponse("lesson.html", {"request": request, "lesson_id": lesson_id, "lesson_content": lesson_content})

@app.get("/quiz/{quiz_id}", response_class=HTMLResponse)
async def read_quiz(request: Request, quiz_id: int):
    # You can expand this with more quizzes or dynamically generate questions.
    quizzes = {
        1: "What is the time complexity of accessing an element in an array?",
        2: "What data structure is used to implement a queue?",
    }
    question = quizzes.get(quiz_id, "Quiz question not found.")
    return templates.TemplateResponse("quiz.html", {"request": request, "quiz_id": quiz_id, "question": question})

@app.get("/lessons", response_class=HTMLResponse)
async def list_lessons(request: Request):
    return templates.TemplateResponse("lessons.html", {"request": request})

@app.get("/quizzes", response_class=HTMLResponse)
async def list_quizzes(request: Request):
    return templates.TemplateResponse("quizzes.html", {"request": request})

@app.post("/quiz/{quiz_id}")
async def submit_quiz(request: Request, quiz_id: int, answer: str = Form(...)):
    correct_answers = {
        1: "O(1)",  # Expected answer for quiz 1
        2: "Linked List",  # Expected answer for quiz 2
    }
    correct_answer = correct_answers.get(quiz_id, None)
    if answer.strip().lower() == correct_answer.lower():
        feedback = "Correct!"
    else:
        feedback = "That's not right. Review the lesson on " + (
            "Arrays" if quiz_id == 1 else "Linked Lists"
        ) + " and try again."
    question = correct_answers.get(quiz_id, "Quiz question not found.")
    return templates.TemplateResponse("quiz.html", {"request": request, "quiz_id": quiz_id, "question": question, "feedback": feedback})