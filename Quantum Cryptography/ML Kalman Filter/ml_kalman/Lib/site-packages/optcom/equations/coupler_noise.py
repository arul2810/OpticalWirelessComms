# Copyright 2019 The Optcom Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""".. moduleauthor:: Sacha Medaer"""

from typing import Callable, List, Optional, overload, Union

import numpy as np

import optcom.utils.constants as cst
import optcom.utils.utilities as util
from optcom.field import Field
from optcom.equations.abstract_equation import AbstractEquation
from optcom.utils.id_tracker import IdTracker


class CouplerNoise(AbstractEquation):
    r"""Calculate the noise propagation in fiber coupler.


    Notes
    -----

    .. math:: \begin{split}
                \frac{\partial P_{ljw}}{\partial z} = & 2i
                \sum_{\substack{m=1 \\ m\neq l}}^{M} \sum_{k=1}^{K_m}
                \sum_{n=1}^{W_k} \kappa_{lmn} P_{mkn}
                + 2i \sum_{\substack{m=1 \\ m\neq l}}^{M} \delta_{almw}
                P_{ljw} \\
                & \text{for }
                  \begin{cases}
                    l = 1,\ldots,M \text{ with } M
                    \text{ the number of cores}\\
                    j = 1,\ldots,K_l \text{ with } K_l
                    \text{ the number of noise channels in core } l\\
                    w = 1,\ldots,W_j \text{ with } W_j
                    \text{ the number of wavelength constituents }
                    \text{of noise channel j}
                  \end{cases}
             \end{split}

    """

    def __init__(self, asymmetry_coeff: List[Callable],
                 coupling_coeff: List[Callable],
                 noise_omega: np.ndarray, id_tracker: IdTracker) -> None:
        r"""
        Parameters
        ----------
        asymmetry_coeff :
            The asymmetry coefficient of the noise.
        coupling_coeff :
            The coupling coefficient of the noise.
        noise_omega :
            The angular frequencies composing the noise array.
            :math:`[ps^{-1}]`
        id_tracker : optcom.utils.id_tracker.IdTracker
            The IdTracker of the corresponding CNLSE.

        """
        self._noise_omega: np.ndarray = noise_omega
        asym_coeff_callable: List[Callable] = asymmetry_coeff
        coup_coeff_callable: List[Callable] = coupling_coeff
        self._asym_coeff: List[np.ndarray] = []
        self._coup_coeff: List[np.ndarray] = []
        for i in range(len(asym_coeff_callable)):
            self._asym_coeff.append(asym_coeff_callable[i](noise_omega))
        for i in range(len(coup_coeff_callable)):
            self._coup_coeff.append(coup_coeff_callable[i](noise_omega))
        self._id_tracker: IdTracker = id_tracker
    # ==================================================================
    @overload
    def __call__(self, noises: np.ndarray, z: float, h: float
                 )-> np.ndarray: ...
    # ------------------------------------------------------------------
    @overload
    def __call__(self, noises: np.ndarray, z: float, h: float, ind: int
                 ) -> np.ndarray: ...
    # ------------------------------------------------------------------
    def __call__(self, *args):
        if (len(args) == 4):
            noises, z, h, ind = args
            asym_term: np.ndarray = np.zeros_like(noises[ind])
            coup_term: np.ndarray = np.zeros_like(noises[ind])
            eq_id: int = self._id_tracker.eq_id_of_field_id(ind)
            for i in range(len(noises)):
                eq_id_: int = self._id_tracker.eq_id_of_field_id(i)
                if (eq_id_ != eq_id):
                        rel_pos = eq_id_ if (eq_id_ < eq_id) else (eq_id_ - 1)
                        asym_term += 2j*noises[i]*self._asym_coeff[rel_pos]
                        coup_term += 2j*noises[i]*self._coup_coeff[rel_pos]

            return asym_term + coup_term
        else:

            raise NotImplementedError()
