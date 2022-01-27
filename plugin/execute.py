from plugin.detectors.fake_recharge import FakeRecharge

def make_plugin():
    plugin_detectors = [FakeRecharge]
    plugin_printers = []

    return plugin_detectors, plugin_printers