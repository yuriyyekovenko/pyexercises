from ird.tests.utils.wfehelper import WFERestHelper


class BaseTest:

    @classmethod
    def setup_class(cls):
        cls.wfe = WFERestHelper()
