# methods/gpe/gabor.py

import cv2
import numpy as np


def complex_gabor(
    frame,
    ksize=31,
    sigma=4.0,
    theta=np.pi/2,
    lambd=12.0
):
    """
    Complex Gabor filter.
    """

    real_kernel = cv2.getGaborKernel(
        (ksize, ksize),
        sigma,
        theta,
        lambd,
        gamma=0.5,
        psi=0
    )

    imag_kernel = cv2.getGaborKernel(
        (ksize, ksize),
        sigma,
        theta,
        lambd,
        gamma=0.5,
        psi=np.pi/2
    )

    real_resp = cv2.filter2D(
        frame,
        cv2.CV_32F,
        real_kernel
    )

    imag_resp = cv2.filter2D(
        frame,
        cv2.CV_32F,
        imag_kernel
    )

    return (
        real_resp
        +
        1j * imag_resp
    )
