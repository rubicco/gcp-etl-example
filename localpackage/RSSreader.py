import pandas as pd
import time as time
import feedparser


class RSSreader:
    def __init__(self, blog_name, url_rss):
        self.blog_name = blog_name
        self.url = url_rss
        print(f"Request sent: {blog_name}")
        self.feed = feedparser.parse(url_rss)
        print(f"Extract and Transforming started: {blog_name}")
        self.extracted_data = self.__extract_transform()
        print(f"Extract and Transforming ended: {blog_name}")
        self.csv = self.to_csv()
        
    def to_csv(self):
        csv = pd.DataFrame(self.extracted_data)
        csv["blog_name"] = [self.blog_name] * csv.shape[0]
        path_output = f"/tmp/{self.blog_name}.csv"
        csv.to_csv(path_output, index=False)
        print(f"CSV file is written to: {path_output}")
        return csv
    
    def __extract_transform(self, tags=["title", "link", "published_parsed", "description"]):
        # extract the target tags that wanted to be stored in database
        res = []
        for entry in self.feed.entries:
            tmp = {}
            for k in tags:
                if k == "published_parsed":
                    # transform the date for BigQuery
                    tmp[k] = self.__parse_date(entry[k])
                else:
                    tmp[k] = entry[k]
            res.append(tmp)
        return res

    def to_string(self):
        return self.csv.loc[:, ["title", "blog_name"]].to_string()
    
    @staticmethod
    def __parse_date(struct_time):
        return time.strftime("%Y-%m-%d %H:%M:%S %Z", struct_time)
