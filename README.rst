==============================================================
HATE-ITA: Hate Speech Detection in Italian Social Media Text
==============================================================

`Debora Nozza <http://dnozza.github.io/>`_ •
`Federico Bianchi <https://federicobianchi.io/>`_ •
`Giuseppe Attanasio <https://gattanasio.cc/>`_

Model description
--------

HATE-ITA is a binary hate speech classification model for Italian social media text.

.. image:: https://github.com/MilaNLProc/hate-ita/blob/main/hateita.png
   :align: center
   :width: 200px

See the paper for additional details:

Debora Nozza, Federico Bianchi, and Giuseppe Attanasio. 2022. HATE-ITA: New Baselines for Hate Speech Detection in Italian. In Proceedings of the Sixth Workshop on Online Abuse and Harms (WOAH), pages 252–260, Seattle, Washington (Hybrid). Association for Computational Linguistics. `Link <https://aclanthology.org/2022.woah-1.24/>`_

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

    >> ["hate", "not-hate"]


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

    @inproceedings{nozza-etal-2022-hate-ita,
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