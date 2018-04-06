# -*- coding: utf-8 -*-

from journalist_app import create_app


class UpgradeTester():

    def __init__(self, config):
        self.config = config
        self.app = create_app(config)

    def load_data(self):
        pass

    def check_upgrade(self):
        pass


class UpgradeTester():

    def __init__(self, config):
        self.config = config
        self.app = create_app(config)

    def load_data(self):
        pass

    def check_downgrade(self):
        pass
