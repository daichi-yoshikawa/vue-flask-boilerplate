import os
import pytest

from flask_app import create_app


@pytest.fixture
def app():
  app = create_app(testing=True)
  return app
