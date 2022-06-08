==============================================================
HATE-ITA: Hate Speech Detection in Italian Social Media Text
==============================================================



Abstract
--------


Online hate speech is a dangerous phenomenon that can (and should) be promptly counteracted properly. While Natural Language Processing has been successfully used for the purpose, many of the research efforts are directed toward the English language. This choice severely limits the classification power in non-English languages. In this paper, we test several learning frameworks for identifying hate speech in Italian text. We release HATE-ITA, a set of multi-language models trained on a large set of English data and available Italian datasets. HATE-ITA performs better than mono-lingual models and seems to adapt well also on language-specific slurs. We believe our findings will encourage research in other mid-to-low resource communities and provide a valuable benchmarking tool for the Italian community.

See the paper for additional details:

Nozza, D., Bianchi, F., & Attanasio, G. . "HATE-ITA: Hate Speech Detection in Italian Social Media Text". In Proceedings of the 6th Workshop on Online Abuse and Harms (Forthcoming). Association for Computational Linguistics, 2022.

----------

* Free software: MIT license

Installing
----------

.. code-block:: bash

    pip install -U hate-ita

**Important**: If you want to use CUDA you need to install the correct version of
the CUDA systems that matches your distribution, see `PyTorch <https://pytorch.org/get-started/locally/>`__.

Features
--------

.. code-block:: python

    from hate-ita.classifier import HateSpeechClassifier
    hc = HateSpeechClassifier()

    hc.predict(["ti odio", "come si fa a rompere la lavatrice porca puttana"])

    >> ["hate", "non-hate"]


Models
------

+------------+---------------------------------------------+----------------------+
| Model      | Link                                        | Macro F1 on Test Set |
+------------+---------------------------------------------+----------------------+
| HATE-ITA   | https://huggingface.co/MilaNLProc/hate-ita  | 0.83                 |
+------------+---------------------------------------------+----------------------+
| HATE-ITA-L | TBD                                         | TBD                  |
+------------+---------------------------------------------+----------------------+

Reference
---------

If you use this tool please cite the following paper:

.. code-block::

    @inproceedings{bianchi-etal-2022-xlmemo,
    title = {{HATE-ITA}: Hate Speech Detection in Italian Social Media Text},
    author = "Nozza, Debora and Bianchi, Federico and Attanasio, Giuseppe",
    booktitle = "Proceedings of the 6th Workshop on Online Abuse and Harms",
    year = "2022",
    publisher = "Association for Computational Linguistics"
    }

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
