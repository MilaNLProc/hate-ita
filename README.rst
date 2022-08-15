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



License
-------

Code comes from HuggingFace and thus our License is an MIT license.

For models restriction may apply on the data (which are derived from existing datasets) or Twitter (main data source). We refer users to the original licenses accompanying each dataset and Twitter regulations.

Installing
----------

.. code-block:: bash
    !git clone https://github.com/MilaNLProc/hate-ita/
    !cd hate-ita
    pip install -e .

**Important**: If you want to use CUDA you need to install the correct version of
the CUDA systems that matches your distribution, see `PyTorch <https://pytorch.org/get-started/locally/>`__.

Features
--------

.. code-block:: python

    from hate_ita.classifier import HateSpeechClassifier
    hc = HateSpeechClassifier()

    hc.predict(["ti odio", "come si fa a rompere la lavatrice porca puttana"])

    >> ["hate", "not-hate"]


Models
------

We release three models (see the paper for reference).

.. code-block:: python

    from hate_ita.classifier import HateSpeechClassifier
    hc = HateSpeechClassifier("twitter")

    hc = HateSpeechClassifier("base")

    hc = HateSpeechClassifier("large")


Reference
---------

If you use this tool please cite the following paper:

.. code-block::

   @inproceedings{nozza-etal-2022-hate,
       title = "{HATE}-{ITA}: Hate Speech Detection in {I}talian Social Media Text",
       author = "Nozza, Debora  and
         Bianchi, Federico  and
         Attanasio, Giuseppe",
       booktitle = "Proceedings of the Sixth Workshop on Online Abuse and Harms (WOAH)",
       month = jul,
       year = "2022",
       address = "Seattle, Washington (Hybrid)",
       publisher = "Association for Computational Linguistics",
       url = "https://aclanthology.org/2022.woah-1.24",
       doi = "10.18653/v1/2022.woah-1.24",
       pages = "252--260"
   }

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
