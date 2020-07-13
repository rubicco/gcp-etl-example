from localpackage.RSSreader import RSSreader
from google.cloud import bigquery


def import_posts(request):
    request_json = request.get_json()
    
    readers = {blog_name: RSSreader(blog_name, url_rss) 
               for blog_name, url_rss in request_json.items()}

    client = bigquery.Client()
    # TODO: modify the dataset_id and table_id
    dataset_id = 'Technews'
    table_id = 'posts'

    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True

    for blog_name in request_json.keys():
        with open(f"/tmp/{blog_name}.csv", "rb") as source_file:
            job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
        print(f"Data Loading started: {dataset_id}:{table_id}")
        job.result()  # Waits for table load to complete.
        print(f"Data Loading finished: {dataset_id}:{table_id} ({job.output_rows} rows)")
    
    return "\n".join([rss_reader.to_string() for blog_name, rss_reader in readers.items()])
