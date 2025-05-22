import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load cleaned Titanic dataset
df = pd.read_csv("cleaned_titanic_data.csv")

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Titanic Survival Dashboard"

# Layout: Title + Filters + KPIs + Graphs
app.layout = html.Div([
    html.H1("Titanic Survival Dashboard", style={'textAlign': 'center', 'marginBottom': 30}),
    
    # Filters: Pclass, Sex, Embarked
    html.Div([
        html.Div([
            html.Label("Select Passenger Class:"),
            dcc.Dropdown(
                id='pclass-dropdown',
                options=[{'label': str(cls), 'value': cls} for cls in sorted(df['Pclass'].unique())] + [{'label': 'All', 'value': 'All'}],
                value='All'
            )
        ], style={'width': '30%', 'display': 'inline-block', 'paddingRight': '10px'}),
        
        html.Div([
            html.Label("Select Sex:"),
            dcc.Dropdown(
                id='sex-dropdown',
                options=[{'label': sex.capitalize(), 'value': sex} for sex in df['Sex'].unique()] + [{'label': 'All', 'value': 'All'}],
                value='All'
            )
        ], style={'width': '30%', 'display': 'inline-block', 'paddingRight': '10px'}),

        html.Div([
            html.Label("Select Embarked:"),
            dcc.Dropdown(
                id='embarked-dropdown',
                options=[{'label': emb, 'value': emb} for emb in df['Embarked'].dropna().unique()] + [{'label': 'All', 'value': 'All'}],
                value='All'
            )
        ], style={'width': '30%', 'display': 'inline-block'})
    ], style={'marginBottom': 40}),

    # KPI cards
    html.Div([
        html.Div(id='total-passengers', className='kpi-card', style={'width': '30%', 'display': 'inline-block'}),
        html.Div(id='survival-rate', className='kpi-card', style={'width': '30%', 'display': 'inline-block'}),
        html.Div(id='avg-age', className='kpi-card', style={'width': '30%', 'display': 'inline-block'}),
    ], style={'textAlign': 'center', 'marginBottom': 50}),

    # Graphs grid
    html.Div([
        dcc.Graph(id='survival-bar'),
        dcc.Graph(id='sex-pie'),
        dcc.Graph(id='title-bar'),
        dcc.Graph(id='fare-box'),
        dcc.Graph(id='family-scatter'),
    ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '40px'})
])

# Callback: filter data based on selections, update KPIs and graphs
@app.callback(
    [
        Output('total-passengers', 'children'),
        Output('survival-rate', 'children'),
        Output('avg-age', 'children'),
        Output('survival-bar', 'figure'),
        Output('sex-pie', 'figure'),
        Output('title-bar', 'figure'),
        Output('fare-box', 'figure'),
        Output('family-scatter', 'figure'),
    ],
    [
        Input('pclass-dropdown', 'value'),
        Input('sex-dropdown', 'value'),
        Input('embarked-dropdown', 'value'),
    ]
)
def update_dashboard(pclass, sex, embarked):
    # Filter data based on dropdowns
    filtered_df = df.copy()
    if pclass != 'All':
        filtered_df = filtered_df[filtered_df['Pclass'] == pclass]
    if sex != 'All':
        filtered_df = filtered_df[filtered_df['Sex'] == sex]
    if embarked != 'All':
        filtered_df = filtered_df[filtered_df['Embarked'] == embarked]

    # Calculate KPIs
    total_passengers = len(filtered_df)
    survival_rate = filtered_df['Survived'].mean() if total_passengers > 0 else 0
    avg_age = filtered_df['Age'].mean() if total_passengers > 0 else 0

    # Format KPI cards as HTML Divs
    total_passengers_div = html.Div([
        html.H3("Total Passengers"),
        html.P(f"{total_passengers}")
    ], style={'backgroundColor': '#f0f0f0', 'padding': '20px', 'borderRadius': '5px'})

    survival_rate_div = html.Div([
        html.H3("Survival Rate"),
        html.P(f"{survival_rate:.2%}")
    ], style={'backgroundColor': '#d4edda', 'padding': '20px', 'borderRadius': '5px'})

    avg_age_div = html.Div([
        html.H3("Average Age"),
        html.P(f"{avg_age:.1f} years")
    ], style={'backgroundColor': '#cce5ff', 'padding': '20px', 'borderRadius': '5px'})

    # Graph 1: Survival by gender bar chart
    survival_fig = px.histogram(
        filtered_df, x='Survived', color='Sex',
        barmode='group',
        labels={'Survived': 'Survival (0 = No, 1 = Yes)'},
        title="Survival by Gender"
    )

    # Graph 2: Gender distribution pie chart
    sex_pie_fig = px.pie(
        filtered_df, names='Sex',
        title='Gender Distribution'
    )

    # Graph 3: Survival by Title bar chart
    title_bar_fig = px.histogram(
        filtered_df, x='Title', color='Survived',
        barmode='group',
        title='Survival by Title'
    )

    # Graph 4: Fare distribution boxplot
    fare_box_fig = px.box(
        filtered_df, y='Fare', color='Survived',
        title='Fare Distribution by Survival'
    )

    # Graph 5: Family size vs Survival scatter plot
    family_scatter_fig = px.scatter(
        filtered_df, x='FamilySize', y='Survived', color='Sex',
        title='Family Size vs Survival',
        labels={'FamilySize': 'Family Size', 'Survived': 'Survival (0 = No, 1 = Yes)'}
    )

    return (
        total_passengers_div,
        survival_rate_div,
        avg_age_div,
        survival_fig,
        sex_pie_fig,
        title_bar_fig,
        fare_box_fig,
        family_scatter_fig,
    )


if __name__ == '__main__':
    app.run_server(debug=True)
