This repository contains a simple ETL data pipeline that is based on GCP (Cloud Functions and BigQuery).

The pipeline gathers RSS news feed from 2 different sources ([BBC-tech](http://feeds.bbci.co.uk/news/science_and_environment/rss.xml) and [technology.org](http://feeds.feedburner.com/TechnologiesTechnologyOrg?format=xml)), and with a Python 3.7 Cloud Function ETL is done. The data is loaded to BigQuery table.

In order to repeat this simple pipeline, you should follow these steps:

1. [Create a BigQuery table](https://console.cloud.google.com/bigquery) in a project by using the following scheme. Check Useful Links for official guide.

```
[
  {
    "description": "Title of the post.",
    "mode": "NULLABLE",
    "name": "title",
    "type": "STRING"
  },
  {
    "description": "URL to the [pst.",
    "mode": "NULLABLE",
    "name": "link",
    "type": "STRING"
  },
  {
    "description": "Publication date",
    "mode": "NULLABLE",
    "name": "published_parsed",
    "type": "TIMESTAMP"
  },
  {
    "description": "Summary of the post.",
    "mode": "NULLABLE",
    "name": "description",
    "type": "STRING"
  },
  {
    "description": "The webpage that is taken from.",
    "mode": "NULLABLE",
    "name": "blog_name",
    "type": "STRING"
  }
]
```

2. Add table details to the main.py in the TODO lines.

3. zip the `main.py`, `requirements.txt` files and `localpackage` folder to upload it to GCP.

    - In `localpackage` folder, there is a `RSSreader.py` file that handles gathering data, parsing XML file and saving as csv file for a specific RSS feed. You can modify things in need.

4. [Deploy the Cloud Function](https://console.cloud.google.com/functions/list) in GCP. Check Useful Links for Official guide.

5. Finally, you can test the Cloud Function with the request data as follows:

```
{
    "bbc-tech": "http://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
    "techorg": "http://feeds.feedburner.com/TechnologiesTechnologyOrg?format=xml"
}
```

Note that if you add another RSS feed, you may need to modify `RSSreader.py`. 





## Useful-links:

* BigQuery  

    * [Creating BigQuery table](https://cloud.google.com/bigquery/docs/tables#console)
    
    
* Cloud Functions
    * [Quickstart for deployment](https://cloud.google.com/functions/docs/quickstart-console)
    
    * [Quickstart for Python3.7 in Cloud Functions](https://cloud.google.com/functions/docs/quickstart-python)

