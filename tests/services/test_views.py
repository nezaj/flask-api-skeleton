"""
Tests for services endpoints
"""
from flask import url_for
import pytest

VIEW_NAME = 'services.health'

@pytest.mark.usefixtures('client')
class TestServicesHealthView(object):

    def test_health_returns_200(self):
        res = self.client.get(url_for(VIEW_NAME))
        assert res.status_code == 200
