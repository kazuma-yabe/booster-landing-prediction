#Create an interactive dashboard for visualising SpaceX data using Plotly Dash

# Import libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Import SpaceX launch data
spacex_df = pd.read_csv("data/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Initialise a dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

                                #Add a dropdown menu for selecting a launch site, All by default
                                dcc.Dropdown(id='site-dropdown',
                                            options=[{'label': 'All Sites', 'value': 'ALL'}] 
                                            + [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()],
                                            value='ALL',
                                            placeholder='Select a Launch Site here',
                                            searchable=True
                                        ),
                                html.Br(),

                                #Add a pie chart for success rates
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (kg):"),

                                #Add a slider for selecting the payload range 
                                html.Div(
                                dcc.RangeSlider(
                                id='payload-slider',
                                min=0,  # starting point
                                max=10000,  # ending point
                                step=1000,  # interval
                                value=[min_payload, max_payload],  # default range
                                marks={i: f'{i}\u00A0kg' for i in range(0, 10001, 1000)},
                                ),
                                style={'margin-bottom': '30px'}
                                ),

                                #Add a scatter chart to show the relationship between payload and launch success rates
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

#Define a callback to update the pie chart based on the selected launch site
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(
            spacex_df,
            names='Launch Site',
            values='class',
            title='Total Success Launches by Site'
        )
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        success_fail_counts = filtered_df['class'].value_counts().reset_index()
        success_fail_counts.columns = ['class', 'count']
        success_fail_counts['outcome'] = success_fail_counts['class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(
            success_fail_counts,
            names='outcome',
            values='count',
            title=f'Success vs Failure for site {selected_site}',
            category_orders={'outcome': ['Success', 'Failure']},
            color='outcome',
            color_discrete_map={'Success': 'blue', 'Failure': 'red'}
        )
    
    return fig


#Define a callback to update the scatter chart as output,
#based on the selected values from site-dropdown and payload-slider as inputs

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter_chart(selected_site, payload_range):
    # Filter data based on the selected payload range
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) & 
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]
    
    if selected_site == 'ALL':
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Payload vs. Outcome for All Sites',
            labels={'Payload Mass (kg)': 'Payload Mass (kg)'},
            hover_data=['Launch Site']
        )
    else:
        # Filter data for the selected launch site
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Payload vs. Outcome for {selected_site}',
            labels={'Payload Mass (kg)': 'Payload Mass (kg)'},
            hover_data=['Launch Site']
        )

    fig.update_yaxes(
    tickmode='array',
    tickvals=[0, 1],
    ticktext=['Failure', 'Success'],
    title=dict(
        text='Launch Outcome',
        font=dict(size=12)
    ))
    
    return fig

# Run the dash app server
if __name__ == '__main__':
    app.run_server()
