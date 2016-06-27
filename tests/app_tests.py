from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def text_index():
    # check that we get a 400 on / URL
    resp = app.request('/')
    assert_response(resp, status="404")

    # check that we get a 200 on /hello URL
    resp = app.request("/hello")
    assert_response(resp, status="200")

    # test get request to / URL
    resp = app.request("/")
    assert_response(resp)

    # make sure default values work from the form
    resp = app.request("/", method="POST")
    assert_response(resp, contains="Nobody")

    # test that our expected values work
    data = { 'name': 'Lee', 'greet': 'Howdy' }
    resp = app.request('/', method="POST", data=data)
    assert_response(resp, contains="Lee")
