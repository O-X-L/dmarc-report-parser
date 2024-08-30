import os
import unittest
from glob import glob

from lxml import etree

from .utils import main as util
from .main import extract_report, parse_report_file, parsed_forensic_reports_to_csv, \
    parsed_aggregate_reports_to_csv, parse_report_email, parsed_smtp_tls_reports_to_csv, ParserError
from .testdata import td


def minify_xml(xml_string):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.fromstring(xml_string.encode('utf-8'), parser)
    return etree.tostring(tree, pretty_print=False).decode('utf-8')


def compare_xml(xml1, xml2):
    parser = etree.XMLParser(remove_blank_text=True)
    tree1 = etree.fromstring(xml1.encode('utf-8'), parser)
    tree2 = etree.fromstring(xml2.encode('utf-8'), parser)
    return etree.tostring(tree1) == etree.tostring(tree2)


class Test(unittest.TestCase):
    def testBase64Decoding(self):
        """Test base64 decoding"""
        # Example from Wikipedia Base64 article
        b64_str = "YW55IGNhcm5hbCBwbGVhcw"
        decoded_str = util.decode_base64(b64_str)
        assert decoded_str == b"any carnal pleas"

    def testPSLDownload(self):
        subdomain = "foo.example.com"
        result = util.get_base_domain(subdomain)
        assert result == "example.com"

        # Test newer PSL entries
        subdomain = "e3191.c.akamaiedge.net"
        result = util.get_base_domain(subdomain)
        assert result == "c.akamaiedge.net"

    def testExtractReportXMLComparator(self):
        """Test XML comparator function"""
        print()
        xmlnice = open(f"{td()}/extract_report/nice-input.xml").read()
        print(xmlnice)
        xmlchanged = minify_xml(open(f"{td()}/extract_report/changed-input.xml").read())
        print(xmlchanged)
        self.assertTrue(compare_xml(xmlnice, xmlnice))
        self.assertTrue(compare_xml(xmlchanged, xmlchanged))
        self.assertFalse(compare_xml(xmlnice, xmlchanged))
        self.assertFalse(compare_xml(xmlchanged, xmlnice))
        print("Passed!")

    def testExtractReportBytes(self):
        """Test extract report function for bytes string input"""
        print()
        file = f"{td()}/extract_report/nice-input.xml"
        with open(file, 'rb') as f:
            data = f.read()
        print("Testing {0}: " .format(file), end="")
        xmlout = extract_report(data)
        xmlin = open(f"{td()}/extract_report/nice-input.xml").read()
        self.assertTrue(compare_xml(xmlout, xmlin))
        print("Passed!")

    def testExtractReportXML(self):
        """Test extract report function for XML input"""
        print()
        file = f"{td()}/extract_report/nice-input.xml"
        print("Testing {0}: " .format(file), end="")
        xmlout = extract_report(file)
        xmlin = open(f"{td()}/extract_report/nice-input.xml").read()
        self.assertTrue(compare_xml(xmlout, xmlin))
        print("Passed!")

    def testExtractReportGZip(self):
        """Test extract report function for gzip input"""
        print()
        file = f"{td()}/extract_report/nice-input.xml.gz"
        print("Testing {0}: " .format(file), end="")
        xmlout = extract_report(file)
        xmlin = open(f"{td()}/extract_report/nice-input.xml").read()
        self.assertTrue(compare_xml(xmlout, xmlin))
        print("Passed!")

    def testExtractReportZip(self):
        """Test extract report function for zip input"""
        print()
        file = f"{td()}/extract_report/nice-input.xml.zip"
        print("Testing {0}: " .format(file), end="")
        xmlout = extract_report(file)
        print(xmlout)
        xmlin = minify_xml(open(f"{td()}/extract_report/nice-input.xml").read())
        print(xmlin)
        self.assertTrue(compare_xml(xmlout, xmlin))
        xmlin = minify_xml(open(f"{td()}/extract_report/changed-input.xml").read())
        print(xmlin)
        self.assertFalse(compare_xml(xmlout, xmlin))
        print("Passed!")

    def testAggregateSamples(self):
        """Test sample aggregate/rua DMARC reports"""
        print()
        sample_paths = glob(f"{td()}/aggregate/*")
        for sample_path in sample_paths:
            if os.path.isdir(sample_path):
                continue
            print("Testing {0}: " .format(sample_path), end="")
            parsed_report = parse_report_file(
                sample_path, always_use_local_files=True)["report"]
            parsed_aggregate_reports_to_csv(parsed_report)
            print("Passed!")

    def testEmptySample(self):
        """Test empty/unparasable report"""
        with self.assertRaises(ParserError):
            parse_report_file(f"{td()}/empty.xml")

    def testForensicSamples(self):
        """Test sample forensic/ruf/failure DMARC reports"""
        print()
        sample_paths = glob(f"{td()}/forensic/*.eml")
        for sample_path in sample_paths:
            print("Testing {0}: ".format(sample_path), end="")
            with open(sample_path) as sample_file:
                sample_content = sample_file.read()
                parsed_report = parse_report_email(
                    sample_content)["report"]
            parsed_report = parse_report_file(
                sample_path)["report"]
            parsed_forensic_reports_to_csv(parsed_report)
            print("Passed!")

    def testSmtpTlsSamples(self):
        """Test sample SMTP TLS reports"""
        print()
        sample_paths = glob(f"{td()}/smtp_tls/*")
        for sample_path in sample_paths:
            if os.path.isdir(sample_path):
                continue
            print("Testing {0}: " .format(sample_path), end="")
            parsed_report = parse_report_file(
                sample_path)["report"]
            parsed_smtp_tls_reports_to_csv(parsed_report)
            print("Passed!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
