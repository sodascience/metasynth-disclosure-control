"""Module with the CBS implementations for discrete variables."""

from __future__ import annotations

import polars as pl

from metasyn.distribution.discrete import DiscreteUniformDistribution
from metasyn.distribution.discrete import PoissonDistribution
from metasyn.distribution.discrete import UniqueKeyDistribution

from metasyncontrib.disclosure.numerical import DisclosureNumerical
from metasyncontrib.disclosure.utils import micro_aggregate
from metasyncontrib.disclosure.base import metadist_disclosure


@metadist_disclosure()
class DisclosureDiscreteUniform(DisclosureNumerical, DiscreteUniformDistribution):
    """Implementation for discrete uniform distribution."""


@metadist_disclosure()
class DisclosureUniqueKey(UniqueKeyDistribution):
    """Implementation for unique key distribution."""

    @classmethod
    def _fit(cls, values: pl.Series, n_avg: int = 11):
        orig_dist = super()._fit(values)
        if orig_dist.consecutive == 1:
            return cls(0, 1)
        sub_values = micro_aggregate(values, n_avg)
        return super()._fit(sub_values)


@metadist_disclosure()
class DisclosurePoisson(DisclosureNumerical, PoissonDistribution):
    """Disclosure implementation for Poisson distribution."""