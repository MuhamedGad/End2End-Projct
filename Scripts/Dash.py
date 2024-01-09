import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import mlflow
import mlflow.sklearn
import os
import pickle
import yaml
import pandas as pd
import numpy as np
from predict import model

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Global variables to store selected values
model_output_scores=[]
model_output_skills =[]
selected_language = []
selected_database = []
selected_platform = []
selected_webframe = []
selected_misc_tech = []
selected_tools = []
selected_target_role = []
skills = ['Python', 'Java', 'C']

# Layout of the app
app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row([
            dbc.Col(html.H1("TechSkill Explorer", className="text-center my-4 text-light"), width=12)
        ], className="bg-primary rounded-top py-2"),

        # Language section
        dbc.Row([
            dbc.Col([
                html.H3("Language", className="text-primary"),
                dcc.Dropdown(
                    id='language-selector',
                    options=[
                        {'label': language, 'value': language} for language in [
                            'APL', 'Ada', 'Apex', 'Assembly', 'Bash/Shell (all shells)', 'C',
                            'C#', 'C++', 'Clojure', 'Cobol', 'Crystal', 'Dart', 'Delphi', 'Elixir',
                            'Erlang', 'F#', 'Flow', 'Fortran', 'GDScript', 'Go', 'Groovy',
                            'HTML/CSS', 'Haskell', 'Java', 'JavaScript', 'Julia', 'Kotlin', 'Lisp',
                            'Lua', 'MATLAB', 'Nim', 'OCaml', 'Objective-C', 'PHP', 'Perl',
                            'PowerShell', 'Prolog', 'Python', 'R', 'Raku', 'Ruby', 'Rust', 'SAS',
                            'SQL', 'Scala', 'Solidity', 'Swift', 'TypeScript', 'VBA',
                            'Visual Basic (.Net)', 'Zig'
                        ]
                    ],
                    multi=True,
                    className="mb-3"
                ),
                html.Div(id='selected-language-output', className="lead text-muted")
            ], width=6)
        ], className="bg-light rounded-bottom p-3"),

        # Database section
        dbc.Row([
            dbc.Col([
                html.H3("Database", className="text-primary"),
                dcc.Dropdown(
                    id='database-selector',
                    options=[
                        {'label': database, 'value': database} for database in [
                            'BigQuery', 'Cassandra', 'Clickhouse', 'Cloud Firestore',
                            'Cockroachdb', 'Cosmos DB', 'Couch DB', 'Couchbase', 'Datomic',
                            'DuckDB', 'Dynamodb', 'Elasticsearch', 'Firebase Realtime Database',
                            'Firebird', 'H2', 'IBM DB2', 'InfluxDB', 'MariaDB', 'Microsoft Access',
                            'Microsoft SQL Server', 'MongoDB', 'MySQL', 'Neo4J', 'Oracle',
                            'PostgreSQL', 'RavenDB', 'Redis', 'SQLite', 'Snowflake', 'Solr',
                            'Supabase', 'TiDB'
                        ]
                    ],
                    multi=True,
                    className="mb-3"
                ),
                html.Div(id='selected-database-output', className="lead text-muted")
            ], width=6)
        ], className="bg-light rounded-bottom p-3"),

        # Platform section
        dbc.Row([
            dbc.Col([
                html.H3("Platform", className="text-primary"),
                dcc.Dropdown(
                    id='platform-selector',
                    options=[
                        {'label': platform, 'value': platform} for platform in [
                            'Amazon Web Services (AWS)', 'Cloudflare', 'Colocation',
                            'Digital Ocean', 'Firebase', 'Fly.io', 'Google Cloud', 'Heroku',
                            'Hetzner', 'IBM Cloud Or Watson', 'Linode, now Akamai',
                            'Managed Hosting', 'Microsoft Azure', 'Netlify', 'OVH', 'OpenShift',
                            'OpenStack', 'Oracle Cloud Infrastructure (OCI)', 'Render', 'Scaleway',
                            'VMware', 'Vercel', 'Vultr'
                        ]
                    ],
                    multi=True,
                    className="mb-3"
                ),
                html.Div(id='selected-platform-output', className="lead text-muted")
            ], width=6)
        ], className="bg-light rounded-bottom p-3"),

        # Webframe section
        dbc.Row([
            dbc.Col([
                html.H3("Webframe", className="text-primary"),
                dcc.Dropdown(
                    id='webframe-selector',
                    options=[
                        {'label': webframe, 'value': webframe} for webframe in [
                            'ASP.NET', 'ASP.NET CORE', 'Angular', 'AngularJS', 'Blazor',
                            'CodeIgniter', 'Deno', 'Django', 'Drupal', 'Elm', 'Express', 'FastAPI',
                            'Fastify', 'Flask', 'Gatsby', 'Laravel', 'Lit', 'NestJS', 'Next.js',
                            'Node.js', 'Nuxt.js', 'Phoenix', 'Play Framework', 'Qwik', 'React',
                            'Remix', 'Ruby on Rails', 'Solid.js', 'Spring Boot', 'Svelte',
                            'Symfony', 'Vue.js', 'WordPress', 'jQuery'
                        ]
                    ],
                    multi=True,
                    className="mb-3"
                ),
                html.Div(id='selected-webframe-output', className="lead text-muted")
            ], width=6)
        ], className="bg-light rounded-bottom p-3"),

        #MiscTech
        dbc.Row([
            dbc.Col([
                html.H3("MiscTech", className="text-primary"),
                dcc.Dropdown(
                    id='misc-tech-selector',
                    options=[
                        {'label': misc_tech, 'value': misc_tech} for misc_tech in [
                            '.NET (5+) ', '.NET Framework (1.0 - 4.8)', '.NET MAUI',
                           
                    '.NET MAUI',
                            'Apache Kafka', 'Apache Spark', 'CUDA', 'Capacitor', 'Cordova',
                            'Electron', 'Flutter', 'GTK', 'Hadoop', 'Hugging Face Transformers',
                            'Ionic', 'JAX', 'Keras', 'Ktor', 'MFC', 'Micronaut', 'NumPy', 'OpenGL',
                            'Opencv', 'Pandas', 'Qt', 'Quarkus', 'RabbitMQ', 'React Native',
                            'Scikit-Learn', 'Spring Framework', 'SwiftUI', 'Tauri', 'TensorFlow',
                            'Tidyverse', 'Torch/PyTorch', 'Uno Platform', 'Xamarin'
                        ]
                    ],
                    multi=True,
                    className="mb-3"
                ),
                html.Div(id='selected-misc-tech-output', className="lead text-muted")
            ], width=6)
        ], className="bg-light rounded-bottom p-3"),

        # Tools section
        dbc.Row([
            dbc.Col([
                html.H3("Tools", className="text-primary"),
                dcc.Dropdown(
                    id='tools-selector',
                    options=[
                        {'label': tool, 'value': tool} for tool in [
                            'APT', 'Ansible', 'Ant', 'Boost.Test', 'Bun', 'CMake', 'CUTE',
                            'Cargo', 'Catch2', 'Chef', 'Chocolatey', 'Composer', 'Dagger', 'Docker',
                            'ELFspy', 'GNU GCC', 'Godot', 'Google Test', 'Gradle', 'Homebrew',
                            'Kubernetes', 'LLVM\'s Clang', 'MSBuild', 'MSVC', 'Make',
                            'Maven (build tool)', 'Meson', 'Ninja', 'Nix', 'NuGet', 'Pacman', 'Pip',
                            'Podman', 'Pulumi', 'Puppet', 'QMake', 'SCons', 'Terraform', 'Unity 3D',
                            'Unreal Engine', 'Visual Studio Solution', 'Vite', 'Wasmer', 'Webpack',
                            'Yarn', 'bandit', 'build2', 'cppunit', 'doctest', 'lest',
                            'liblittletest', 'npm', 'pnpm', 'snitch', 'tunit'
                        ]
                    ],
                    multi=True,
                    className="mb-3"
                ),
                html.Div(id='selected-tools-output', className="lead text-muted")
            ], width=6)
        ], className="bg-light rounded-bottom p-3"),
        
        
        # Target Role section
        dbc.Row([
            dbc.Col([
                html.H3("Target Role", className="text-primary"),
                dcc.Dropdown(
                    id='target-role-selector',
                    options=[
                        {'label': role, 'value': role} for role in [
                            'Academic researcher', 'Cloud infrastructure engineer',
                            'Data or business analyst', 'Data scientist or machine learning specialist',
                            'Database administrator', 'DevOps specialist',
                            'Developer, QA or test', 'Developer, back-end',
                            'Developer, desktop or enterprise applications',
                            'Developer, front-end', 'Developer, full-stack',
                            'Developer, game or graphics', 'Developer, mobile',
                            'Engineer, data', 'Scientist', 'Security professional',
                            'System administrator'
                        ]
                    ],
                    multi=False,
                    className="mb-3"
                ),
                html.Div(id='selected-target-role-output', className="lead text-muted")
            ], width=6)
        ], className="bg-light rounded-bottom p-3"),
        
        
        
        
        # Button to trigger machine learning model
        dbc.Row([
            dbc.Col([
                dbc.Button("Get Recommendations", id='run-model-button', n_clicks=0, color="primary", className="mt-3"),
                html.Div(id='model-output', className="lead text-muted mt-3")
            ], width=12)
        ], className="bg-light rounded-bottom p-3"),
        
        



        # Bar Chart section
        dbc.Row([
            dbc.Col([
                html.H3("Role Scores", className="text-primary"),
                dcc.Graph(
                    id='role-scores-bar-chart',
                    figure={
                        'data': [
                            {'x': [score for _, score in model_output_scores], 'y': [role for role, _ in model_output_scores], 'type': 'bar', 'orientation': 'h'},
                        ],
                        'layout': {
                            'title': 'Role Scores',
                            'xaxis': {'title': 'Score'},
                            'yaxis': {'title': 'Role'},
                            'margin': {'l': 150, 'r': 10, 't': 30, 'b': 30},
                        }
                    }
                )
            ], width=12)
        ], className="bg-light rounded-bottom p-3"),

        
        # Additional section for displaying recommended skills
        dbc.Row([
            dbc.Col([
                html.H3("Recommended Skills", className="text-primary"),
                html.Div(id='recommended-skills-output', className="lead text-muted")
            ], width=12)
        ], className="bg-light rounded-bottom p-3"),
        

    ]
)

# Callbacks to update selected values
@app.callback(
    Output('selected-language-output', 'children'),
    [Input('language-selector', 'value')]
)
def update_selected_language(selected_language_value):
    global selected_language
    if selected_language_value is not None:
        selected_language = selected_language_value
        return f"You selected languages: {', '.join(selected_language)}"
    else:
        return "No language selected"

@app.callback(
    Output('selected-database-output', 'children'),
    [Input('database-selector', 'value')]
)
def update_selected_database(selected_database_value):
    global selected_database
    if selected_database_value is not None:
        selected_database = selected_database_value
        return f"You selected databases: {', '.join(selected_database)}"
    else:
        return "No database selected"

@app.callback(
    Output('selected-platform-output', 'children'),
    [Input('platform-selector', 'value')]
)
def update_selected_platform(selected_platform_value):
    global selected_platform
    if selected_platform_value is not None:
        selected_platform = selected_platform_value
        return f"You selected platforms: {', '.join(selected_platform)}"
    else:
        return "No platform selected"

@app.callback(
    Output('selected-webframe-output', 'children'),
    [Input('webframe-selector', 'value')]
)
def update_selected_webframe(selected_webframe_value):
    global selected_webframe
    if selected_webframe_value is not None:
        selected_webframe = selected_webframe_value
        return f"You selected webframes: {', '.join(selected_webframe)}"
    else:
        return "No webframe selected"

@app.callback(
    Output('selected-misc-tech-output', 'children'),
    [Input('misc-tech-selector', 'value')]
)
def update_selected_misc_tech(selected_misc_tech_value):
    global selected_misc_tech
    if selected_misc_tech_value is not None:
        selected_misc_tech = selected_misc_tech_value
        return f"You selected misc tech: {', '.join(selected_misc_tech)}"
    else:
        return "No misc tech selected"

@app.callback(
    Output('selected-tools-output', 'children'),
    [Input('tools-selector', 'value')]
)
def update_selected_tools(selected_tools_value):
    global selected_tools
    if selected_tools_value is not None:
        selected_tools = selected_tools_value
        return f"You selected tools: {', '.join(selected_tools)}"
    else:
        return "No tools selected"

@app.callback(
    Output('selected-target-role-output', 'children'),
    [Input('target-role-selector', 'value')]
)
def update_selected_target_role(selected_target_role_value):
    global selected_target_role
    if selected_target_role_value is not None:
        selected_target_role = selected_target_role_value
        return f"You selected target role: {selected_target_role}"
    else:
        return "No target role selected"

# Callback to run machine learning model
@app.callback(
    [Output('recommended-skills-output', 'children'),
     Output('role-scores-bar-chart', 'figure')],
    [Input('run-model-button', 'n_clicks')],
    [State('language-selector', 'value'),
     State('database-selector', 'value'),
     State('platform-selector', 'value'),
     State('webframe-selector', 'value'),
     State('misc-tech-selector', 'value'),
     State('tools-selector', 'value'),
     State('target-role-selector', 'value')]
)
def run_machine_learning_model(n_clicks, language, database, platform, webframe, misc_tech, tools, target_role):
    print(f"n_clicks: {n_clicks}")
    print(f"Inputs: {language}, {database}, {platform}, {webframe}, {misc_tech}, {tools}, {target_role}")

    # Declare global variables
    global model_output_scores, model_output_skills

    if n_clicks > 0:
        # Combine all selected skills into a single list
        selected_features = [skill for sublist in [language, database, platform, webframe, misc_tech, tools] if sublist for skill in sublist]


        # Remove duplicates and convert to lowercase
#         selected_features = list(set(map(str.lower, selected_features)))

        # Call the model function with selected features and target role
        global model_output_skills, model_output_scores
        model_output_skills, model_output_scores = model(selected_features, target_role)

        # Display recommended skills
        recommended_skills_output = f"You may consider learning the following: {', '.join(model_output_skills)}"

        # Prepare data for bar chart
        bar_chart_data = [
            {'x': [score for _, score in model_output_scores], 'y': [role for role, _ in model_output_scores],
             'type': 'bar', 'orientation': 'h'},
        ]

        bar_chart_layout = {
            'title': 'Role Scores',
            'xaxis': {'title': 'Score'},
            'yaxis': {'title': 'Role'},
            'margin': {'l': 150, 'r': 10, 't': 30, 'b': 30},
        }

        # Reset global variables
        model_output_scores, model_output_skills = [], []

        return recommended_skills_output, {'data': bar_chart_data, 'layout': bar_chart_layout}
    else:
        return "", {'data': [], 'layout': {}}


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
