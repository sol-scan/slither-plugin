from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.core.declarations.function_contract import FunctionContract
from slither.slithir.operations import Return


class FakeRecharge(AbstractDetector):
    """
    假充值检测
    """

    ARGUMENT = "fake-recharge"
    HELP = "ERC20代币转账失败但交易成功"
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.LOW

    WIKI = "https://github.com/sol-scan/slither-plugin/wiki/Detector-Documentation#ERC20%E4%BB%A3%E5%B8%81%E8%BD%AC%E8%B4%A6%E5%A4%B1%E8%B4%A5%E4%BD%86%E4%BA%A4%E6%98%93%E6%88%90%E5%8A%9F"

    WIKI_TITLE = "ERC20代币转账失败但交易成功"
    WIKI_DESCRIPTION = "ERC20代币transfer时，会返回bool，若用户在转账失败时，未让交易失败，而是返回false，则具有假充值的风险"

    # region wiki_exploit_scenario
    WIKI_EXPLOIT_SCENARIO = """
```solidity
contract ERC20FackRecharge {
    // ...
    function transfer(address _to, uint256 _value) public returns (bool) {
        if (balances[msg.sender] >= _value && _value > 0) {
            balances[msg.sender] -= _value;
            balances[_to] += _value;
            return true;
        } else {
            return false;
        }
    }

    // ...
}
```
"""
    # endregion wiki_exploit_scenario

    WIKI_RECOMMENDATION = "转账失败时，使用require或者revert"

    def _detect(self):
        results = []

        targets = []
        for c in self.contracts:
            for f in c.functions_declared:
                if f.signature_str == 'transfer(address,uint256) returns(bool)':
                    targets.append(f)
        for t in targets:
            f: FunctionContract = t
            for n in f.nodes:
                for ir in n.irs:
                    if isinstance(ir, Return) and str(n.expression) == 'false':
                        info = self.generate_result(
                            ["return ", n, "maybe fake recharge\n"])
                        results.append(info)

        return results
