from pytest import mark

from metasyn.distribution.constant import (
    ConstantDistribution,
    DiscreteConstantDistribution,
    StringConstantDistribution,
    DateTimeConstantDistribution,
    TimeConstantDistribution,
    DateConstantDistribution,
)

from metasyncontrib.disclosure.constant import (
    DisclosureConstant,
    DisclosureDiscreteConstant,
    DisclosureStringConstant,
    DisclosureDateTimeConstant,
    DisclosureTimeConstant,
    DisclosureDateConstant,
)

@mark.parametrize(
    "dist_builtin, dist_disclosure, value",
    [
        (ConstantDistribution, DisclosureConstant, 8.0),
        (DiscreteConstantDistribution, DisclosureDiscreteConstant, 8),
        (StringConstantDistribution, DisclosureStringConstant, "Secretvalue"),
        (DateTimeConstantDistribution, DisclosureDateTimeConstant, "2024-02-23T12:08:38+00:00"),
        (TimeConstantDistribution, DisclosureTimeConstant, "12:08:38"),
        (DateConstantDistribution, DisclosureDateConstant, "2024-02-23")
    ]
)
def test_constant(dist_builtin, dist_disclosure, value):
    dist = dist_builtin(value)
    data = [dist.draw() for _ in range(21)]
    
    assert dist_disclosure.fit(data, n_avg = 22)._param_dict().get("value") != value
    assert dist_disclosure.fit(data, n_avg = 11)._param_dict().get("value") == value