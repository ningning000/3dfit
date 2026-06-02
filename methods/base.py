# methods/base.py

from abc import ABC, abstractmethod


class BaseEstimator(ABC):

    @abstractmethod
    def estimate(self, roi):
        """
        Parameters
        ----------
        roi : dict

        Returns
        -------
        result : dict
        """
        pass
