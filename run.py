from unittestreport import TestRunner
import unittest
import time
import datetime
testsuite = unittest.defaultTestLoader.discover(r"D:\credit\test_case")
now_time = time.strftime("%Y_%m_%d")
file_name = now_time + '.html'
runner = TestRunner(testsuite, filename=file_name, report_dir=r"D:\credit\report", templates=3)
runner.run()
