import pytest


class TestUserListAPI:
  def test_get(self, client):
    res = client.get('/api/v1/users/')
    data = res.get_json()
    assert data == {'test': 'value'}

