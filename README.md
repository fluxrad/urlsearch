# URLSearch

From the amills "Learn more Python" series. Search a URL a specified string and notify if it exists/doesn't exist.

## Files
***

### urlsearch.cfg
Config file for the urlsearch script/module. See: urlsearch.cfg.example.

**Options:**

**sns_topic** (optional): The ARN for an Amazon SNS topic. Used for a pub/sub notification system.

**sns_region** (optional): The SNS region to connect to. Probably us-east-1

**search_url**: The URL to request for searching

**search_string**: String to search for. By default, the script notifies if this string is _absent_. This behavior can be altered in urlsearch.py

### ~/.boto

In order to make use of AWS SNS functionality to send notifications via
email/SMS, you'll need to install and configure boto. You can read more about
boto [here](http://docs.pythonboto.org/en/latest/). Once you've installed boto,
be sure to create your user's ~/.boto config file with the following info:

    [Credentials]
    aws_access_key_id = YOUR_AWS_KEY_ID
    aws_secret_access_key = YOUR_AWS_KEY
