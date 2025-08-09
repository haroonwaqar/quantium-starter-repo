import pytest
from dash.testing.application_runners import import_app

import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

# This will import your app from app.py
@pytest.fixture
def dash_app():
    app = import_app("app")  # assuming your app file is app.py
    return app

def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel Sales" in header.text  # adjust text to your actual header

def test_visualisation_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    chart = dash_duo.find_element("#sales-line-chart")
    assert chart is not None

def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None
