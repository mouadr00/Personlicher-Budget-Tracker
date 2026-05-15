from nicegui import ui
from ui.pages import create_pages

create_pages()

ui.run(
    title='Persönlicher Budget Tracker',
    reload=True
)