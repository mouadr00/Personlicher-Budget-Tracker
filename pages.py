from nicegui import ui
from ui.components import sidebar, page_layout, summary_card

def create_pages():
    
    @ui.page('/')
    def dashboard():

        with ui.row().classes('w-full'):
            sidebar()
        
            with ui.column().classes('p-8'):

        ui.label(
            'Persönlicher Budget Tracker'
        ).classes('text-3xl font-bold text-blue-500 text-Helvetica mb-4') 

        ui.label(
            'Dashboard'
            ).classes('text-3xl font-bold')

        with ui.row():

            ui.card().classes('p-6')
                ui.label('Einnahmen')
                ui.label('CHF 2500')
            
            ui.card().classes('p-6')
                ui.label('Ausgaben')
                ui.label('CHF 1500')
            
            ui.card().classes('p-6')
                ui.label('Saldo') 
                ui.label('CHF 1000') 
            
            ui.table(
                columns=[
                    {'name': 'date', 'label': 'Datum', 'field': 'date'},
                    {'name': 'category', 'label': 'Kategorie', 'field': 'category'},
                    {'name': 'amount', 'label': 'Betrag', 'field': 'amount'},
                ],
                rows=rows,
            )

# Demo Daten
transactions = [
    {'date': '2026-03-25',
     'category': 'Gehalt',
     'description': 'Teilzeitjob',
     'amount': '+CHF 2500'
     },
    {'date': '2026-03-26',
     'category': 'Miete',
     'description': 'Wohnung',
     'amount': '-CHF 1200'
     },   
     {'date': '2026-03-27',
     'category': 'Lebensmittel',
     'description': 'Supermarkt',
     'amount': '-CHF 100'
     }   
]

def create_pages():

# Login Page
@ui.page('/login')
def login_page():

    with ui.column().classes(
        'w-full h-screen items-center justify-center bg-gray-100'
    ):
        with ui.card().classes(
            'p-8 w-96 shadow-xl rounded-2xl bg-white'
        ):

            ui.label('' \
            'Budget Tracker Login'
            ).classes(
                'text-2xl font-bold text-gray-800 mb-6 text-center'
            )

            username = ui.input(
                'Benutzername'
                ).classes('w-full')

            password = ui.input(
                'Passwort', 
                password=True
                ).classes('w-full')

            def login():
                ui.notify(
                    f'Willkommen, {username.value}!',
                    color='green'
                )
                ui.navigate.to('/')

            ui.button(
                'Login',
                on_click=login
                ).classes(
                'w-full mt-4 bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition-colors duration-300'
            )

# Dashboard
@ui.page('/')
def dashboard_page():

    with ui.row().classes('w-full'):

        sidebar()

        with ui.column().classes('p-8 w-full bg-gray-100 min-h-screen'):
            ui.label(
                'Dashboard'
                ).classes('text-3xl font-bold text-gray-800 mb-6')
            
            page_layout('Dashboard')

            # Summary Cards
            
            with ui.row().classes('gap-6 mb-8'):

                summary_card(
                    'Einnahmen', 
                    'CHF 2500', 
                    'green'
                )

                summary_card(
                    'Ausgaben', 
                    'CHF 1500', 
                    'red'
                )

                summary_card(
                    'Saldo', 
                    'CHF 1000', 
                    'blue'
                )

            # Chart
            ui.echart({
                'xAxis': {
                    'type': 'category',
                    'data': [
                        'Januar', 
                        'Februar', 
                        'März', 
                        'April', 
                        'Mai', 
                        'Juni'
                    ]
                },
                'yAxis': {
                    'type': 'value'
                },
                'series': [{
                    'data': [
                        2000, 
                        2200, 
                        2500, 
                        2400, 
                        2600, 
                        2800
                    ],
                    'type': 'bar'
                }]
            }).classes('w-full h-96 bg-white rounded-xl shadow-lg') 

            ui.separator().classes('my-8')

            ui.label(
                'Letzte Transaktionen'
                ).classes(
                    'text-2xl font-bold text-gray-800 mb-4'
                )
            
            ui.table(
                columns=[
                    {
                        'name': 'date', 
                        'label': 'Datum', 
                        'field': 'date'
                    },
                    {
                        'name': 'category', 
                        'label': 'Kategorie', 
                        'field': 'category'
                    },
                    {
                        'name': 'description', 
                        'label': 'Beschreibung', 
                        'field': 'description'
                    },
                    {
                        'name': 'amount', 
                        'label': 'Betrag', 
                        'field': 'amount'
                    }
                ],
                rows=transactions,
            ).classes(
                'w-full bg-white rounded-xl shadow-lg'
                )
# Einnahme hinzufügen
@ui.page('/income')
def income_page():

    with ui.row().classes('w-full'):

        sidebar()

        with ui.column().classes(
            'p-8 w-full bg-gray-100 min-h-screen'
        ):
        
            page_layout(' + Einnahme hinzufügen')
            
            with ui.card().classes(
                'p-8 w-full max-w-xl shadow-xl'
            ):
                ui.input('Betrag')
                ui.input('Beschreibung')

                ui.select(
                    [
                        'Lohn'
                        'Nebenjob'
                        'Sparen'
                    ],
                    label='Kategorie'
                )

                ui.input('Datum')

                ui.button(
                    'Einnahme speichern',
                ).classes(
                    'w-full mt-4 bg-green-600 text-white py-2 rounded-lg hover:bg-green-600 transition-colors duration-300'
                )

# Ausgabe hinzufügen
@ui.page('/expense')
def expense_page():

    with ui.row().classes('w-full'):

        sidebar()

        with ui.column().classes(
            'p-8 w-full bg-gray-100 min-h-screen'
        ):
        
            page_layout('- Ausgabe hinzufügen')
            
            with ui.card().classes(
                'p-8 w-full max-w-xl shadow-xl'
            ):
                ui.input('Betrag')
                ui.input('Beschreibung')

                ui.select(
                    [
                        'Miete'
                        'Lebensmittel'
                        'Freizeit'
                    ],
                    label='Kategorie'
                )

                ui.input('Datum')

                ui.button(
                    'Ausgabe speichern',
                ).classes(
                    'w-full mt-4 bg-red-600 text-white py-2 rounded-lg hover:bg-red-700 transition-colors duration-300'
                )

# Monatsübersicht
@ui.page('/monthly-overview')
def monthly_overview_page():

    with ui.row().classes('w-full'):

        sidebar()

        with ui.column().classes(
            'p-8 w-full bg-gray-100 min-h-screen'
        ):
        
            page_layout('Monatsübersicht')
            
            ui.select(
                [
                    '2026-01',
                    '2026-02',
                    '2026-03',
                    '2026-04',
                    '2026-05',
                    '2026-06'
                ],
                label='Monat auswählen'
            ).classes('w-64 mb-6')

            ui.table(
                columns=[
                    {
                        'name': 'date', 
                        'label': 'Datum', 
                        'field': 'date'
                    },
                    {
                        'name': 'category', 
                        'label': 'Kategorie', 
                        'field': 'category'
                    },
                    {
                        'name': 'description', 
                        'label': 'Beschreibung', 
                        'field': 'description'
                    },
                    {
                        'name': 'amount', 
                        'label': 'Betrag', 
                        'field': 'amount'
                    },
                ],
                rows=transactions,
            ).classes(
                'w-full bg-white rounded-xl shadow-xl'
                )

# Kategorien
@ui.page('/categories')
def categories_page():  

    with ui.row().classes('w-full'):

        sidebar()

        with ui.column().classes(
            'p-8 w-full bg-gray-100 min-h-screen'
        ):
        
            page_layout('Kategorien')
            
            categories = [
                {'name': 'Lebensmittel'},
                {'name': 'Gehalt'},
                {'name': 'Miete'},
                {'name': 'Versicherung'},
                {'name': 'Freizeit'},
                {'name': 'Transport'},
                {'name': 'Sparen'}
                {'name': 'Sonstiges'}
                {'name': 'Sonstiges'}
            ]

            ui.table(
                columns=[
                    {
                        'name': 'name', 
                        'label': 'Kategorie', 
                        'field': 'name'
                    }
                ],
                rows=categories
            ).classes(
                'w-full max-w-lg bg-white shadow-lg rounded-xl'
                )
    