"""
A package containing utility functions for computational MRI exercises.

Author          : Jinho Kim
Email           : jinho.kim@fau.de
"""

from pathlib import Path
from typing import Optional

import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np
import scipy.io


def _get_root():
    return Path(__file__).parent

def load_data(fname):
    root = _get_root()
    assert fname.endswith(".mat"), "The filename must contain the .mat extension"
    mat = scipy.io.loadmat(root / fname)
    return mat


def imshow(
    imgs: list,
    titles: Optional[list] = None,
    suptitle: Optional[str] = None,
    root: Optional[Path] = None,
    filename: Optional[str] = None,
    fig_size: Optional[tuple] = None,
    save_indiv: bool = False,
    num_rows: int = 1,
    pos: Optional[list] = None,
    norm: Optional[float] = None,
    is_mag: bool = True,
):
    """
    This function displays multiple images in a single row.
    Args:
        imgs:           list of images to display
        titles:         list of titles for each image, optional
        suptitle:       main title for the figure, optional        
        root:           Root path to save, optional
        filename:       name of the file to save the figure, optional
        fig_size:       figure size, default is (15,10)        
        save_indiv:     Save individual images or not        
        num_rows:       The number of rows of layout (a single row by default)
        pos:            Position of images.
                        ex) for 2x3 layout, [1,1,1,0,1,1] plots images like
                                            ===============
                                            img1 img2 img3
                                                 img4 img5
                                            ===============
                        ex) for 2x3 layout with gt given, [1,1,1,0,1,1] plots images like
                                            ===============
                                            gt img1 img2 img3
                                                    img4 img5
                                            ===============
        norm:           normalization factor, default is 1.0
        is_mag:         plot images in magnitude scale or not (optional, default=True)
    """

    pos, num_cols = _get_pos(pos, num_rows=num_rows, num_imgs=len(imgs))

    if fig_size is None:
        fig_size = (num_cols * 5, num_rows * 4 + 0.5)

    f = plt.figure(figsize=fig_size)
    titles = [None] * len(imgs) if titles is None else titles

    img_idx = 0
    for i, pos_indiv in enumerate(pos, start=1):
        ax = f.add_subplot(num_rows, num_cols, i)

        if pos_indiv == 0:
            img = np.ones_like(imgs[0], dtype=float)
            title = ""
        else:
            img = np.abs(imgs[img_idx]) if is_mag else imgs[img_idx]
            title = titles[img_idx]
            img_idx += 1

        if norm is None:
            ax.imshow(img, cmap="gray")
        else:
            norm_method = clr.Normalize() if norm == 1.0 else clr.PowerNorm(gamma=norm)
            ax.imshow(img, cmap="gray", norm=norm_method)
        ax.axis("off")
        ax.set_title(title)

    f.suptitle(suptitle) if suptitle is not None else f.suptitle("")

    if root is None:
        root = _get_root()
    if isinstance(root, str):
        root = Path(root)
    root = root / "Results"
    if not root.exists() and filename:
        root.mkdir(parents=True, exist_ok=True)

    if filename is None:
        plt.show()

    elif filename is not None:
        print(f"Saving figure to {root}")
        plt.savefig(root / filename, bbox_inches="tight", pad_inches=0.3)
        plt.close(f)
        if save_indiv:
            for img, title in zip(imgs, titles):
                img = abs(img)
                title = title.split("\n")[0]
                plt.imshow(img, cmap="gray", norm=clr.PowerNorm(gamma=norm))
                plt.axis("off")
                plt.savefig(
                    root / f"{filename}_{title}",
                    bbox_inches="tight",
                    pad_inches=0.2,
                )


def _get_pos(pos, num_rows, num_imgs):
    num_cols = np.ceil(num_imgs / num_rows).astype(int)
    len_pos = num_rows * num_cols

    if pos is None:
        pos = [1] * num_imgs + [0] * (len_pos - num_imgs)
    else:  # if pos is given
        assert np.count_nonzero(pos) == num_imgs, "Givin pos are not matched to the number of given images"
        res = len_pos - len(pos)
        pos += [0] * res

    return pos, num_cols
