"""
test code to demonstrate "pytest"

See the URL below for how to execute on VS code.
https://hiroronn.hatenablog.jp/entry/20180905/1536146652
To add pytest arguments, edit "python.testing.pytestArgs".

Notes
------
modules pytest-cov and pytest-xdist are needed to check test covarage.
execute command below on tarminal.
> pytest test_pytest.py --cov=target
execute command below to know where is missed.
> pytest test_pytest.py --cov=target --cov-report term-missing
"""

import pytest

import target


IS_DETAILTEST=True

# # function format is also valid. 
# def test_add_num_double():
#     """test function
#     
#     Notes
#     -------
#     The name of test function must start
#     with "test_" 
#     """
#     tar = target.TargetClass()
#     assert tar. add_num_and_double(1,2) == 6


# here is class format
# more useful in many case
class TestCal():
    def setup_method(self,method):
        print('\n ===start:{}'.format(method.__name__))
        self.tar = target.TargetClass()

    def teardown_method(self,method):
        print('\n ===end::{}'.format(method.__name__))
        del self.tar

    def test_add_num_double(self):
        """value test function

        Notes
        -------
        The name of all test function must start
        with "test_" 
        """
        assert self.tar.add_num_and_double(1,2) == 6

    # @pytest.mark.skip(reason="skip!!!!") # skip unconditionally
    @pytest.mark.skipif(IS_DETAILTEST==False, reason="not so important")
    def test_add_num_and_double_raise(self):
        """exception test function
        """
        with pytest.raises(ValueError):
            self.tar.add_num_and_double("1","2")

    @pytest.mark.skipif(IS_DETAILTEST==False, reason="not so important")
    def test_even_or_odd_raise(self):
        """exception test function
        """
        with pytest.raises(ValueError):
            self.tar.even_or_odd("1")

    def test_even_or_odd_sign(self):
        assert self.tar.even_or_odd(-1) == None

    def test_even_or_odd_even(self):
        assert self.tar.even_or_odd(4) == 0

    def test_even_or_odd_odd(self):
        assert self.tar.even_or_odd(15) == 1


