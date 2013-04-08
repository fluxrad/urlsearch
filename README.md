# URLSearch

From the amills "Learn more Python" series. Search a URL a specified string and notify if it exists/doesn't exist.

# urlsearch.cfg

Config file for the urlsearch script/module. See: urlsearch.cfg.example.

**Options:**

**sns_topic** (optional): The ARN for an Amazon SNS topic. Used for a pub/sub notification system.

**sns_region** (optional): The SNS region to connect to. Probably us-east-1

**search_url**: The URL to request for searching

**search_string**: String to search for. By default, the script notifies if this string is _absent_. This behavior can be altered in urlsearch.py

