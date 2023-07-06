import unittest
from pystax.checker import DomainProbe

probe = DomainProbe()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        domain_result = probe.probe_domain("example.com")
        print(domain_result)

    def test_something2(self):
        domain_result = probe.probe_domain("example.org")
        print(domain_result)

    def test_something3(self):
        domain_result = probe.probe_domain("hgwhd.xty")
        print(domain_result)

    def test_something4(self):
        domain_result = probe.probe_domain("404.com")
        print(domain_result)

    def test_something5(self):
        domain_result = probe.probe_domain("gov.uk")
        print(domain_result)

    def test_something5(self):
        domain_result = probe.probe_domain("192.168.0.1")
        print(domain_result)

    def test_something6(self):
        ip_result = probe.probe_ip("192.168.0.1")
        print(ip_result)

    def test_something8(self):
        ip_result = probe.probe_ip("999.999.999.999")
        print(ip_result)

    def test_something9(self):
        ip_result = probe.probe_ip("1.1.1.1")
        print(ip_result)

    def test_something10(self):
        ip_result = probe.probe_ip("127.0.0.1")
        print(ip_result)

    def test_something11(self):
        ip_result = probe.probe_ip("djcnjdcn")
        print(ip_result)

    def test_something12(self):
        ip_result = probe.probe_ip("asfdsseee")
        print(ip_result)

    def test_something13(self):
        ip_result = probe.probe_ip("bing.com")
        print(ip_result)


if __name__ == '__main__':
    unittest.main()
