"""
Tests for services endpoints
"""
from flask import url_for
import pytest

VIEW_NAME = 'api.index'

@pytest.mark.usefixtures('client')
class TestAPIIndexView(object):

    def test_index_returns_200(self):
        res = self.client.get(url_for(VIEW_NAME))
        assert res.status_code == 200
