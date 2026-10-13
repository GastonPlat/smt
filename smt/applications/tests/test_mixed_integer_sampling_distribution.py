import unittest
import numpy as np
from smt.applications.mixed_integer import MixedIntegerSamplingMethod
from smt.sampling_methods.lhs import LHS
from smt.design_space import DesignSpace, OrdinalVariable, IntegerVariable, CategoricalVariable
from collections import Counter

class TestMixedIntegerSamplingDistribution(unittest.TestCase):
    def test_ordinal_distribution(self):
        design_space = DesignSpace([OrdinalVariable(["low", "medium", "high", "very high"])])
        sampler = MixedIntegerSamplingMethod(LHS, design_space, output_in_folded_space=False)
        samples = sampler(1200)
        decoded = design_space.decode_values(samples)
        counts = Counter(row[0] for row in decoded)

        # Expect ~300 of each
        for level in ["low", "medium", "high", "very high"]:
            self.assertTrue(250 < counts[level] < 350, f"Expected uniform distribution for {level}, got {counts[level]}")

    def test_integer_distribution(self):
        design_space = DesignSpace([IntegerVariable(0, 3)])
        sampler = MixedIntegerSamplingMethod(LHS, design_space, output_in_folded_space=False)
        samples = sampler(1200)
        counts = Counter(row[0] for row in samples)

        for val in [0.0, 1.0, 2.0, 3.0]:
            self.assertTrue(250 < counts[val] < 350, f"Expected uniform distribution for {val}, got {counts[val]}")

    def test_categorical_distribution(self):
        design_space = DesignSpace([CategoricalVariable(["low", "medium", "high", "very high"])])
        sampler = MixedIntegerSamplingMethod(LHS, design_space, output_in_folded_space=False)
        samples = sampler(1200)
        decoded = design_space.decode_values(samples)
        counts = Counter(row[0] for row in decoded)

        for level in ["low", "medium", "high", "very high"]:
            self.assertTrue(250 < counts[level] < 350, f"Expected uniform distribution for {level}, got {counts[level]}")

if __name__ == '__main__':
    unittest.main()
