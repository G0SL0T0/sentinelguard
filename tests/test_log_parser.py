import pytest
from core.log_parser import parse_nginx_log

def test_nginx_log_parsing():
    log_line = '192.168.1.1 - - [01/Jan/2023:12:00:00 +0000] "GET /test HTTP/1.1"'
    result = parse_nginx_log(log_line)
    assert result["ip"] == "192.168.1.1"
    assert "GET /test" in result["request"]