from nicegui import ui


def sidebar():

    with ui.column().classes(
        'bg-blue-900 text-white h-screen w-64 p-4'
    ):
        
        ui.label('Budget Tracker').classes(
            'text-2xl font-bold mb-8'
            )
        
        ui.link('Dashboard').classes(
            'text-white text-lg mb-3'
        )

        ui.link('+ Einnahme hinzufügen, '/income').classes(
                'text-white text-lg mb-3'
        )

        ui.link('- Ausgabe hinzufügen', '/expense').classes(
                'text-white text-lg mb-3'
        )
        ui.link('Monatsübersicht', '/monthly-overview').classes(
                'text-white text-lg mb-3'
        )

        ui.link('Kategorien, '/categories').classes(
                'text-white text-lg mb-3'

        )

def page_layout(title: str):

    with ui.column().classes('w-full p-8'):
        
        ui.label(title).classes(
            'text-3xl font-bold text-blue-500 text-Helvetica mb-6'
        )

def summary_card(title: str, value: str, color: str):):

    with ui.card().classes(
        f'p-6 w-64 shadow-lg rounded-xl bg-{color}-100'
    ):

        ui.label(title).classes(
            'text-lg font-semibold text-gray-700 mb-2'
        )

        ui.label(value).classes(
            'text-2xl font-bold text-gray-900'
        )