"""
Computational Magnetic Resonance Imaging (CMRI) 2024/2025 Winter semester

- Author          : Jinho Kim
- Email           : <jinho.kim@fau.de>
"""

import numpy as np
import utils


class Lab01_op:
    """
    label: Label map of the digital brain phantom
        - 1: Cerebrospinal fluid (CSF)
        - 2: Gray matter (GM)
        - 3: White matter (WM)
    T1_map: Predefined T1 Values
    T2_map: Predefined T2 Values
    PD_map: Proton Density Values
    """

    def __init__(self):
        # Define TR and TE as a pair in a list [TR, TE]
        self.PDw_TRTE = None  # Task 2.2
        self.T1w_TRTE = None  # Task 2.3
        self.T2w_TRTE = None  # Task 2.4

    def load_data(self, path="digital_brain_phantom.mat"):
        mat = utils.load_data(path)
        self.label = mat["ph"]["label"][0][0]  # (128, 128)
        self.T1_map = mat["ph"]["t1"][0][0]  # (128, 128)
        self.T2_map = mat["ph"]["t2"][0][0]  # (128, 128)
        self.PD_map = mat["ph"]["sd"][0][0]  # (128, 128)

    def get_csf_mask(self):
        """
        Get CSF mask from the label map
        Return:
            A mask of CSF, shape: (128, 128)
        """
        mask = np.zeros_like(self.label, dtype=np.uint8)
        rows, cols = self.label.shape
        for i in range(rows):
            for j in range(cols):
                if self.label[i, j] == 1:
                    mask[i, j] = 1
        return mask

    def get_gm_mask(self):
        """
        Get GM mask from the label map
        Return:
            A mask of GM, shape: (128, 128)
        """
        mask = np.zeros_like(self.label, dtype=np.uint8)
        rows, cols = self.label.shape
        for i in range(rows):
            for j in range(cols):
                if self.label[i, j] == 2:
                    mask[i, j] = 1
        return mask

    def get_wm_mask(self):
        """
        Get WM mask from the label map
        Return:
            A mask of WM, shape: (128, 128)
        """
        mask = np.zeros_like(self.label, dtype=np.uint8)
        rows, cols = self.label.shape
        for i in range(rows):
            for j in range(cols):
                if self.label[i, j] == 3:
                    mask[i, j] = 1
        return mask

        return None

    def get_T1(self, target):
        """
        Returns the T1 value of the target region

        Args:
            target: A mask of the target region (CSF, GM, WM), shape: (128, 128)
        Return:
            T1 value of the target region in [ms]
        """
        # Your code here ...

        T1_ms = None
        return T1_ms

    def get_T2(self, target):
        """
        Returns the T2 value of the target region

        Args:
            target: A mask of the target region (CSF, GM, WM), shape: (128, 128)
        Return:
            T2 value of the target region in [ms]
        """
        # Your code here ...

        T2_ms = None
        return T2_ms

    def get_PD(self, target):
        """
        Returns the PD value of the target region

        Args:
            target: A mask of the target region (CSF, GM, WM), shape: (128, 128)
        Return:
            PD value of the target region
        """
        # Your code here ...

        PD = None
        return PD

    def spin_echo(self, TR, TE):
        """
        Simulate a spin echo sequence

        Args:
            TR: Repetition time in [ms]
            TE: Echo time in [ms]
        Return:
            A 2D image of the spin echo sequence, shape: (128, 128)
        """
        # Your code here ...

        SE = None
        return SE


if __name__ == "__main__":
    # %% Load modules
    # This import is necessary to run the code cell-by-cell
    from lab01 import *

    # %% Define the object
    op = Lab01_op()

    # %% 1.1.	Load the file digital_brain_phantom.mat by calling load_data method.
    op.load_data()