import pytest
import numpy as np
from app import app as flask_app
# from click.testing import CliRunner
from mlib import format_input, scale_input, height_human

@pytest.fixture
def test_array():
    val = np.array(1)
    feature = val.reshape(-1, 1)
    return feature

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_format_input(test_array):
    assert test_array.shape == format_input(2).shape

def test_scale_input(test_array):
    assert int(scale_input(test_array)) == int(np.array([[-9.56513601]]))

def test_height_human():
    assert "6 foot, 1 inches" == height_human(73.4)
    assert "5 foot, 11 inches" == height_human(71.1)

def test_index(app, client):
    res = client.get("/")
    assert res.status_code == 200
    expected = "Predict the height from weight of MLB players"
    assert expected in res.get_data(as_text=True)
