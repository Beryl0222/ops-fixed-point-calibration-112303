"""检查交换数据中用于回查的事实。"""
import unittest

import numpy as np

from fixed_point_calibration_input import load_record


class ExchangeRecordTests(unittest.TestCase):
    def test_exchange_contract(self):
        record = load_record()
        self.assertTrue(record["calibration"][2]["id"] == record["calibration"][3]["id"] and record["calibration"][2]["bins"][0][0] != record["calibration"][3]["bins"][0][0])
        self.assertTrue(record["tails"]["dry"] != record["tails"]["wet"])
        self.assertTrue(len(set(record["device"]["scales"])) >= 5 and len(record["device"]["zero_points"]) >= 2)
        self.assertTrue(max(record["device"]["bias"]) > 2**(record["device"]["accumulator_bits"]-2))
