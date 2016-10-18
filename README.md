datapilot4
==============================

#Identifying Innovative Networks in Wales from Web Data

In this, the fourth data pilot for Welsh Government's Arloesiadur platform, we attemp to identify networks of innovative actors based on a 'seed' of organisations. We use the seed nodes as a 'base' network, using an iterative method to add new nodes (and edges) based on the identification of edges through web data crawling (social media, company websites, shared officers, etc.).

Due to the nature of this project's data (being personal, identifiable information) we are unable to upload either the raw data we use to populate the base network nor the data we generate through our web crawls. Whilst this is at odds with the value we place on openness, it is a necessary choice that allows us to carry out the data pilot in a reasonable amount of time.

In the future, we hope to carry out network creation using open data sources (such as Companies House), which would allow us to open up our analyses even further. Until then, we will continue to release our code under an open source license, thereby ensuring that our methods are open, transparent and, where users are able to access the data, reproducible.

## Base Network

Our base network consists of 281 companies that took part in Welsh Government's [Accelerated Growth Programme](https://businesswales.gov.wales/growth/). Each node in the network can contain the following variables:

    - Registered Company Name
    - Billing Postal Code
    - Website URL
    - Phone number
    - Email address
    - Main Contact (Full name)
    - Main Contact (Job title)
    - Main Contact (Phone number)
    - Mobile number

It should be noted that not all of the nodes have assigned values for all of the above variables.

## Method

We first look at the behaviour of the organizations in the base network to determine whether they are displaying innovative characteristics. Due to this being a pilot project, we are being very selective with the characteristics - both in terms of the number of potential sources we are looking at and the way in which we are analyzing them. The behaviours we will look at are:
    - Evidence of active patenting
    - Evidence of Innovate UK funded activity
    - The language of a Company's website and other online presence

The first two of the behaviours are self explanatory. The third is related to processing the language of a company's online presence, to identify whether that company self-identifies innovative behaviours in its online literature, such as exploration of new technologies, or the bringing of new products to the market.

Once we have identified their behaviours, we classify the organisation as 'innovative' or 'not-innovative'. These are semantic choices, and refer only to the behaviour of the company in the limited scope of our analysis. We actively crawl data relating to the 'innovative' organisations to identify links to other organisations.

The sources we are looking at to identify links to other organisations are:

- Companies House
- Twitter
- Company Websites
- Gateway to Research

Once we have crawled each of the data sources for each of the organisations, we repeat the process of identifying innovative behaviour outlined above for new organisations added to the network. Edges between organisations are also stored at this point, allowing us to recreate a network graph from the data for analysis and visualisation purposes. In some cases, links will be identified to organisations already present in the network. In this case, new edges will be created, but no further crawling on the organisation will be carried out.

The process is repeated for an inderteminate amount of iterations, or until no further organisational links are identified.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
